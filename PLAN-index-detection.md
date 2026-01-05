# Implementation Plan: Index File Detection and Import

## Issue Summary
**GitHub Issue**: #6181 - Import .bai files if they are present when importing BAM (instead of reindexing)
**Related Issue**: #18664 - Don't recreate index files when symlinking imported datasets

**Problem**: When importing large BAM files (100GB+), Galaxy regenerates index files even when valid `.bai`/`.csi` indexes already exist alongside the source files. This causes significant delays (10-15 minutes per sample) and wastes computational resources.

**Goal**: Implement explicit index file detection that:
1. Alerts users when indexes are detected nearby
2. Allows frontend to explicitly request index collection
3. Does NOT automatically assume well-known indexes should be imported (backend stays conservative)
4. Provides infrastructure to collect MetadataFile files during import

---

## Architecture Overview

```
┌─────────────────┐      ┌────────────────────┐      ┌─────────────────┐
│   Frontend UI   │──────▶│    Fetch API       │──────▶│  Data Fetch Job │
│  (index toggle) │      │ (secondary_files[])│      │ (index handling)│
└─────────────────┘      └────────────────────┘      └─────────────────┘
         │                        │                        │
         │                        │                        ▼
         │                        │               ┌─────────────────┐
         ▼                        ▼               │   set_meta()    │
┌─────────────────┐      ┌──────────────────┐     │ (skip if index  │
│ Index Detection │      │ Index Patterns   │     │  already exists)│
│    Service      │      │   Registry       │     └─────────────────┘
└─────────────────┘      └──────────────────┘
```

---

## Implementation Steps

### Phase 1: Backend Index Pattern Registry

#### Step 1.1: Create Index Pattern Registry
**File**: `lib/galaxy/datatypes/index_patterns.py` (new file)

Create a registry that maps datatypes to their known index file patterns:

```python
"""Registry of known index file patterns for datatypes."""
from dataclasses import dataclass
from typing import Optional

@dataclass
class IndexPattern:
    """Describes an index file pattern for a datatype."""
    primary_extension: str           # e.g., "bam"
    index_extension: str             # e.g., "bai"
    index_suffix: str                # e.g., ".bai" or ".bam.bai"
    metadata_key: str                # e.g., "bam_index"
    description: str                 # Human-readable description
    alternative_suffixes: tuple[str, ...] = ()  # e.g., (".bam.bai",) for BAM

# Registry of index patterns
INDEX_PATTERNS: dict[str, list[IndexPattern]] = {
    "bam": [
        IndexPattern(
            primary_extension="bam",
            index_extension="bai",
            index_suffix=".bai",
            metadata_key="bam_index",
            description="BAM Index (.bai)",
            alternative_suffixes=(".bam.bai",),
        ),
        IndexPattern(
            primary_extension="bam",
            index_extension="bam.csi",
            index_suffix=".csi",
            metadata_key="bam_csi_index",
            description="BAM CSI Index (.csi)",
            alternative_suffixes=(".bam.csi",),
        ),
    ],
    "vcf_bgzip": [
        IndexPattern(
            primary_extension="vcf_bgzip",
            index_extension="tbi",
            index_suffix=".tbi",
            metadata_key="tabix_index",
            description="Tabix Index (.tbi)",
            alternative_suffixes=(".vcf.gz.tbi",),
        ),
    ],
    "cram": [
        IndexPattern(
            primary_extension="cram",
            index_extension="crai",
            index_suffix=".crai",
            metadata_key="cram_index",
            description="CRAM Index (.crai)",
            alternative_suffixes=(".cram.crai",),
        ),
    ],
    # Additional patterns for bed_tabix, gff_tabix, etc.
}

def get_index_patterns(extension: str) -> list[IndexPattern]:
    """Get index patterns for a given file extension."""
    return INDEX_PATTERNS.get(extension, [])

def detect_index_files(primary_path: str, extension: str) -> list[dict]:
    """
    Detect existing index files for a primary file.

    Returns list of dicts with:
    - path: Full path to detected index
    - pattern: The IndexPattern that matched
    - exists: True if file exists
    """
    import os
    results = []
    patterns = get_index_patterns(extension)

    for pattern in patterns:
        # Try primary suffix (file.bam -> file.bam.bai or file.bai)
        for suffix in (pattern.index_suffix,) + pattern.alternative_suffixes:
            if suffix.startswith("."):
                # Suffix pattern: file.bam.bai
                index_path = primary_path + suffix
            else:
                # Extension replacement: file.bam -> file.bai
                base = os.path.splitext(primary_path)[0]
                index_path = base + "." + suffix

            if os.path.exists(index_path):
                results.append({
                    "path": index_path,
                    "pattern": pattern,
                    "exists": True,
                })
                break  # Found one for this pattern, move to next

    return results
```

#### Step 1.2: Add Index Detection to File Sources
**File**: `lib/galaxy/files/sources/__init__.py`

Add method to `BaseFilesSource` for detecting related index files:

```python
def detect_related_indexes(
    self,
    file_path: str,
    extension: Optional[str] = None
) -> list[dict]:
    """
    Detect index files that may exist alongside a primary file.

    Returns list of detected indexes with their paths and metadata keys.
    Only returns indexes that actually exist.
    """
    from galaxy.datatypes.index_patterns import detect_index_files

    # If extension not provided, try to infer from path
    if extension is None:
        extension = self._infer_extension(file_path)

    return detect_index_files(file_path, extension)
```

---

### Phase 2: API Schema Extensions

#### Step 2.1: Extend Fetch Data Schema
**File**: `lib/galaxy/schema/fetch_data.py`

Add new fields to support index file specification:

```python
class SecondaryFileSpec(FetchBaseModel):
    """Specification for a secondary file (e.g., index) to import alongside primary data."""
    src: Src  # Same source types as main data
    path: Optional[str] = None
    url: Optional[str] = None
    ftp_path: Optional[str] = None
    metadata_key: str = Field(..., description="Metadata key to store file (e.g., 'bam_index')")

class BaseDataElement(FetchBaseModel):
    # ... existing fields ...

    # NEW: Secondary files (indexes) to import instead of regenerating
    secondary_files: Optional[list[SecondaryFileSpec]] = Field(
        None,
        description="Pre-existing secondary files (e.g., indexes) to import. When provided, "
                    "Galaxy will use these instead of regenerating during metadata setting."
    )
```

#### Step 2.2: Add Index Detection API Endpoint
**File**: `lib/galaxy/webapps/galaxy/api/remote_files.py`

Add endpoint for detecting indexes:

```python
@router.get(
    "/api/remote_files/indexes",
    summary="Detect index files for a remote file",
)
def detect_indexes(
    self,
    trans: ProvidesUserContext = DependsOnTrans,
    target: str = Query(..., description="URI or path of primary file"),
    extension: Optional[str] = Query(None, description="File extension hint"),
) -> list[DetectedIndex]:
    """
    Detect existing index files that could be imported alongside a primary file.

    Returns information about detected indexes including their paths and
    whether they should be used.
    """
    # Implementation calls file source's detect_related_indexes
```

**New response model**:
```python
class DetectedIndex(Model):
    """Information about a detected index file."""
    path: str
    metadata_key: str
    description: str
    exists: bool
    suggested: bool = True  # Frontend can use this to pre-check the option
```

---

### Phase 3: Data Fetch Job Modifications

#### Step 3.1: Handle Index Files in Data Fetch
**File**: `lib/galaxy/tools/data_fetch.py`

Modify `_fetch_url` and `_fetch_path` functions to handle secondary files:

```python
def _handle_secondary_files(
    item: dict,
    primary_path: str,
    object_store: ObjectStore,
    trans,
) -> dict[str, str]:
    """
    Process secondary file specifications from the fetch request.

    Downloads/copies secondary files (indexes) and returns mapping of metadata_key -> file_path.
    """
    secondary_files_result = {}

    secondary_specs = item.get("secondary_files", [])
    for spec in secondary_specs:
        metadata_key = spec["metadata_key"]

        # Fetch the secondary file based on source type
        if spec.get("path"):
            secondary_path = _realize_path(spec["path"], ...)
        elif spec.get("url"):
            secondary_path = _fetch_url_to_file(spec["url"], ...)
        elif spec.get("ftp_path"):
            secondary_path = _fetch_ftp_to_file(spec["ftp_path"], ...)

        secondary_files_result[metadata_key] = secondary_path

    return secondary_files_result
```

#### Step 3.2: Pass Secondary Files to Upload Parameters
**File**: `lib/galaxy/tools/actions/upload_common.py`

Extend `create_paramfile()` to include secondary file paths:

```python
def create_paramfile(trans, uploaded_datasets, incoming_params):
    # ... existing code ...

    for uploaded_dataset in uploaded_datasets:
        # ... existing params ...

        # NEW: Include pre-fetched secondary files (indexes)
        if hasattr(uploaded_dataset, 'secondary_files') and uploaded_dataset.secondary_files:
            params['secondary_files'] = uploaded_dataset.secondary_files
```

---

### Phase 4: Metadata Setting Modifications

#### Step 4.1: Modify set_meta to Accept Pre-existing Indexes
**File**: `lib/galaxy/datatypes/binary.py`

Modify the `Bam.set_meta()` method to check for pre-imported indexes:

```python
def set_meta(
    self,
    dataset: DatasetProtocol,
    overwrite: bool = True,
    metadata_tmp_files_dir: Optional[str] = None,
    preloaded_indexes: Optional[dict[str, str]] = None,  # NEW parameter
    **kwd
) -> None:
    # These metadata values are not accessible by users, always overwrite
    super().set_meta(dataset=dataset, overwrite=overwrite, **kwd)

    index_flag = self.get_index_flag(dataset.get_file_name())
    if index_flag == "-b":
        spec_key = "bam_index"
    else:
        spec_key = "bam_csi_index"

    # NEW: Check if a pre-loaded index was provided
    if preloaded_indexes and spec_key in preloaded_indexes:
        preloaded_path = preloaded_indexes[spec_key]
        if os.path.exists(preloaded_path) and self._validate_index(
            dataset.get_file_name(), preloaded_path, index_flag
        ):
            # Use the pre-loaded index instead of regenerating
            index_file = dataset.metadata.spec[spec_key].param.new_file(
                dataset=dataset, metadata_tmp_files_dir=metadata_tmp_files_dir
            )
            shutil.copy(preloaded_path, index_file.get_file_name())
            if index_flag == "-b":
                dataset.metadata.bam_index = index_file
            else:
                dataset.metadata.bam_csi_index = index_file
            return  # Skip regeneration

    # Existing index generation code...
    index_file = dataset.metadata.spec[spec_key].param.new_file(
        dataset=dataset, metadata_tmp_files_dir=metadata_tmp_files_dir
    )
    # ... pysam.index() call ...

def _validate_index(
    self,
    bam_path: str,
    index_path: str,
    index_flag: str
) -> bool:
    """Validate that an index file is valid for the given BAM."""
    try:
        # Quick validation: try to open the BAM with the index
        with pysam.AlignmentFile(bam_path, "rb", index_filename=index_path) as f:
            # Try to fetch from first reference to validate index works
            if f.references:
                next(f.fetch(f.references[0], 0, 1), None)
        return True
    except Exception:
        return False
```

#### Step 4.2: Create Base Class for Index-Supporting Datatypes
**File**: `lib/galaxy/datatypes/data.py`

Add mixin/base functionality for datatypes that support pre-loaded indexes:

```python
class SupportsPreloadedIndexes:
    """Mixin for datatypes that can accept pre-loaded index files."""

    def set_meta_with_preloaded_indexes(
        self,
        dataset: DatasetProtocol,
        preloaded_indexes: Optional[dict[str, str]] = None,
        **kwd
    ) -> None:
        """
        Set metadata, optionally using pre-loaded index files.

        Subclasses should override to handle their specific index types.
        """
        # Default implementation just calls regular set_meta
        self.set_meta(dataset, **kwd)
```

---

### Phase 5: Job Execution Integration

#### Step 5.1: Pass Index Files Through Job Execution
**File**: `lib/galaxy/metadata/set_metadata.py`

Modify metadata setting to receive and use pre-loaded indexes:

```python
def set_metadata_portable(
    # ... existing params ...
    preloaded_indexes: Optional[dict[str, str]] = None,  # NEW
):
    # ... existing code ...

    # When calling set_meta, pass preloaded indexes if available
    if preloaded_indexes and hasattr(datatype, 'set_meta_with_preloaded_indexes'):
        datatype.set_meta_with_preloaded_indexes(
            dataset,
            preloaded_indexes=preloaded_indexes,
            **kwd
        )
    else:
        datatype.set_meta(dataset, **kwd)
```

#### Step 5.2: Store Index Files as MetadataFiles
**File**: `lib/galaxy/model/store/discover.py`

Ensure pre-loaded index files are properly stored as MetadataFile objects:

```python
def _handle_preloaded_index(
    dataset: HistoryDatasetAssociation,
    metadata_key: str,
    index_path: str,
    sa_session,
) -> MetadataFile:
    """
    Create a MetadataFile from a pre-loaded index file.
    """
    from galaxy.model import MetadataFile

    # Create MetadataFile object
    mf = MetadataFile(name=metadata_key, dataset=dataset)
    sa_session.add(mf)
    sa_session.flush()

    # Copy the index file to the MetadataFile location
    dest_path = mf.get_file_name()
    shutil.copy(index_path, dest_path)

    # Update dataset metadata
    setattr(dataset.metadata, metadata_key, mf)

    return mf
```

---

### Phase 6: Frontend Implementation

#### Step 6.1: Index Detection in Upload UI
**File**: `client/src/components/Upload/UploadBox.vue` (or equivalent)

Add index detection UI component:

```vue
<template>
  <!-- When file is selected, show detected indexes -->
  <div v-if="detectedIndexes.length > 0" class="detected-indexes-panel">
    <div class="alert alert-info">
      <strong>Index files detected!</strong>
      <p>The following index files were found and can be imported to skip regeneration:</p>
      <div v-for="index in detectedIndexes" :key="index.path" class="index-option">
        <input
          type="checkbox"
          v-model="selectedIndexes"
          :value="index"
          :id="'index-' + index.metadata_key"
        />
        <label :for="'index-' + index.metadata_key">
          {{ index.description }}: {{ index.path }}
        </label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    async detectIndexes(filePath, extension) {
      const response = await fetch(
        `/api/remote_files/indexes?target=${encodeURIComponent(filePath)}&extension=${extension}`
      );
      this.detectedIndexes = await response.json();
      // Pre-select suggested indexes
      this.selectedIndexes = this.detectedIndexes.filter(i => i.suggested);
    },

    buildUploadPayload() {
      // Include selected indexes in the upload payload
      const payload = {
        // ... existing fields ...
        secondary_files: this.selectedIndexes.map(idx => ({
          src: 'path',  // or appropriate source
          path: idx.path,
          metadata_key: idx.metadata_key,
        })),
      };
      return payload;
    }
  }
}
</script>
```

#### Step 6.2: Upload Payload Builder Modifications
**File**: `client/src/utils/upload-payload.js`

Extend payload builder to include index files:

```javascript
export function uploadPayload(items, historyId, composite = false) {
    const elements = items.map((item) => {
        const elem = {
            // ... existing fields ...
        };

        // NEW: Include secondary files (indexes) if user selected them
        if (item.secondaryFiles && item.secondaryFiles.length > 0) {
            elem.secondary_files = item.secondaryFiles.map(idx => ({
                src: idx.src || 'path',
                path: idx.path,
                url: idx.url,
                ftp_path: idx.ftpPath,
                metadata_key: idx.metadataKey,
            }));
        }

        return elem;
    });

    return { targets: [{ destination: { type: "hdas" }, elements }] };
}
```

#### Step 6.3: Remote Files Browser Enhancement
**File**: `client/src/components/FilesDialog/FilesDialog.vue` (or equivalent)

When browsing remote files, show index file indicators:

```vue
<template>
  <div class="file-row" v-for="file in files">
    <span>{{ file.name }}</span>
    <!-- Show badge if indexes detected -->
    <span v-if="file.hasIndexes" class="badge badge-info" title="Index files available">
      📑 +index
    </span>
  </div>
</template>
```

---

### Phase 7: Testing

#### Step 7.1: Unit Tests
**File**: `test/unit/datatypes/test_index_patterns.py` (new)

```python
def test_bam_index_detection():
    """Test that BAM index patterns are correctly detected."""
    from galaxy.datatypes.index_patterns import detect_index_files

    # Create temp BAM and BAI files
    with tempfile.TemporaryDirectory() as tmpdir:
        bam_path = os.path.join(tmpdir, "test.bam")
        bai_path = os.path.join(tmpdir, "test.bam.bai")

        Path(bam_path).touch()
        Path(bai_path).touch()

        detected = detect_index_files(bam_path, "bam")

        assert len(detected) == 1
        assert detected[0]["path"] == bai_path
        assert detected[0]["pattern"].metadata_key == "bam_index"

def test_no_index_when_missing():
    """Test that no index is detected when file doesn't exist."""
    # ...

def test_csi_index_detection():
    """Test CSI index detection for BAM files."""
    # ...
```

#### Step 7.2: Integration Tests
**File**: `test/integration/test_index_import.py` (new)

```python
class TestIndexImport(IntegrationTestCase):

    def test_bam_with_preloaded_index(self):
        """Test importing BAM with pre-existing BAI index."""
        # Create BAM and BAI in test directory
        # Import via API with secondary_files specified
        # Verify index was used (check timing, verify metadata)

    def test_index_validation_rejects_invalid(self):
        """Test that invalid index files are rejected."""
        # Create BAM and mismatched BAI
        # Attempt import with secondary_files
        # Verify Galaxy regenerates instead of using invalid index

    def test_frontend_index_detection_api(self):
        """Test the index detection API endpoint."""
        # Call /api/remote_files/indexes
        # Verify correct indexes are returned
```

#### Step 7.3: Selenium/E2E Tests
**File**: `test/selenium/test_upload_with_index.py` (new)

```python
def test_upload_shows_index_detection(self):
    """Test that upload UI shows detected indexes."""
    # Navigate to upload
    # Select BAM file with adjacent BAI
    # Verify index detection panel appears
    # Select index and upload
    # Verify dataset metadata shows index was imported
```

---

## File Change Summary

### New Files
| File | Purpose |
|------|---------|
| `lib/galaxy/datatypes/index_patterns.py` | Index pattern registry and detection |
| `test/unit/datatypes/test_index_patterns.py` | Unit tests for index detection |
| `test/integration/test_index_import.py` | Integration tests for index import |

### Modified Files
| File | Changes |
|------|---------|
| `lib/galaxy/schema/fetch_data.py` | Add `SecondaryFileSpec` and `secondary_files` field |
| `lib/galaxy/webapps/galaxy/api/remote_files.py` | Add index detection endpoint |
| `lib/galaxy/files/sources/__init__.py` | Add `detect_related_indexes` method |
| `lib/galaxy/tools/data_fetch.py` | Handle secondary files during fetch |
| `lib/galaxy/tools/actions/upload_common.py` | Pass secondary files through upload |
| `lib/galaxy/datatypes/binary.py` | Modify `Bam.set_meta()` to use pre-loaded indexes |
| `lib/galaxy/datatypes/tabular.py` | Modify `VcfGz.set_meta()` for tabix indexes |
| `lib/galaxy/datatypes/interval.py` | Modify tabix datatypes for pre-loaded indexes |
| `lib/galaxy/metadata/set_metadata.py` | Support preloaded indexes in metadata setting |
| `lib/galaxy/model/store/discover.py` | Handle MetadataFile creation from pre-loaded indexes |
| `client/src/components/Upload/*.vue` | Add index detection UI |
| `client/src/utils/upload-payload.js` | Include secondary files in payload |

---

## Design Decisions

### 1. Explicit Over Implicit
The backend will **never** automatically import secondary files. The frontend must explicitly request them via the `secondary_files` parameter. This ensures:
- Users are aware when indexes are being used
- No unexpected behavior from automatic detection
- Clear audit trail of what was imported

### 2. Validation Before Use
Pre-loaded indexes are validated before use:
- Basic file existence check
- Format validation (can pysam open it?)
- Compatibility check (does it work with the primary file?)

If validation fails, Galaxy falls back to regenerating the index with a warning.

### 3. User Notification
The frontend will clearly show:
- When indexes are detected (info banner)
- Which indexes are available (checkboxes)
- What action will be taken (import vs regenerate)

### 4. Backwards Compatibility
- Existing API calls without `secondary_files` work unchanged
- Existing datatypes without pre-loaded index support work unchanged
- No changes to existing database schema

---

## Performance Expectations

| Scenario | Current Time | With Index Import |
|----------|-------------|-------------------|
| 100GB BAM import | 10-15 min | < 1 min |
| 10GB VCF import | 2-3 min | < 30 sec |
| Symlinked import | Same as copy | Near-instant |

---

## Future Enhancements

1. **Auto-detection toggle**: Admin setting to enable automatic index detection for trusted sources
2. **Index validation levels**: Strict (full validation) vs Quick (existence only)
3. **Batch operations**: Apply index import to all files in a collection
4. **Index generation job**: Separate job for index generation to not block import
