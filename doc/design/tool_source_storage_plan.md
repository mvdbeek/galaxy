# Tool Source Storage Backend Implementation Plan

## Overview

This plan builds on [PR #21278](https://github.com/galaxyproject/galaxy/pull/21278) to create a configurable, pluggable tool source storage system. The goal is to enable storing and retrieving tool sources from multiple backends (database, Redis, disk) with support for incremental population and performance benchmarking.

## Background

### Current State (PR #21278)

PR #21278 introduces:
- `DatabaseToolBox` class that loads tools from the database for non-webapp job handlers
- `ToolSource` model in `lib/galaxy/model/__init__.py:1391` with `hash` and `source` (JSON) columns
- Integration with `ToolRequest` for job tool state tracking

### Existing Infrastructure

- **ToolSource Classes** (`lib/galaxy/tool_util/parser/`):
  - `ToolSource` abstract base class with `to_string()` method
  - `XmlToolSource`, `YamlToolSource`, `CwlToolSource` implementations
  - Factory pattern in `factory.py` with `TOOL_SOURCE_FACTORIES`

- **ObjectStore Pattern** (`lib/galaxy/objectstore/`):
  - Abstract `ObjectStore` base class with pluggable backends
  - Implementations: disk, S3, Azure, etc.
  - Configuration via YAML/XML

- **Redis Dependency**: Already available for Celery (`redis>=5.3.0`)

---

## Architecture

### 1. Storage Backend Interface

Create a new abstract base class for tool source storage:

```
lib/galaxy/tool_source_store/
    __init__.py           # ToolSourceStore ABC and factory
    database.py           # DatabaseToolSourceStore
    redis.py              # RedisToolSourceStore
    disk.py               # DiskToolSourceStore
    models.py             # StoredToolSource dataclass
```

#### Core Interface (`lib/galaxy/tool_source_store/__init__.py`)

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict, List, Iterator
from datetime import datetime

@dataclass
class StoredToolSource:
    """Representation of a stored tool source."""
    hash: str                          # Content hash (SHA256)
    tool_source_class: str             # XmlToolSource, YamlToolSource, etc.
    raw_source: str                    # Serialized tool source string
    tool_id: Optional[str] = None      # Tool ID if known
    tool_version: Optional[str] = None # Tool version if known
    tool_dir: Optional[str] = None     # Original tool directory
    stored_at: Optional[datetime] = None
    metadata: Optional[Dict] = None    # Additional metadata

class ToolSourceStore(ABC):
    """Abstract base class for tool source storage backends."""

    @abstractmethod
    def store(self, tool_source: StoredToolSource) -> str:
        """Store a tool source, returns the storage key (hash)."""
        pass

    @abstractmethod
    def get(self, hash: str) -> Optional[StoredToolSource]:
        """Retrieve a tool source by hash."""
        pass

    @abstractmethod
    def exists(self, hash: str) -> bool:
        """Check if a tool source exists."""
        pass

    @abstractmethod
    def delete(self, hash: str) -> bool:
        """Delete a tool source by hash."""
        pass

    @abstractmethod
    def list_all(self) -> Iterator[str]:
        """List all stored tool source hashes."""
        pass

    @abstractmethod
    def get_by_tool_id(self, tool_id: str, version: Optional[str] = None) -> List[StoredToolSource]:
        """Get tool sources by tool ID and optional version."""
        pass

    @abstractmethod
    def count(self) -> int:
        """Return the total number of stored tool sources."""
        pass

    def get_stats(self) -> Dict:
        """Return storage statistics."""
        return {"count": self.count()}
```

### 2. Backend Implementations

#### 2.1 Database Backend (`lib/galaxy/tool_source_store/database.py`)

Extends the existing `ToolSource` model from PR #21278.

**Schema Changes** - New migration to add columns to `tool_source` table:
```python
# Add to existing tool_source table
tool_source_class: Mapped[str] = mapped_column(Unicode(64))
tool_id: Mapped[Optional[str]] = mapped_column(Unicode(255), index=True)
tool_version: Mapped[Optional[str]] = mapped_column(Unicode(64))
tool_dir: Mapped[Optional[str]] = mapped_column(Unicode(1024))
stored_at: Mapped[datetime] = mapped_column(default=now)
metadata_json: Mapped[Optional[dict]] = mapped_column(JSONType)
```

**Implementation**:
```python
class DatabaseToolSourceStore(ToolSourceStore):
    def __init__(self, session_factory):
        self._session_factory = session_factory

    def store(self, tool_source: StoredToolSource) -> str:
        with self._session_factory() as session:
            existing = session.query(ToolSourceModel).filter_by(hash=tool_source.hash).first()
            if existing:
                return existing.hash
            model = ToolSourceModel(
                hash=tool_source.hash,
                source={"raw": tool_source.raw_source},
                tool_source_class=tool_source.tool_source_class,
                tool_id=tool_source.tool_id,
                tool_version=tool_source.tool_version,
                tool_dir=tool_source.tool_dir,
                metadata_json=tool_source.metadata,
            )
            session.add(model)
            session.commit()
            return model.hash
```

#### 2.2 Redis Backend (`lib/galaxy/tool_source_store/redis.py`)

Uses Redis for high-performance caching/storage.

**Key Structure**:
```
tool_source:{hash}           -> JSON blob of StoredToolSource
tool_source:index:tool_id:{tool_id} -> Set of hashes
tool_source:index:version:{tool_id}:{version} -> Set of hashes
tool_source:all              -> Set of all hashes
```

**Implementation**:
```python
import json
from redis import Redis

class RedisToolSourceStore(ToolSourceStore):
    PREFIX = "tool_source"

    def __init__(self, redis_url: str, ttl: Optional[int] = None):
        self._redis = Redis.from_url(redis_url, decode_responses=True)
        self._ttl = ttl  # Optional TTL in seconds

    def store(self, tool_source: StoredToolSource) -> str:
        key = f"{self.PREFIX}:{tool_source.hash}"
        data = {
            "hash": tool_source.hash,
            "tool_source_class": tool_source.tool_source_class,
            "raw_source": tool_source.raw_source,
            "tool_id": tool_source.tool_id,
            "tool_version": tool_source.tool_version,
            "tool_dir": tool_source.tool_dir,
            "stored_at": tool_source.stored_at.isoformat() if tool_source.stored_at else None,
            "metadata": tool_source.metadata,
        }
        pipe = self._redis.pipeline()
        if self._ttl:
            pipe.setex(key, self._ttl, json.dumps(data))
        else:
            pipe.set(key, json.dumps(data))
        pipe.sadd(f"{self.PREFIX}:all", tool_source.hash)
        if tool_source.tool_id:
            pipe.sadd(f"{self.PREFIX}:index:tool_id:{tool_source.tool_id}", tool_source.hash)
            if tool_source.tool_version:
                pipe.sadd(
                    f"{self.PREFIX}:index:version:{tool_source.tool_id}:{tool_source.tool_version}",
                    tool_source.hash
                )
        pipe.execute()
        return tool_source.hash
```

#### 2.3 Disk Backend (`lib/galaxy/tool_source_store/disk.py`)

File-based storage with directory structure.

**Directory Structure**:
```
{base_path}/
    sources/
        {hash[:2]}/
            {hash[2:4]}/
                {hash}.json
    index/
        tool_id/
            {tool_id}.json  # List of hashes
        version/
            {tool_id}/
                {version}.json  # List of hashes
```

**Implementation**:
```python
import os
import json
from pathlib import Path

class DiskToolSourceStore(ToolSourceStore):
    def __init__(self, base_path: str):
        self._base_path = Path(base_path)
        self._sources_path = self._base_path / "sources"
        self._index_path = self._base_path / "index"
        self._sources_path.mkdir(parents=True, exist_ok=True)
        self._index_path.mkdir(parents=True, exist_ok=True)

    def _source_path(self, hash: str) -> Path:
        return self._sources_path / hash[:2] / hash[2:4] / f"{hash}.json"

    def store(self, tool_source: StoredToolSource) -> str:
        path = self._source_path(tool_source.hash)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "hash": tool_source.hash,
            "tool_source_class": tool_source.tool_source_class,
            "raw_source": tool_source.raw_source,
            "tool_id": tool_source.tool_id,
            "tool_version": tool_source.tool_version,
            "tool_dir": tool_source.tool_dir,
            "stored_at": tool_source.stored_at.isoformat() if tool_source.stored_at else None,
            "metadata": tool_source.metadata,
        }
        with open(path, 'w') as f:
            json.dump(data, f)
        self._update_indexes(tool_source)
        return tool_source.hash
```

### 3. Factory and Configuration

#### Configuration Schema (`lib/galaxy/config/schemas/config_schema.yml`)

Add new configuration options:

```yaml
tool_source_store:
  type: str
  default: database
  desc: |
    Backend for storing tool sources. Options: database, redis, disk.

tool_source_store_config_file:
  type: str
  default: null
  path_resolves_to: config_dir
  desc: |
    Path to tool source store configuration file (YAML format).

tool_source_redis_url:
  type: str
  default: null
  desc: |
    Redis URL for tool source storage when using redis backend.
    Example: redis://localhost:6379/1

tool_source_disk_path:
  type: str
  default: tool_sources
  path_resolves_to: data_dir
  desc: |
    Directory path for tool source storage when using disk backend.
```

#### Sample Configuration (`lib/galaxy/config/sample/tool_source_store_conf.sample.yml`)

```yaml
# Tool Source Store Configuration
#
# Configures where Galaxy stores serialized tool sources for
# dynamic tool loading by job handlers.

# Backend type: database, redis, or disk
backend: database

# Database backend configuration (default)
database:
  # Uses Galaxy's main database connection by default
  # connection: null

# Redis backend configuration
redis:
  url: redis://localhost:6379/1
  # Optional TTL in seconds (null = no expiration)
  ttl: null
  # Connection pool settings
  max_connections: 10

# Disk backend configuration
disk:
  path: ${data_dir}/tool_sources
  # Compression (none, gzip, lz4)
  compression: none
```

#### Factory Function (`lib/galaxy/tool_source_store/__init__.py`)

```python
def build_tool_source_store(config: "GalaxyAppConfiguration") -> ToolSourceStore:
    """Build a tool source store based on configuration."""
    backend = config.tool_source_store

    if backend == "database":
        from .database import DatabaseToolSourceStore
        return DatabaseToolSourceStore(config.model.session)

    elif backend == "redis":
        from .redis import RedisToolSourceStore
        redis_url = config.tool_source_redis_url
        if not redis_url:
            raise ConfigurationError("tool_source_redis_url required for redis backend")
        return RedisToolSourceStore(redis_url)

    elif backend == "disk":
        from .disk import DiskToolSourceStore
        return DiskToolSourceStore(config.tool_source_disk_path)

    else:
        raise ConfigurationError(f"Unknown tool source store backend: {backend}")
```

### 4. API Endpoints

Add new API endpoints for tool source management:

#### API Schema (`lib/galaxy/schema/tool_source.py`)

```python
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ToolSourceResponse(BaseModel):
    hash: str
    tool_source_class: str
    tool_id: Optional[str]
    tool_version: Optional[str]
    tool_dir: Optional[str]
    stored_at: Optional[datetime]
    # raw_source excluded by default for size

class ToolSourceDetailResponse(ToolSourceResponse):
    raw_source: str
    metadata: Optional[dict]

class ToolSourceListResponse(BaseModel):
    total_count: int
    items: List[ToolSourceResponse]

class ToolSourceStatsResponse(BaseModel):
    backend: str
    count: int
    size_bytes: Optional[int]
```

#### API Endpoints (`lib/galaxy/webapps/galaxy/api/tool_sources.py`)

```python
from fastapi import APIRouter, Depends, Query, HTTPException
from galaxy.managers.context import ProvidesAppContext
from galaxy.schema.tool_source import (
    ToolSourceResponse,
    ToolSourceDetailResponse,
    ToolSourceListResponse,
    ToolSourceStatsResponse,
)

router = APIRouter(tags=["tool_sources"])

@router.get(
    "/api/tool_sources",
    summary="List stored tool sources",
    response_model=ToolSourceListResponse,
)
def list_tool_sources(
    trans: ProvidesAppContext = Depends(get_trans),
    tool_id: Optional[str] = Query(None, description="Filter by tool ID"),
    tool_version: Optional[str] = Query(None, description="Filter by tool version"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
):
    """List all stored tool sources with optional filtering."""
    store = trans.app.tool_source_store
    # Implementation...

@router.get(
    "/api/tool_sources/{hash}",
    summary="Get a specific tool source by hash",
    response_model=ToolSourceDetailResponse,
)
def get_tool_source(
    hash: str,
    trans: ProvidesAppContext = Depends(get_trans),
    include_raw: bool = Query(False, description="Include raw source content"),
):
    """Retrieve a tool source by its content hash."""
    store = trans.app.tool_source_store
    source = store.get(hash)
    if not source:
        raise HTTPException(status_code=404, detail="Tool source not found")
    return source

@router.get(
    "/api/tool_sources/by_tool/{tool_id}",
    summary="Get tool sources by tool ID",
    response_model=List[ToolSourceResponse],
)
def get_tool_sources_by_id(
    tool_id: str,
    version: Optional[str] = Query(None),
    trans: ProvidesAppContext = Depends(get_trans),
):
    """Retrieve all tool sources for a given tool ID."""
    store = trans.app.tool_source_store
    return store.get_by_tool_id(tool_id, version)

@router.get(
    "/api/tool_sources/stats",
    summary="Get tool source storage statistics",
    response_model=ToolSourceStatsResponse,
)
def get_tool_source_stats(
    trans: ProvidesAppContext = Depends(get_trans),
):
    """Get statistics about the tool source store."""
    store = trans.app.tool_source_store
    stats = store.get_stats()
    stats["backend"] = trans.app.config.tool_source_store
    return stats
```

### 5. Population Script

Create a CLI script for incremental population of the tool source store.

#### Script (`scripts/tool_source/populate_store.py`)

```python
#!/usr/bin/env python
"""
Populate tool source store from Galaxy toolbox.

Usage:
    python scripts/tool_source/populate_store.py [options]

Options:
    --config FILE       Galaxy configuration file
    --dry-run           Show what would be stored without storing
    --incremental       Only store new/changed tools (default)
    --full              Force re-store all tools
    --tool-id PATTERN   Only process tools matching pattern
    --verbose           Enable verbose output
    --parallel N        Number of parallel workers (default: 4)
"""

import argparse
import hashlib
import logging
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Iterator, Optional

from galaxy.config import GalaxyAppConfiguration
from galaxy.tool_source_store import StoredToolSource, build_tool_source_store
from galaxy.tool_util.parser import get_tool_source
from galaxy.tools import ToolBox

log = logging.getLogger(__name__)

def compute_hash(content: str) -> str:
    """Compute SHA256 hash of content."""
    return hashlib.sha256(content.encode()).hexdigest()

def iter_tool_sources(toolbox: ToolBox, pattern: Optional[str] = None) -> Iterator[tuple]:
    """Iterate over all tools in the toolbox."""
    for tool_id, tool in toolbox._tools_by_id.items():
        if pattern and pattern not in tool_id:
            continue
        if hasattr(tool, 'tool_source') and tool.tool_source:
            yield tool_id, tool.version, tool.tool_source, tool.tool_dir

def populate_store(
    config_file: str,
    dry_run: bool = False,
    incremental: bool = True,
    pattern: Optional[str] = None,
    parallel: int = 4,
    verbose: bool = False,
):
    """Main population function."""
    log.info("Loading Galaxy configuration...")
    config = GalaxyAppConfiguration(__file__=config_file)

    log.info(f"Building tool source store (backend: {config.tool_source_store})...")
    store = build_tool_source_store(config)

    log.info("Loading toolbox...")
    # Initialize minimal app context for toolbox loading
    # ... (app initialization code)

    stats = {"processed": 0, "stored": 0, "skipped": 0, "errors": 0}

    def process_tool(args):
        tool_id, version, tool_source, tool_dir = args
        try:
            raw_source = tool_source.to_string()
            content_hash = compute_hash(raw_source)

            if incremental and store.exists(content_hash):
                return ("skipped", tool_id)

            stored = StoredToolSource(
                hash=content_hash,
                tool_source_class=tool_source.__class__.__name__,
                raw_source=raw_source,
                tool_id=tool_id,
                tool_version=version,
                tool_dir=tool_dir,
                stored_at=datetime.utcnow(),
            )

            if not dry_run:
                store.store(stored)

            return ("stored", tool_id)
        except Exception as e:
            log.error(f"Error processing {tool_id}: {e}")
            return ("error", tool_id, str(e))

    tools = list(iter_tool_sources(toolbox, pattern))
    log.info(f"Processing {len(tools)} tools...")

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {executor.submit(process_tool, t): t for t in tools}
        for future in as_completed(futures):
            result = future.result()
            status = result[0]
            stats[status if status != "error" else "errors"] += 1
            stats["processed"] += 1

            if verbose or status == "error":
                log.info(f"{status}: {result[1]}")

    log.info(f"Population complete: {stats}")
    return stats

def main():
    parser = argparse.ArgumentParser(description="Populate tool source store")
    parser.add_argument("--config", required=True, help="Galaxy config file")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--incremental", action="store_true", default=True)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--tool-id", help="Tool ID pattern filter")
    parser.add_argument("--parallel", type=int, default=4)
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    populate_store(
        config_file=args.config,
        dry_run=args.dry_run,
        incremental=not args.full,
        pattern=args.tool_id,
        parallel=args.parallel,
        verbose=args.verbose,
    )

if __name__ == "__main__":
    main()
```

### 6. Benchmarking

Create benchmarks for tool source deserialization performance.

#### Benchmark Suite (`lib/galaxy/tool_source_store/benchmarks.py`)

```python
"""
Benchmarks for tool source deserialization.

Run with: python -m galaxy.tool_source_store.benchmarks
"""

import hashlib
import json
import statistics
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, List, Optional

from galaxy.tool_util.parser import get_tool_source
from galaxy.tool_util.parser.factory import TOOL_SOURCE_FACTORIES

@dataclass
class BenchmarkResult:
    name: str
    iterations: int
    total_time_ms: float
    mean_time_ms: float
    median_time_ms: float
    min_time_ms: float
    max_time_ms: float
    std_dev_ms: float
    throughput_per_sec: float

def benchmark_function(
    name: str,
    func: Callable,
    iterations: int = 100,
    warmup: int = 10,
) -> BenchmarkResult:
    """Benchmark a function."""
    # Warmup
    for _ in range(warmup):
        func()

    # Actual benchmark
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        times.append((end - start) * 1000)  # Convert to ms

    total_time = sum(times)
    return BenchmarkResult(
        name=name,
        iterations=iterations,
        total_time_ms=total_time,
        mean_time_ms=statistics.mean(times),
        median_time_ms=statistics.median(times),
        min_time_ms=min(times),
        max_time_ms=max(times),
        std_dev_ms=statistics.stdev(times) if len(times) > 1 else 0,
        throughput_per_sec=iterations / (total_time / 1000),
    )

class ToolSourceBenchmarks:
    """Benchmark suite for tool source operations."""

    def __init__(self, tool_sources_dir: Optional[Path] = None):
        self.tool_sources_dir = tool_sources_dir or self._find_tool_sources()
        self._cached_sources: Dict[str, str] = {}

    def _find_tool_sources(self) -> Path:
        """Find Galaxy tools directory."""
        # Look for common locations
        candidates = [
            Path("tools"),
            Path("lib/galaxy/tools/bundled"),
            Path(__file__).parent.parent.parent / "tools" / "bundled",
        ]
        for p in candidates:
            if p.exists():
                return p
        raise RuntimeError("Could not find tools directory")

    def _load_sample_tools(self, count: int = 50) -> List[tuple]:
        """Load sample tool XML files."""
        tools = []
        for xml_file in self.tool_sources_dir.rglob("*.xml"):
            if len(tools) >= count:
                break
            try:
                with open(xml_file) as f:
                    content = f.read()
                if "<tool" in content:
                    tools.append((str(xml_file), content))
            except Exception:
                continue
        return tools

    def benchmark_xml_parsing(self, iterations: int = 100) -> BenchmarkResult:
        """Benchmark XML tool source parsing from string."""
        tools = self._load_sample_tools(10)
        if not tools:
            raise RuntimeError("No tools found for benchmarking")

        # Use a representative tool
        path, content = tools[0]
        factory = TOOL_SOURCE_FACTORIES["XmlToolSource"]

        return benchmark_function(
            name="xml_parsing",
            func=lambda: factory(content),
            iterations=iterations,
        )

    def benchmark_deserialization_from_db_format(
        self, iterations: int = 100
    ) -> BenchmarkResult:
        """Benchmark deserializing from database JSON format."""
        tools = self._load_sample_tools(10)
        path, content = tools[0]

        # Simulate DB storage format
        db_format = json.dumps({
            "raw": content,
            "tool_source_class": "XmlToolSource",
        })

        def deserialize():
            data = json.loads(db_format)
            factory = TOOL_SOURCE_FACTORIES[data["tool_source_class"]]
            return factory(data["raw"])

        return benchmark_function(
            name="db_deserialization",
            func=deserialize,
            iterations=iterations,
        )

    def benchmark_hash_computation(self, iterations: int = 1000) -> BenchmarkResult:
        """Benchmark content hash computation."""
        tools = self._load_sample_tools(10)
        path, content = tools[0]

        return benchmark_function(
            name="hash_computation",
            func=lambda: hashlib.sha256(content.encode()).hexdigest(),
            iterations=iterations,
        )

    def benchmark_store_get(
        self,
        store,
        iterations: int = 100,
    ) -> BenchmarkResult:
        """Benchmark getting tool source from store."""
        # First, ensure we have a stored tool
        tools = self._load_sample_tools(1)
        path, content = tools[0]
        content_hash = hashlib.sha256(content.encode()).hexdigest()

        # Store it
        from . import StoredToolSource
        stored = StoredToolSource(
            hash=content_hash,
            tool_source_class="XmlToolSource",
            raw_source=content,
            tool_id="benchmark_tool",
        )
        store.store(stored)

        return benchmark_function(
            name=f"store_get_{store.__class__.__name__}",
            func=lambda: store.get(content_hash),
            iterations=iterations,
        )

    def benchmark_full_pipeline(self, iterations: int = 50) -> BenchmarkResult:
        """Benchmark full pipeline: get from store -> deserialize -> create tool source."""
        tools = self._load_sample_tools(1)
        path, content = tools[0]

        # Simulate stored format
        stored = {
            "raw_source": content,
            "tool_source_class": "XmlToolSource",
        }
        stored_json = json.dumps(stored)

        def full_pipeline():
            # 1. "Get" from store (simulated with JSON parse)
            data = json.loads(stored_json)
            # 2. Deserialize
            factory = TOOL_SOURCE_FACTORIES[data["tool_source_class"]]
            tool_source = factory(data["raw_source"])
            # 3. Access some properties (simulating tool creation)
            _ = tool_source.parse_id()
            _ = tool_source.parse_version()
            return tool_source

        return benchmark_function(
            name="full_pipeline",
            func=full_pipeline,
            iterations=iterations,
        )

    def run_all(self, iterations: int = 100) -> List[BenchmarkResult]:
        """Run all benchmarks."""
        results = []

        print("Running tool source benchmarks...")
        print(f"Iterations per benchmark: {iterations}")
        print("-" * 60)

        benchmarks = [
            ("XML Parsing", lambda: self.benchmark_xml_parsing(iterations)),
            ("DB Deserialization", lambda: self.benchmark_deserialization_from_db_format(iterations)),
            ("Hash Computation", lambda: self.benchmark_hash_computation(iterations * 10)),
            ("Full Pipeline", lambda: self.benchmark_full_pipeline(iterations // 2)),
        ]

        for name, bench_func in benchmarks:
            try:
                result = bench_func()
                results.append(result)
                print(f"\n{result.name}:")
                print(f"  Mean:     {result.mean_time_ms:.3f} ms")
                print(f"  Median:   {result.median_time_ms:.3f} ms")
                print(f"  Min/Max:  {result.min_time_ms:.3f} / {result.max_time_ms:.3f} ms")
                print(f"  Std Dev:  {result.std_dev_ms:.3f} ms")
                print(f"  Throughput: {result.throughput_per_sec:.1f} ops/sec")
            except Exception as e:
                print(f"\n{name}: FAILED - {e}")

        return results

def main():
    """Run benchmarks from command line."""
    import argparse

    parser = argparse.ArgumentParser(description="Tool source benchmarks")
    parser.add_argument("--iterations", "-n", type=int, default=100)
    parser.add_argument("--tools-dir", type=Path, default=None)
    parser.add_argument("--output", "-o", type=Path, default=None)

    args = parser.parse_args()

    benchmarks = ToolSourceBenchmarks(args.tools_dir)
    results = benchmarks.run_all(args.iterations)

    if args.output:
        import json
        with open(args.output, 'w') as f:
            json.dump([r.__dict__ for r in results], f, indent=2)
        print(f"\nResults saved to {args.output}")

if __name__ == "__main__":
    main()
```

---

## Implementation Steps

### Phase 1: Core Infrastructure

1. **Create `lib/galaxy/tool_source_store/` package**
   - `__init__.py` with `ToolSourceStore` ABC and `StoredToolSource` dataclass
   - `models.py` with Pydantic models for serialization
   - Factory function `build_tool_source_store()`

2. **Implement Database Backend**
   - Create database migration to extend `tool_source` table
   - Implement `DatabaseToolSourceStore`
   - Integrate with existing PR #21278 code

3. **Add Configuration Options**
   - Update `config_schema.yml` with new options
   - Create sample configuration file
   - Update `GalaxyAppConfiguration` to handle new options

### Phase 2: Additional Backends

4. **Implement Redis Backend**
   - `RedisToolSourceStore` with indexing
   - Connection pooling and error handling
   - Optional TTL support

5. **Implement Disk Backend**
   - `DiskToolSourceStore` with sharded directory structure
   - Indexing via JSON files
   - Optional compression support

### Phase 3: API and Integration

6. **Create API Endpoints**
   - Add `lib/galaxy/webapps/galaxy/api/tool_sources.py`
   - Create request/response schemas
   - Integrate with FastAPI router

7. **Integrate with ToolBox/DatabaseToolBox**
   - Update PR #21278's `DatabaseToolBox` to use `ToolSourceStore`
   - Add tool source storage during tool loading
   - Implement cache lookup before database query

### Phase 4: Scripts and Tooling

8. **Create Population Script**
   - `scripts/tool_source/populate_store.py`
   - Support incremental and full modes
   - Parallel processing

9. **Create Benchmark Suite**
   - `lib/galaxy/tool_source_store/benchmarks.py`
   - Benchmarks for all operations
   - CI integration for regression testing

### Phase 5: Testing and Documentation

10. **Add Tests**
    - Unit tests for each backend
    - Integration tests for API endpoints
    - Performance regression tests

11. **Update Documentation**
    - Admin documentation for configuration
    - API documentation
    - Architecture documentation

---

## File Changes Summary

### New Files

```
lib/galaxy/tool_source_store/
    __init__.py
    database.py
    redis.py
    disk.py
    models.py
    benchmarks.py

lib/galaxy/webapps/galaxy/api/tool_sources.py
lib/galaxy/schema/tool_source.py

lib/galaxy/config/sample/tool_source_store_conf.sample.yml

scripts/tool_source/
    __init__.py
    populate_store.py

lib/galaxy/model/migrations/alembic/versions_gxy/
    xxxx_extend_tool_source_table.py

test/unit/tool_source_store/
    test_database.py
    test_redis.py
    test_disk.py
    test_api.py
    conftest.py
```

### Modified Files

```
lib/galaxy/config/__init__.py          # Add tool_source_store config handling
lib/galaxy/config/schemas/config_schema.yml  # Add new config options
lib/galaxy/model/__init__.py           # Extend ToolSource model
lib/galaxy/app.py                      # Initialize tool_source_store
lib/galaxy/webapps/galaxy/buildapp.py  # Register API routes
lib/galaxy/tools/__init__.py           # Integrate with ToolBox
```

---

## Considerations

### Performance

- **Caching**: Consider adding an in-memory LRU cache in front of the storage backend
- **Lazy Loading**: Only deserialize tool sources when needed
- **Compression**: For disk/Redis backends, consider compressing large tool sources

### Migration

- The database backend should be backward compatible with PR #21278
- Provide migration tools for moving between backends

### Security

- API endpoints should require admin permissions for write operations
- Validate tool source content before storage
- Consider signing/verification for integrity

### Monitoring

- Add metrics for store operations (get/put latency, hit rate)
- Log slow operations
- Alert on storage backend failures
