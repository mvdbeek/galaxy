# Plan: Generate Python API Client for Galaxy using openapi-python-client

## Overview

This plan outlines how to generate a typed Python API client for Galaxy using `openapi-python-client`, building on the existing OpenAPI schema generation infrastructure. The new client will be used to replace some API calls in the dataset populator test classes.

## Background

### Existing Infrastructure
- **OpenAPI Schema Generation**: Makefile target `build-api-schema` generates `_schema.yaml` using `scripts/dump_openapi_schema.py`
- **TypeScript Client**: Already generated using `openapi-typescript` via `update-client-api-schema` target
- **Test Populators**: Located in `lib/galaxy_test/base/populators.py` - use raw `requests` calls via abstract `_get`, `_post`, `_put`, `_delete` methods

### Populator Architecture
The populator classes use a mixin pattern:
- `BasePopulator`: Abstract base with HTTP verb methods
- `BaseDatasetPopulator`: Dataset operations (new_dataset, get_history_dataset_details, etc.)
- `DatasetPopulator`: Concrete implementation using `ApiTestInteractor`
- `GiDatasetPopulator`: Implementation using bioblend's `GalaxyClient`

---

## Implementation Steps

### Step 1: Add openapi-python-client as a Development Dependency

**File**: `pyproject.toml`

Add to the `dev` dependency group:
```toml
[dependency-groups]
dev = [
    ...
    "openapi-python-client>=0.23.0",
]
```

**Rationale**: This is a dev/build-time dependency for generating the client, not a runtime dependency.

---

### Step 2: Create Makefile Target for Python Client Generation

**File**: `Makefile`

Add new targets after the existing `update-client-api-schema`:

```makefile
# Python API client generation
PYTHON_CLIENT_DIR = lib/galaxy_test/api_client

build-python-api-client: build-api-schema
	$(IN_VENV) openapi-python-client generate \
		--path _schema.yaml \
		--output-path $(PYTHON_CLIENT_DIR) \
		--config openapi-python-client-config.yaml \
		--overwrite
	$(MAKE) remove-api-schema

update-python-api-client: build-python-api-client
	$(IN_VENV) ruff check --fix $(PYTHON_CLIENT_DIR) || true
	$(IN_VENV) ruff format $(PYTHON_CLIENT_DIR)
```

---

### Step 3: Create openapi-python-client Configuration

**File**: `openapi-python-client-config.yaml` (new file in repo root)

```yaml
project_name_override: galaxy-api-client
package_name_override: galaxy_api_client
use_path_prefix_for_tags: false
post_hooks:
  - ruff check --fix .
  - ruff format .
```

This configuration:
- Sets a sensible package name
- Disables path prefix for cleaner tag-based organization
- Runs ruff for linting/formatting after generation

---

### Step 4: Generate the Initial Client

Run the new Makefile target:
```bash
make update-python-api-client
```

This will generate a client in `lib/galaxy_test/api_client/` with:
- `galaxy_api_client/` - the actual client package
  - `api/` - endpoint methods organized by tags (datasets, histories, jobs, etc.)
  - `models/` - Pydantic models from OpenAPI schemas
  - `client.py` - HTTP client with authentication support
  - `types.py` - type definitions

---

### Step 5: Create a Client Factory for Populators

**File**: `lib/galaxy_test/base/api_client_factory.py` (new file)

```python
"""Factory for creating Galaxy API client instances for testing."""
from typing import Optional

from galaxy_api_client import Client, AuthenticatedClient


def create_api_client(
    base_url: str,
    api_key: Optional[str] = None,
    timeout: float = 60.0,
) -> Client | AuthenticatedClient:
    """Create a Galaxy API client for testing.

    Args:
        base_url: Galaxy server URL (e.g., "http://localhost:8080")
        api_key: Optional API key for authentication
        timeout: Request timeout in seconds

    Returns:
        An authenticated or anonymous client instance
    """
    if api_key:
        return AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            headers={"x-api-key": api_key},
            timeout=timeout,
        )
    return Client(base_url=base_url, timeout=timeout)
```

---

### Step 6: Replace API Calls in Dataset Populator

**File**: `lib/galaxy_test/base/populators.py`

Replace selected methods in `BaseDatasetPopulator` to use the new typed client. Start with a few simple methods:

#### 6.1: Add client property to BaseDatasetPopulator

```python
from galaxy_api_client import AuthenticatedClient
from galaxy_api_client.api.histories import (
    create_history_api_histories_post,
    show_history_api_histories_history_id_get,
)
from galaxy_api_client.api.datasets import (
    show_api_datasets_dataset_id_get,
)
from galaxy_api_client.models import (
    CreateHistoryPayload,
    HistoryDetailedModel,
    DatasetSourceType,
)

class BaseDatasetPopulator(BasePopulator):

    @property
    @abstractmethod
    def _api_client(self) -> AuthenticatedClient:
        """Return the typed API client for this populator."""
        ...
```

#### 6.2: Replace `new_history` method (line 1103)

**Before**:
```python
def new_history(self, name="API Test History", **kwds) -> str:
    create_history_response = self._post("histories", data=dict(name=name))
    assert "id" in create_history_response.json(), create_history_response.text
    return create_history_response.json()["id"]
```

**After**:
```python
def new_history(self, name="API Test History", **kwds) -> str:
    payload = CreateHistoryPayload(name=name)
    response = create_history_api_histories_post.sync(
        client=self._api_client,
        body=payload,
    )
    assert response is not None and response.id
    return response.id
```

#### 6.3: Replace `get_history_dataset_details_raw` method (line 1307)

**Before**:
```python
def get_history_dataset_details_raw(self, history_id: str, dataset_id: str, keys: Optional[str] = None) -> Response:
    data = None
    if keys:
        data = {"keys": keys}
    details_response = self._get(f"histories/{history_id}/contents/{dataset_id}", data=data)
    return details_response
```

**After**:
```python
def get_history_dataset_details(self, history_id: str, dataset_id: str, keys: Optional[str] = None) -> HDADetailed:
    response = show_api_histories_history_id_contents_history_content_id_get.sync(
        client=self._api_client,
        history_id=history_id,
        history_content_id=dataset_id,
        keys=keys,
    )
    if response is None:
        raise ValueError(f"Dataset {dataset_id} not found in history {history_id}")
    return response
```

#### 6.4: Replace `get_job_details` method (line 793)

**Before**:
```python
def get_job_details(self, job_id: str, full: bool = False) -> Response:
    return self._get(f"jobs/{job_id}", {"full": full})
```

**After**:
```python
def get_job_details(self, job_id: str, full: bool = False) -> ShowFullJobResponse:
    response = show_job_api_jobs_job_id_get.sync(
        client=self._api_client,
        job_id=job_id,
        full=full,
    )
    if response is None:
        raise ValueError(f"Job {job_id} not found")
    return response
```

---

### Step 7: Update Concrete Populator Implementations

**File**: `lib/galaxy_test/base/populators.py`

#### 7.1: Update `DatasetPopulator` class

```python
class DatasetPopulator(GalaxyInteractorHttpMixin, BaseDatasetPopulator):
    def __init__(self, galaxy_interactor: ApiTestInteractor) -> None:
        self.galaxy_interactor = galaxy_interactor
        self._client: Optional[AuthenticatedClient] = None

    @property
    def _api_client(self) -> AuthenticatedClient:
        if self._client is None:
            self._client = create_api_client(
                base_url=self.galaxy_interactor.api_url.rstrip('/api'),
                api_key=self.galaxy_interactor.api_key,
            )
        return self._client
```

#### 7.2: Update `GiDatasetPopulator` class

```python
class GiDatasetPopulator(GiHttpMixin, BaseDatasetPopulator):
    def __init__(self, gi: GalaxyClient):
        self._gi = gi
        self._client: Optional[AuthenticatedClient] = None

    @property
    def _api_client(self) -> AuthenticatedClient:
        if self._client is None:
            self._client = create_api_client(
                base_url=self._gi.base_url,
                api_key=self._gi.key,
            )
        return self._client
```

---

### Step 8: Add Tests for the New Client

**File**: `test/unit/test_api_client.py` (new file)

```python
"""Tests for the generated Galaxy API client."""
import pytest
from galaxy_api_client import Client
from galaxy_api_client.models import CreateHistoryPayload


def test_client_can_be_instantiated():
    """Verify the client can be created."""
    client = Client(base_url="http://localhost:8080")
    assert client is not None


def test_models_are_properly_typed():
    """Verify Pydantic models work correctly."""
    payload = CreateHistoryPayload(name="Test History")
    assert payload.name == "Test History"
```

---

## API Methods to Replace (Priority Order)

Start with these simple, frequently-used methods:

| Method | File Location | Complexity |
|--------|---------------|------------|
| `new_history` | populators.py:1103 | Low |
| `delete_history` | populators.py:850 | Low |
| `get_job_details` | populators.py:793 | Low |
| `get_history_dataset_details_raw` | populators.py:1307 | Medium |
| `get_history_contents` | populators.py:1427 | Medium |
| `cancel_job` | populators.py:847 | Low |

---

## Benefits of This Approach

1. **Type Safety**: Full type hints for API requests/responses
2. **Auto-completion**: IDE support for all API endpoints
3. **Validation**: Pydantic validates request/response data
4. **Maintainability**: Client regenerated automatically when API changes
5. **Consistency**: Single source of truth (OpenAPI schema)
6. **Gradual Migration**: Can replace methods incrementally while keeping old interface

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Schema incompatibilities | Run `make lint-api-schema` before generation |
| Breaking test changes | Keep `_raw` methods returning `Response` for backward compat |
| Large generated code | Add to `.gitignore` or commit only essential parts |
| httpx vs requests differences | Client uses httpx; may need adapter for some edge cases |

---

## Success Criteria

1. `make update-python-api-client` generates a working client
2. Unit tests pass for basic client operations
3. At least 3 populator methods successfully migrated
4. Existing API tests continue to pass
5. Type checking passes with mypy

---

## Timeline Estimate

This is a multi-phase effort:
- Phase 1: Infrastructure setup (Steps 1-4)
- Phase 2: Initial method replacements (Steps 5-7)
- Phase 3: Test coverage and validation (Step 8)
- Future: Gradual migration of remaining methods
