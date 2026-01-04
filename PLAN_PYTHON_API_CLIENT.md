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

### Current Operation ID Problem
FastAPI auto-generates verbose operation IDs when not explicitly set, resulting in names like:
- `create_api_histories_post` instead of `histories__create`
- `show_api_datasets_dataset_id_get` instead of `datasets__show`

These verbose names produce ugly generated method names in Python clients.

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

### Step 2: Improve Operation ID Generation in FastAPI

**File**: `lib/galaxy/webapps/galaxy/fast_app.py`

Add a custom `generate_unique_id_function` to produce clean, consistent operation IDs:

```python
from fastapi.routing import APIRoute


def generate_operation_id(route: APIRoute) -> str:
    """Generate clean operation IDs for OpenAPI schema.

    Produces IDs in the format: {tag}__{function_name}
    Examples:
        - histories__create (instead of create_api_histories_post)
        - datasets__show (instead of show_api_datasets_dataset_id_get)
        - jobs__index (instead of index_api_jobs_get)
    """
    # Use the first tag, or 'default' if no tags
    tag = route.tags[0] if route.tags else "default"
    # Normalize tag: lowercase, replace spaces with underscores
    tag = tag.lower().replace(" ", "_")
    # Use the endpoint function name
    operation = route.endpoint.__name__
    return f"{tag}__{operation}"


def get_fastapi_instance(root_path="") -> FastAPI:
    return FastAPI(
        title="Galaxy API",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_tags=api_tags_metadata,
        license_info={"name": "MIT", "url": "https://github.com/galaxyproject/galaxy/blob/dev/LICENSE.txt"},
        root_path=root_path,
        generate_unique_id_function=generate_operation_id,  # <-- Add this
    )
```

**Benefits**:
- All endpoints get consistent, clean operation IDs automatically
- Existing explicit `operation_id` values in route decorators take precedence
- Benefits both Python and TypeScript clients
- No need to modify hundreds of route decorators

**Generated Method Names Comparison**:

| Before | After |
|--------|-------|
| `create_api_histories_post` | `histories__create` |
| `index_api_histories_get` | `histories__index` |
| `show_api_histories_history_id_get` | `histories__show` |
| `delete_api_histories_history_id_delete` | `histories__delete` |
| `show_api_jobs_job_id_get` | `jobs__show` |
| `index_api_datasets_get` | `datasets__index` |

---

### Step 3: Create Makefile Target for Python Client Generation

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

### Step 4: Create openapi-python-client Configuration

**File**: `openapi-python-client-config.yaml` (new file in repo root)

```yaml
project_name_override: galaxy-api-client
package_name_override: galaxy_api_client
use_path_prefixes_for_title_model_names: false
post_hooks:
  - ruff check --fix .
  - ruff format .
```

This configuration:
- Sets a sensible package name
- Avoids verbose class names from path prefixes
- Runs ruff for linting/formatting after generation

**Tag-Based Organization**: The generator automatically organizes endpoints by their OpenAPI tags. Galaxy's routers already define tags consistently:

```python
# lib/galaxy/webapps/galaxy/api/histories.py
router = Router(tags=["histories"])

# lib/galaxy/webapps/galaxy/api/datasets.py
router = Router(tags=["datasets"])

# lib/galaxy/webapps/galaxy/api/jobs.py
router = Router(tags=["jobs"])
```

This produces a clean, intuitive API structure organized by resource type.

---

### Step 5: Generate the Initial Client

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

**Generated API Structure** (organized by router tags):
```
galaxy_api_client/
├── api/
│   ├── histories/              # From Router(tags=["histories"])
│   │   ├── __init__.py
│   │   ├── create.py           # histories__create  -> POST /api/histories
│   │   ├── index.py            # histories__index   -> GET /api/histories
│   │   ├── show.py             # histories__show    -> GET /api/histories/{id}
│   │   └── delete.py           # histories__delete  -> DELETE /api/histories/{id}
│   ├── datasets/               # From Router(tags=["datasets"])
│   │   ├── __init__.py
│   │   ├── index.py            # datasets__index    -> GET /api/datasets
│   │   └── show.py             # datasets__show     -> GET /api/datasets/{id}
│   ├── jobs/                   # From Router(tags=["jobs"])
│   │   ├── __init__.py
│   │   ├── index.py            # jobs__index        -> GET /api/jobs
│   │   └── show.py             # jobs__show         -> GET /api/jobs/{id}
│   ├── workflows/              # From Router(tags=["workflows"])
│   ├── tools/                  # From Router(tags=["tools"])
│   ├── dataset_collections/    # From Router(tags=["dataset collections"])
│   └── ...                     # Other tags
├── models/
│   ├── __init__.py
│   ├── create_history_payload.py
│   ├── history_detailed_model.py
│   └── ...                     # Pydantic models from schemas
└── client.py                   # Client and AuthenticatedClient classes
```

**Usage Example** (tag-based imports):
```python
from galaxy_api_client import AuthenticatedClient
from galaxy_api_client.api.histories import create, index, show, delete
from galaxy_api_client.api.jobs import show as show_job
from galaxy_api_client.models import CreateHistoryPayload

client = AuthenticatedClient(base_url="http://localhost:8080", headers={"x-api-key": "..."})

# Create a history
payload = CreateHistoryPayload(name="My History")
history = create.sync(client=client, body=payload)

# List all histories
histories = index.sync(client=client)

# Get job details
job = show_job.sync(client=client, job_id="abc123")
```

---

### Step 6: Create a Client Factory for Populators

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

### Step 7: Replace API Calls in Dataset Populator

**File**: `lib/galaxy_test/base/populators.py`

Replace selected methods in `BaseDatasetPopulator` to use the new typed client. Start with a few simple methods:

#### 7.1: Add client property to BaseDatasetPopulator

```python
from galaxy_api_client import AuthenticatedClient
from galaxy_api_client.api.histories import create, show, delete
from galaxy_api_client.api.jobs import show as show_job
from galaxy_api_client.models import CreateHistoryPayload

class BaseDatasetPopulator(BasePopulator):

    @property
    @abstractmethod
    def _api_client(self) -> AuthenticatedClient:
        """Return the typed API client for this populator."""
        ...
```

#### 7.2: Replace `new_history` method (line 1103)

**Before**:
```python
def new_history(self, name="API Test History", **kwds) -> str:
    create_history_response = self._post("histories", data=dict(name=name))
    assert "id" in create_history_response.json(), create_history_response.text
    return create_history_response.json()["id"]
```

**After** (with clean method names):
```python
def new_history(self, name="API Test History", **kwds) -> str:
    from galaxy_api_client.api.histories import create

    payload = CreateHistoryPayload(name=name)
    response = create.sync(client=self._api_client, body=payload)
    assert response is not None and response.id
    return response.id
```

#### 7.3: Replace `get_job_details` method (line 793)

**Before**:
```python
def get_job_details(self, job_id: str, full: bool = False) -> Response:
    return self._get(f"jobs/{job_id}", {"full": full})
```

**After**:
```python
def get_job_details(self, job_id: str, full: bool = False) -> ShowFullJobResponse:
    from galaxy_api_client.api.jobs import show

    response = show.sync(client=self._api_client, job_id=job_id, full=full)
    if response is None:
        raise ValueError(f"Job {job_id} not found")
    return response
```

#### 7.4: Replace `delete_history` method (line 850)

**Before**:
```python
def delete_history(self, history_id: str) -> None:
    delete_response = self._delete(f"histories/{history_id}")
    delete_response.raise_for_status()
```

**After**:
```python
def delete_history(self, history_id: str) -> None:
    from galaxy_api_client.api.histories import delete

    response = delete.sync(client=self._api_client, history_id=history_id)
    # Response validation is handled by the typed client
```

---

### Step 8: Update Concrete Populator Implementations

**File**: `lib/galaxy_test/base/populators.py`

#### 8.1: Update `DatasetPopulator` class

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

#### 8.2: Update `GiDatasetPopulator` class

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

### Step 9: Add Tests for the New Client

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
7. **Clean Method Names**: `histories.create()` instead of `histories.create_api_histories_post()`

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Schema incompatibilities | Run `make lint-api-schema` before generation |
| Breaking test changes | Keep `_raw` methods returning `Response` for backward compat |
| Large generated code | Add to `.gitignore` or commit only essential parts |
| httpx vs requests differences | Client uses httpx; may need adapter for some edge cases |
| Operation ID conflicts | Explicit `operation_id` in decorators takes precedence |

---

## Success Criteria

1. `make update-python-api-client` generates a working client
2. Generated method names are clean (e.g., `histories.create`, not `histories.create_api_histories_post`)
3. Unit tests pass for basic client operations
4. At least 3 populator methods successfully migrated
5. Existing API tests continue to pass
6. Type checking passes with mypy

---

## Implementation Phases

- **Phase 1**: Infrastructure setup (Steps 1-5)
  - Add dependency
  - Implement `generate_operation_id` function
  - Add Makefile targets
  - Generate initial client

- **Phase 2**: Initial method replacements (Steps 6-8)
  - Create client factory
  - Replace 3-5 populator methods
  - Update concrete implementations

- **Phase 3**: Test coverage and validation (Step 9)
  - Add unit tests
  - Run full test suite
  - Future: Gradual migration of remaining methods
