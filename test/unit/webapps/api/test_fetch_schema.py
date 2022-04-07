from galaxy.schema.fetch_data import (
    FetchDataPayload,
    FileDataElement,
    NestedElement,
    PastedDataElement,
    UrlDataElement,
)

HISTORY_ID = "abcdef0123456789"
example_payload = {
    "targets": [
        {
            "destination": {"type": "hdas"},
            "elements": [
                {
                    "src": "pasted",
                    "paste_content": "abcdef",
                    "name": None,
                    "dbkey": "?",
                    "ext": "auto",
                    "space_to_tab": False,
                    "to_posix_lines": True,
                },
                {"src": "url", "url": "https://github.com/bla.txt"},
                {"src": "files", "name": "uploaded file"},
            ],
        }
    ],
    "auto_decompress": True,
    "files": [],
    "history_id": HISTORY_ID,
}
items_payload = {
    "targets": [
        {
            "destination": {"type": "hdas"},
            "items": [
                {
                    "src": "url",
                    "url": "https://raw.githubusercontent.com/galaxyproject/galaxy/dev/test-data/html_file.txt",
                },
            ],
        }
    ],
    "history_id": HISTORY_ID,
}

nested_collection_payload = {
    "targets": [
        {
            "destination": {"type": "hdca"},
            "elements": [{"name": "samp1", "elements": [{"src": "files", "dbkey": "hg19", "info": "my cool bed"}]}],
            "collection_type": "list:list",
            "name": "Test upload",
        }
    ],
    "history_id": HISTORY_ID,
}


def test_fetch_data_schema():
    payload = FetchDataPayload(**example_payload)
    elements = payload.targets[0].elements
    assert len(elements) == 3
    assert isinstance(elements[0], PastedDataElement)
    assert isinstance(elements[1], UrlDataElement)
    assert isinstance(elements[2], FileDataElement)


def test_data_items():
    FetchDataPayload(**items_payload)


def test_nested_collection():
    payload = FetchDataPayload(**nested_collection_payload)
    collection_element = payload.targets[0].elements[0]
    assert isinstance(collection_element, NestedElement)
    assert isinstance(collection_element.elements[0], FileDataElement)
