import pytest

from galaxy.datatypes.data import Directory
from .util import (
    get_input_files,
    MockDataset,
    MockDatasetDataset,
)


class _Kraken2Like(Directory):
    file_ext = "kraken2db"
    peek_text = "Compressed Kraken2 database"
    required_files = ["hash.k2d", "opts.k2d", "taxo.k2d", "seqid2taxid.k2d"]


@pytest.mark.parametrize("input_file", ["1.kraken2db.tar.gz"])
def test_kraken2db_sniff(input_file):
    with get_input_files(input_file) as input_files:
        assert _Kraken2Like().sniff(input_files[0]) is True


@pytest.mark.parametrize("input_file", ["1.kraken2db.tar.gz"])
def test_kraken2db_set_peek(input_file):
    loader = _Kraken2Like()
    with get_input_files(input_file) as input_files:
        dataset = MockDataset(1)
        dataset.set_file_name(input_files[0])
        dataset.dataset = MockDatasetDataset(dataset.get_file_name())
        loader.set_peek(dataset)
        assert dataset.peek == loader.peek_text


@pytest.mark.parametrize("input_file", ["1.kraken2db.tar.gz"])
def test_plain_directory_does_not_sniff(input_file):
    with get_input_files(input_file) as input_files:
        assert Directory().sniff(input_files[0]) is False
