# pyopenapi-gen 5.0.3 Bug Reproducer: Missing Module References

## Summary

pyopenapi-gen 5.0.3 generates imports for modules that don't exist when processing OpenAPI schemas with:
1. Recursive type definitions (e.g., `SectionModel-Input` containing `parameters` that include `SectionModel-Input`)
2. `anyOf`/`oneOf` unions referencing recursive types
3. Schema names with `-Input` or `-Output` suffixes

## Bug Description

When the generator encounters a type that appears multiple times (due to recursion or multiple references), it creates numbered variants of the dataclass (e.g., `SectionModelInput2`, `SectionModelInput3`).

**The bug**: When generating `TypeAlias` union types that reference these schemas, the generator creates imports to the **unnumbered** version (e.g., `SectionModelInput`) which is never generated.

### Example from generated code

**section_model_input_parameters_item.py** (buggy):
```python
from .conditional_model_input import ConditionalModelInput
from .section_model_input import SectionModelInput  # BUG: This file doesn't exist!
from .text_model import TextModel

# Duplicate imports with numbered variant:
from .conditional_model_input import ConditionalModelInput
from .section_model_input_2 import SectionModelInput2  # This file exists
from .text_model import TextModel

# Uses the non-existent SectionModelInput:
SectionModelInputParametersItem: TypeAlias = Union[TextModel, ConditionalModelInput, SectionModelInput]
```

The generator creates:
- `section_model_input_2.py` (EXISTS - contains `SectionModelInput2`)
- `section_model_input_3.py` (EXISTS - contains `SectionModelInput3`)
- `section_model_input.py` (MISSING - never generated)

## Reproduction Steps

### Prerequisites
- Python 3.12+
- pyopenapi-gen 5.0.3

```bash
pip install pyopenapi-gen>=5.0.3
```

### Minimal Reproducer

1. Use the schema file: `discriminated_union_schema.yaml`

2. Generate the client:
```bash
python -m pyopenapi_gen discriminated_union_schema.yaml \
    --project-root output \
    --output-package test_client \
    --force \
    --no-postprocess
```

3. Check for missing modules:
```bash
cd output/test_client/models

# Extract all imported module names
grep -h "^from \." *.py | sed 's/from \.\([^ ]*\) import.*/\1/' | sort -u > /tmp/imported.txt

# List all existing modules
ls *.py | sed 's/\.py$//' | sort -u > /tmp/existing.txt

# Find missing modules
comm -23 /tmp/imported.txt /tmp/existing.txt
```

**Expected output showing missing modules:**
```
conditional_model_input_2
section_model_input
```

4. Verify the import error:
```bash
cd output
python -c "from test_client.models.section_model_input_parameters_item import SectionModelInputParametersItem"
```

**Error:**
```
ModuleNotFoundError: No module named 'test_client.models.section_model_input'
```

## Root Cause Analysis

The bug appears to be in the type deduplication/naming logic:

1. When `SectionModel-Input` is first encountered, the generator plans to create `section_model_input.py`
2. When `SectionModel-Input` is encountered again (in recursive references), the generator creates numbered variants `section_model_input_2.py`, `section_model_input_3.py`
3. When generating TypeAlias files that reference these types, the generator uses the original unnumbered name `SectionModelInput` instead of the actual generated class names
4. The unnumbered `section_model_input.py` is never written because it was replaced by numbered variants

The same issue affects:
- `conditional_model_input_2` (referenced but not generated)
- `section_model_input` (referenced but not generated)
- Any recursive schema with `-Input`/`-Output` suffix

## Impact

This bug prevents importing any models that contain recursive type definitions, making pyopenapi-gen 5.0.3 unusable for complex OpenAPI schemas like Galaxy's API (3000+ schemas with recursive tool parameter definitions).

## Files in this reproducer

- `minimal_schema.yaml` - Simple schema that works correctly
- `discriminated_union_schema.yaml` - Schema that triggers the bug
- `README.md` - This file

## Environment

- pyopenapi-gen version: 5.0.3
- Python version: 3.12+
- OS: Any
