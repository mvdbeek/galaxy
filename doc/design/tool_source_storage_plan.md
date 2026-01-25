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

## Scalable Tool Listing: Handling `/api/tools` Without Full Memory Load

### The Challenge

The `/api/tools` endpoint must return metadata for all tools (potentially thousands) quickly, but:
1. Loading and deserializing all tool sources consumes significant memory
2. Creating full `Tool` objects for each tool is expensive
3. The current `ToolBox` keeps all tools in memory (`_tools_by_id`)

### Solution: Separate Tool Index from Tool Sources

The key insight is that `/api/tools` needs **lightweight metadata**, not full tool sources. We separate:

| Layer | Purpose | Size | Storage |
|-------|---------|------|---------|
| **Tool Index** | API responses, search, panel | ~1-2 KB/tool | Always in memory or fast cache |
| **Tool Sources** | Tool execution, form rendering | ~10-100 KB/tool | On-demand from store |
| **Tool Objects** | Runtime execution | Variable | LRU cache with eviction |

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         API Layer                                │
│  /api/tools  /api/tools/{id}  /api/tools/{id}/build            │
└────────────────────┬───────────────────┬────────────────────────┘
                     │                   │
         ┌───────────▼───────────┐       │
         │     Tool Index        │       │
         │  (Always Available)   │       │
         │  - id, name, version  │       │
         │  - description        │       │
         │  - panel_section      │       │
         │  - labels, edam       │       │
         │  - source_hash ──────────────►│
         └───────────────────────┘       │
                                         │
                     ┌───────────────────▼────────────────────┐
                     │         Tool Source Store              │
                     │      (Database/Redis/Disk)             │
                     │  - Full XML/YAML source                │
                     │  - Loaded on-demand                    │
                     └───────────────────┬────────────────────┘
                                         │
                     ┌───────────────────▼────────────────────┐
                     │      Tool Object Cache (LRU)           │
                     │  - Parsed Tool objects                 │
                     │  - Evicted under memory pressure       │
                     │  - Rebuilt from source on cache miss   │
                     └────────────────────────────────────────┘
```

### 1. Tool Index Model

Create a lightweight index stored alongside tool sources:

```python
# lib/galaxy/tool_source_store/index.py

from dataclasses import dataclass, field
from typing import Optional, List, Dict
from datetime import datetime

@dataclass
class ToolIndexEntry:
    """Lightweight tool metadata for API responses and search."""
    # Identity
    id: str
    uuid: Optional[str] = None
    version: Optional[str] = None

    # Display
    name: str = ""
    description: str = ""

    # Classification
    panel_section_id: Optional[str] = None
    panel_section_name: Optional[str] = None
    labels: List[str] = field(default_factory=list)
    edam_operations: List[str] = field(default_factory=list)
    edam_topics: List[str] = field(default_factory=list)

    # Source reference (for on-demand loading)
    source_hash: str = ""
    source_class: str = "XmlToolSource"

    # Status
    hidden: bool = False
    disabled: bool = False

    # Timestamps
    indexed_at: Optional[datetime] = None

    def to_api_dict(self, detail: bool = False) -> Dict:
        """Convert to API response format."""
        result = {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "labels": self.labels,
            "panel_section_id": self.panel_section_id,
            "panel_section_name": self.panel_section_name,
            "hidden": self.hidden,
        }
        if detail:
            result.update({
                "uuid": self.uuid,
                "edam_operations": self.edam_operations,
                "edam_topics": self.edam_topics,
            })
        return result


@dataclass
class ToolIndex:
    """In-memory index of all tools for fast API access."""
    entries: Dict[str, ToolIndexEntry] = field(default_factory=dict)
    by_section: Dict[str, List[str]] = field(default_factory=dict)
    version: str = ""  # For cache invalidation
    built_at: Optional[datetime] = None

    def get(self, tool_id: str) -> Optional[ToolIndexEntry]:
        return self.entries.get(tool_id)

    def list_all(self,
                 section_id: Optional[str] = None,
                 include_hidden: bool = False) -> List[ToolIndexEntry]:
        """List tools with optional filtering."""
        if section_id:
            tool_ids = self.by_section.get(section_id, [])
            entries = [self.entries[tid] for tid in tool_ids if tid in self.entries]
        else:
            entries = list(self.entries.values())

        if not include_hidden:
            entries = [e for e in entries if not e.hidden]

        return entries

    def search(self, query: str, limit: int = 50) -> List[ToolIndexEntry]:
        """Fast text search across tool metadata."""
        query_lower = query.lower()
        results = []
        for entry in self.entries.values():
            if entry.hidden:
                continue
            # Score based on match location
            score = 0
            if query_lower in entry.id.lower():
                score += 100
            if query_lower in entry.name.lower():
                score += 50
            if query_lower in entry.description.lower():
                score += 10
            if any(query_lower in label.lower() for label in entry.labels):
                score += 25
            if score > 0:
                results.append((score, entry))

        results.sort(key=lambda x: -x[0])
        return [entry for _, entry in results[:limit]]

    def memory_size_estimate(self) -> int:
        """Estimate memory usage in bytes."""
        # Rough estimate: ~500 bytes per entry for typical tool
        return len(self.entries) * 500
```

### 2. Index Storage in Each Backend

Extend storage backends to handle the index:

```python
# Add to ToolSourceStore ABC

class ToolSourceStore(ABC):
    # ... existing methods ...

    @abstractmethod
    def store_index(self, index: ToolIndex) -> None:
        """Store the complete tool index."""
        pass

    @abstractmethod
    def load_index(self) -> Optional[ToolIndex]:
        """Load the tool index."""
        pass

    @abstractmethod
    def update_index_entry(self, entry: ToolIndexEntry) -> None:
        """Update a single index entry."""
        pass
```

**Database Backend Index Storage:**
```python
# New table: tool_index
class ToolIndexModel(Base):
    __tablename__ = "tool_index"

    tool_id: Mapped[str] = mapped_column(Unicode(255), primary_key=True)
    uuid: Mapped[Optional[str]] = mapped_column(Unicode(64), index=True)
    version: Mapped[Optional[str]] = mapped_column(Unicode(64))
    name: Mapped[str] = mapped_column(Unicode(255))
    description: Mapped[str] = mapped_column(Text)
    panel_section_id: Mapped[Optional[str]] = mapped_column(Unicode(255), index=True)
    panel_section_name: Mapped[Optional[str]] = mapped_column(Unicode(255))
    labels: Mapped[List[str]] = mapped_column(JSONType)
    edam_operations: Mapped[List[str]] = mapped_column(JSONType)
    edam_topics: Mapped[List[str]] = mapped_column(JSONType)
    source_hash: Mapped[str] = mapped_column(Unicode(64), ForeignKey("tool_source.hash"))
    source_class: Mapped[str] = mapped_column(Unicode(64))
    hidden: Mapped[bool] = mapped_column(default=False)
    disabled: Mapped[bool] = mapped_column(default=False)
    indexed_at: Mapped[datetime] = mapped_column(default=now)
```

**Redis Backend Index Storage:**
```python
# Keys:
# tool_index:entry:{tool_id} -> JSON of ToolIndexEntry
# tool_index:all -> Set of all tool_ids
# tool_index:section:{section_id} -> Set of tool_ids in section
# tool_index:meta -> JSON with version, built_at

class RedisToolSourceStore(ToolSourceStore):
    def load_index(self) -> Optional[ToolIndex]:
        pipe = self._redis.pipeline()

        # Get all tool IDs
        tool_ids = self._redis.smembers("tool_index:all")
        if not tool_ids:
            return None

        # Batch get all entries
        entries = {}
        for tool_id in tool_ids:
            data = self._redis.get(f"tool_index:entry:{tool_id}")
            if data:
                entry_dict = json.loads(data)
                entries[tool_id] = ToolIndexEntry(**entry_dict)

        # Get section mapping
        by_section = {}
        for key in self._redis.scan_iter("tool_index:section:*"):
            section_id = key.split(":")[-1]
            by_section[section_id] = list(self._redis.smembers(key))

        # Get metadata
        meta = json.loads(self._redis.get("tool_index:meta") or "{}")

        return ToolIndex(
            entries=entries,
            by_section=by_section,
            version=meta.get("version", ""),
            built_at=datetime.fromisoformat(meta["built_at"]) if "built_at" in meta else None,
        )
```

### 3. Lazy Tool Loading with LRU Cache

Replace the full in-memory toolbox with lazy loading:

```python
# lib/galaxy/tools/lazy_toolbox.py

from functools import lru_cache
from typing import Optional, Dict
from cachetools import LRUCache
import threading

class LazyToolBox:
    """
    ToolBox that loads tools on-demand from the tool source store.

    Keeps a lightweight index in memory for API responses,
    but only loads full Tool objects when needed.
    """

    def __init__(
        self,
        app,
        tool_source_store: ToolSourceStore,
        cache_size: int = 500,  # Number of Tool objects to cache
    ):
        self._app = app
        self._store = tool_source_store
        self._index: Optional[ToolIndex] = None
        self._tool_cache: LRUCache = LRUCache(maxsize=cache_size)
        self._cache_lock = threading.RLock()

        # Load index on startup
        self._load_index()

    def _load_index(self) -> None:
        """Load the tool index from store."""
        self._index = self._store.load_index()
        if self._index is None:
            # Build index from sources if not present
            self._rebuild_index()

    def _rebuild_index(self) -> None:
        """Rebuild index from all stored tool sources."""
        entries = {}
        by_section = {}

        for source_hash in self._store.list_all():
            stored = self._store.get(source_hash)
            if stored:
                entry = self._build_index_entry(stored)
                entries[entry.id] = entry
                if entry.panel_section_id:
                    by_section.setdefault(entry.panel_section_id, []).append(entry.id)

        self._index = ToolIndex(
            entries=entries,
            by_section=by_section,
            version=hashlib.md5(str(sorted(entries.keys())).encode()).hexdigest()[:8],
            built_at=datetime.utcnow(),
        )
        self._store.store_index(self._index)

    def _build_index_entry(self, stored: StoredToolSource) -> ToolIndexEntry:
        """Build index entry from stored source (without full Tool creation)."""
        # Use lightweight parsing - just extract metadata
        from galaxy.tool_util.parser import get_tool_source
        tool_source = get_tool_source(
            raw_tool_source=stored.raw_source,
            tool_source_class=stored.tool_source_class,
        )

        return ToolIndexEntry(
            id=tool_source.parse_id(),
            version=tool_source.parse_version(),
            name=tool_source.parse_name(),
            description=tool_source.parse_description() or "",
            labels=list(tool_source.parse_xrefs()),
            edam_operations=tool_source.parse_edam_operations(),
            edam_topics=tool_source.parse_edam_topics(),
            source_hash=stored.hash,
            source_class=stored.tool_source_class,
            hidden=tool_source.parse_hidden(),
        )

    # === API Methods (use index, no Tool loading) ===

    def list_tools(
        self,
        section_id: Optional[str] = None,
        include_hidden: bool = False,
    ) -> List[Dict]:
        """
        List all tools - used by /api/tools.
        Returns lightweight dicts from index, no Tool loading.
        """
        entries = self._index.list_all(section_id, include_hidden)
        return [entry.to_api_dict() for entry in entries]

    def search_tools(self, query: str, limit: int = 50) -> List[Dict]:
        """Search tools by text - fast, uses index only."""
        entries = self._index.search(query, limit)
        return [entry.to_api_dict() for entry in entries]

    def get_tool_info(self, tool_id: str) -> Optional[Dict]:
        """Get tool info - uses index, no Tool loading."""
        entry = self._index.get(tool_id)
        return entry.to_api_dict(detail=True) if entry else None

    # === Tool Loading Methods (load from store on-demand) ===

    def get_tool(self, tool_id: str, version: Optional[str] = None) -> Optional[Tool]:
        """
        Get a full Tool object - loads from store if not cached.
        Used for tool execution, form building, etc.
        """
        cache_key = f"{tool_id}:{version or 'latest'}"

        with self._cache_lock:
            if cache_key in self._tool_cache:
                return self._tool_cache[cache_key]

        # Get source hash from index
        entry = self._index.get(tool_id)
        if not entry:
            return None

        # Load source from store
        stored = self._store.get(entry.source_hash)
        if not stored:
            return None

        # Create Tool object
        tool = self._create_tool_from_source(stored)

        with self._cache_lock:
            self._tool_cache[cache_key] = tool

        return tool

    def _create_tool_from_source(self, stored: StoredToolSource) -> Tool:
        """Create a Tool object from stored source."""
        from galaxy.tool_util.parser import get_tool_source
        from galaxy.tools import create_tool_from_source

        tool_source = get_tool_source(
            raw_tool_source=stored.raw_source,
            tool_source_class=stored.tool_source_class,
        )

        return create_tool_from_source(
            self._app,
            tool_source,
            tool_dir=stored.tool_dir,
        )

    # === Cache Management ===

    def cache_stats(self) -> Dict:
        """Return cache statistics."""
        return {
            "tool_cache_size": len(self._tool_cache),
            "tool_cache_maxsize": self._tool_cache.maxsize,
            "index_size": len(self._index.entries) if self._index else 0,
            "index_memory_estimate": self._index.memory_size_estimate() if self._index else 0,
        }

    def clear_cache(self) -> None:
        """Clear the tool object cache."""
        with self._cache_lock:
            self._tool_cache.clear()

    def evict_tool(self, tool_id: str) -> None:
        """Evict a specific tool from cache."""
        with self._cache_lock:
            keys_to_remove = [k for k in self._tool_cache if k.startswith(f"{tool_id}:")]
            for key in keys_to_remove:
                del self._tool_cache[key]
```

### 4. Pre-computed API Responses

For extremely large installations, pre-compute and cache the `/api/tools` response:

```python
# lib/galaxy/tool_source_store/api_cache.py

import gzip
import json
from typing import Optional
from datetime import datetime, timedelta

class ToolAPICache:
    """
    Cache for pre-computed API responses.
    Stores gzip-compressed JSON for common API queries.
    """

    CACHE_KEYS = {
        "tools_list": "/api/tools",
        "tools_list_detailed": "/api/tools?detailed=true",
        "tool_panel": "/api/tools?in_panel=true",
    }

    def __init__(self, store: ToolSourceStore, ttl_seconds: int = 300):
        self._store = store
        self._ttl = timedelta(seconds=ttl_seconds)
        self._cache: Dict[str, tuple] = {}  # key -> (data, expires_at)

    def get_tools_list(self, detailed: bool = False) -> Optional[bytes]:
        """Get cached tools list response (gzip compressed)."""
        key = "tools_list_detailed" if detailed else "tools_list"
        return self._get_cached(key)

    def _get_cached(self, key: str) -> Optional[bytes]:
        if key in self._cache:
            data, expires_at = self._cache[key]
            if datetime.utcnow() < expires_at:
                return data
            del self._cache[key]
        return None

    def refresh(self, index: ToolIndex) -> None:
        """Refresh all cached API responses from index."""
        now = datetime.utcnow()
        expires_at = now + self._ttl

        # Basic tools list
        tools_list = [entry.to_api_dict() for entry in index.entries.values()
                      if not entry.hidden]
        self._cache["tools_list"] = (
            gzip.compress(json.dumps(tools_list).encode()),
            expires_at
        )

        # Detailed tools list
        tools_detailed = [entry.to_api_dict(detail=True) for entry in index.entries.values()
                          if not entry.hidden]
        self._cache["tools_list_detailed"] = (
            gzip.compress(json.dumps(tools_detailed).encode()),
            expires_at
        )

    def invalidate(self) -> None:
        """Invalidate all cached responses."""
        self._cache.clear()
```

### 5. Updated API Endpoints

Modify `/api/tools` to use the index:

```python
# lib/galaxy/webapps/galaxy/api/tools.py

from fastapi import APIRouter, Response
from fastapi.responses import StreamingResponse
import gzip

@router.get("/api/tools")
def list_tools(
    trans: ProvidesAppContext = Depends(get_trans),
    q: Optional[str] = Query(None, description="Search query"),
    section_id: Optional[str] = Query(None),
    in_panel: bool = Query(False),
    detailed: bool = Query(False),
):
    """
    List available tools.

    Uses lightweight index for fast responses without loading full tools.
    """
    toolbox = trans.app.lazy_toolbox  # or regular toolbox with index

    # Try pre-computed cache first for common queries
    if not q and not section_id and not in_panel:
        api_cache = trans.app.tool_api_cache
        cached = api_cache.get_tools_list(detailed=detailed)
        if cached:
            return Response(
                content=cached,
                media_type="application/json",
                headers={"Content-Encoding": "gzip"}
            )

    # Search query
    if q:
        tools = toolbox.search_tools(q)
    else:
        tools = toolbox.list_tools(section_id=section_id)

    return tools

@router.get("/api/tools/{tool_id}")
def get_tool(
    tool_id: str,
    trans: ProvidesAppContext = Depends(get_trans),
    version: Optional[str] = Query(None),
    io_details: bool = Query(False),
):
    """
    Get tool details.

    Basic info from index, full tool loaded only if io_details=True.
    """
    toolbox = trans.app.lazy_toolbox

    if io_details:
        # Need full Tool object for inputs/outputs
        tool = toolbox.get_tool(tool_id, version)
        if not tool:
            raise HTTPException(404, "Tool not found")
        return tool.to_dict()
    else:
        # Just use index
        info = toolbox.get_tool_info(tool_id)
        if not info:
            raise HTTPException(404, "Tool not found")
        return info

@router.get("/api/tools/{tool_id}/build")
def build_tool(
    tool_id: str,
    trans: ProvidesAppContext = Depends(get_trans),
    version: Optional[str] = Query(None),
):
    """
    Build tool form - requires full Tool object.
    """
    toolbox = trans.app.lazy_toolbox
    tool = toolbox.get_tool(tool_id, version)
    if not tool:
        raise HTTPException(404, "Tool not found")

    # Build form using full tool
    return tool.to_json(trans)
```

### 6. Memory Budget Configuration

Add configuration for memory management:

```yaml
# galaxy.yml

# Tool loading configuration
tool_cache_size: 500        # Max Tool objects in LRU cache
tool_index_in_memory: true  # Keep tool index in memory (recommended)
tool_api_cache_ttl: 300     # Seconds to cache /api/tools response

# Memory pressure handling
tool_cache_evict_on_memory_pressure: true
tool_cache_memory_limit_mb: 512  # Evict if cache exceeds this
```

### 7. Benchmarks for Index Operations

Add index-specific benchmarks:

```python
# Add to benchmarks.py

def benchmark_index_search(self, iterations: int = 100) -> BenchmarkResult:
    """Benchmark searching the tool index."""
    # Build a sample index
    index = ToolIndex()
    for i in range(1000):
        index.entries[f"tool_{i}"] = ToolIndexEntry(
            id=f"tool_{i}",
            name=f"Tool Number {i}",
            description=f"A tool that does thing {i}",
            labels=["genomics", "ngs"] if i % 2 == 0 else ["proteomics"],
        )

    queries = ["genomics", "tool_5", "number", "does"]

    def search():
        for q in queries:
            index.search(q, limit=50)

    return benchmark_function("index_search", search, iterations)

def benchmark_api_response_generation(self, iterations: int = 100) -> BenchmarkResult:
    """Benchmark generating /api/tools response from index."""
    index = ToolIndex()
    for i in range(1000):
        index.entries[f"tool_{i}"] = ToolIndexEntry(
            id=f"tool_{i}",
            name=f"Tool {i}",
            description=f"Description {i}",
        )

    def generate_response():
        return [e.to_api_dict() for e in index.entries.values()]

    return benchmark_function("api_response_generation", generate_response, iterations)
```

### Summary: Memory vs. Performance Trade-offs

| Configuration | Memory Usage | `/api/tools` Latency | Tool Execution |
|---------------|--------------|----------------------|----------------|
| Full ToolBox (current) | High (~100MB+ for 1000 tools) | Fast | Fast |
| Index + LRU(500) | Medium (~10MB index + ~50MB cache) | Fast | Fast for cached, ~50ms for uncached |
| Index + LRU(100) | Low (~10MB index + ~10MB cache) | Fast | Fast for cached, ~50ms for uncached |
| Index + No Cache | Very Low (~10MB) | Fast | ~50ms per tool load |

**Recommendation**: Use Index + LRU cache with size tuned to available memory. For most installations, 500 cached tools covers the "hot" tools used in 95%+ of jobs.

---

## Implementation Steps

### Phase 1: Core Infrastructure

1. **Create `lib/galaxy/tool_source_store/` package**
   - `__init__.py` with `ToolSourceStore` ABC and `StoredToolSource` dataclass
   - `models.py` with Pydantic models for serialization
   - Factory function `build_tool_source_store()`

2. **Implement Database Backend**
   - Create database migration to extend `tool_source` table
   - Create `tool_index` table for lightweight metadata
   - Implement `DatabaseToolSourceStore`
   - Integrate with existing PR #21278 code

3. **Add Configuration Options**
   - Update `config_schema.yml` with new options
   - Create sample configuration file
   - Update `GalaxyAppConfiguration` to handle new options

### Phase 2: Tool Index and Lazy Loading

4. **Implement Tool Index**
   - `ToolIndexEntry` dataclass with lightweight metadata
   - `ToolIndex` class with search and lookup methods
   - Index storage/loading in all backends

5. **Implement LazyToolBox**
   - LRU cache for Tool objects
   - On-demand loading from store
   - Index-based API responses
   - Memory pressure handling

6. **Pre-computed API Cache**
   - Gzip-compressed response caching
   - TTL-based invalidation
   - Automatic refresh on index changes

### Phase 3: Additional Backends

7. **Implement Redis Backend**
   - `RedisToolSourceStore` with source and index storage
   - Connection pooling and error handling
   - Optional TTL support

8. **Implement Disk Backend**
   - `DiskToolSourceStore` with sharded directory structure
   - Index storage as JSON files
   - Optional compression support

### Phase 4: API and Integration

9. **Create API Endpoints**
   - Add `lib/galaxy/webapps/galaxy/api/tool_sources.py`
   - Update `/api/tools` to use index
   - Create request/response schemas
   - Integrate with FastAPI router

10. **Integrate with ToolBox/DatabaseToolBox**
    - Update PR #21278's `DatabaseToolBox` to use `ToolSourceStore`
    - Add tool source storage during tool loading
    - Implement cache lookup before database query

### Phase 5: Scripts and Tooling

11. **Create Population Script**
    - `scripts/tool_source/populate_store.py`
    - Support incremental and full modes
    - Parallel processing
    - Index building

12. **Create Benchmark Suite**
    - `lib/galaxy/tool_source_store/benchmarks.py`
    - Benchmarks for all operations including index search
    - CI integration for regression testing

### Phase 6: Testing and Documentation

13. **Add Tests**
    - Unit tests for each backend
    - Unit tests for ToolIndex and LazyToolBox
    - Integration tests for API endpoints
    - Performance regression tests
    - Memory usage tests

14. **Update Documentation**
    - Admin documentation for configuration
    - API documentation
    - Architecture documentation
    - Migration guide from full ToolBox

---

## File Changes Summary

### New Files

```
lib/galaxy/tool_source_store/
    __init__.py              # ToolSourceStore ABC, StoredToolSource, factory
    database.py              # DatabaseToolSourceStore
    redis.py                 # RedisToolSourceStore
    disk.py                  # DiskToolSourceStore
    models.py                # Pydantic models for serialization
    index.py                 # ToolIndex, ToolIndexEntry
    api_cache.py             # ToolAPICache for pre-computed responses
    benchmarks.py            # Performance benchmarks

lib/galaxy/tools/
    lazy_toolbox.py          # LazyToolBox with LRU cache

lib/galaxy/webapps/galaxy/api/tool_sources.py
lib/galaxy/schema/tool_source.py

lib/galaxy/config/sample/tool_source_store_conf.sample.yml

scripts/tool_source/
    __init__.py
    populate_store.py        # Incremental population script
    build_index.py           # Index building script

lib/galaxy/model/migrations/alembic/versions_gxy/
    xxxx_extend_tool_source_table.py
    xxxx_add_tool_index_table.py

test/unit/tool_source_store/
    test_database.py
    test_redis.py
    test_disk.py
    test_index.py
    test_lazy_toolbox.py
    test_api.py
    test_api_cache.py
    conftest.py
```

### Modified Files

```
lib/galaxy/config/__init__.py          # Add tool_source_store config handling
lib/galaxy/config/schemas/config_schema.yml  # Add new config options
lib/galaxy/model/__init__.py           # Extend ToolSource model, add ToolIndex model
lib/galaxy/app.py                      # Initialize tool_source_store, lazy_toolbox, api_cache
lib/galaxy/webapps/galaxy/buildapp.py  # Register API routes
lib/galaxy/webapps/galaxy/api/tools.py # Update to use index for /api/tools
lib/galaxy/tools/__init__.py           # Integrate with ToolBox, add ToolSource storage
```

---

## Considerations

### Performance

- **Index in Memory**: Keep the lightweight `ToolIndex` in memory for fast `/api/tools` responses
- **LRU Caching**: Use bounded LRU cache for `Tool` objects to limit memory usage
- **Lazy Loading**: Only deserialize tool sources when needed for execution
- **Pre-computed Responses**: Cache gzip-compressed API responses for common queries
- **Compression**: For disk/Redis backends, consider compressing large tool sources

### Memory Management

- **Index Size**: ~500 bytes per tool, 1000 tools ≈ 500 KB
- **Tool Cache**: Size based on available memory; default 500 tools ≈ 50 MB
- **API Cache**: Gzip-compressed responses, typically < 1 MB total
- **Eviction**: Automatic eviction under memory pressure

### Migration

- The database backend should be backward compatible with PR #21278
- Provide migration tools for moving between backends
- Support gradual migration: run old ToolBox alongside new LazyToolBox during transition
- Index can be rebuilt from sources at any time

### Security

- API endpoints should require admin permissions for write operations
- Validate tool source content before storage
- Consider signing/verification for integrity
- Tool source hashes provide content integrity verification

### Monitoring

- Add metrics for store operations (get/put latency, hit rate)
- Track cache hit/miss rates for LRU cache
- Monitor index size and memory usage
- Log slow operations
- Alert on storage backend failures

### Backward Compatibility

- Full ToolBox remains available for installations that prefer it
- LazyToolBox is opt-in via configuration
- Existing tool configuration files continue to work
- Gradual adoption: start with new installations, migrate existing ones later
