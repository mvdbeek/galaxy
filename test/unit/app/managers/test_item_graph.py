import pytest
from sqlalchemy import union

from galaxy.managers.jobs import JobConnectionsManager
from galaxy.model import (
    HistoryDatasetAssociation,
    HistoryDatasetCollectionAssociation,
    Job,
)
from galaxy.model.scoped_session import galaxy_scoped_session
from galaxy.model.unittest_utils import GalaxyDataTestApp


@pytest.fixture
def sa_session():
    return GalaxyDataTestApp().model.session


@pytest.fixture
def job_connections_manager(sa_session) -> JobConnectionsManager:
    gm = JobConnectionsManager(sa_session)
    return gm


def setup_connected_dataset(sa_session: galaxy_scoped_session):
    center_hda = HistoryDatasetAssociation(sa_session=sa_session)
    input_hda = HistoryDatasetAssociation(sa_session=sa_session)
    input_hdca = HistoryDatasetCollectionAssociation()
    output_hda = HistoryDatasetAssociation(sa_session=sa_session)
    output_hdca = HistoryDatasetCollectionAssociation()
    input_job = Job()
    output_job = Job()
    input_job.add_output_dataset("output_hda", center_hda)
    input_job.add_input_dataset("input_hda", input_hda)
    input_job.add_input_dataset_collection("input_hdca", input_hdca)
    output_job.add_input_dataset("input_hda", center_hda)
    output_job.add_output_dataset("output_hda", output_hda)
    output_job.add_output_dataset_collection("output_hdca", output_hdca)
    sa_session.add_all([center_hda, input_hda, input_hdca, output_hdca, input_job, output_job])
    sa_session.flush()
    expected_graph = {
        "input": [{"src": "hda", "id": input_hda.id}, {"src": "hdca", "id": input_hdca.id}],
        "output": [{"src": "hda", "id": output_hda.id}, {"src": "hdca", "id": output_hdca.id}],
    }
    return center_hda, expected_graph


def test_graph_manager_inputs_for_hda(job_connections_manager: JobConnectionsManager):
    sa_session = job_connections_manager.sa_session
    center_hda, expected_graph = setup_connected_dataset(sa_session)
    s = job_connections_manager.inputs_for_hda(center_hda.id)
    assert len(sa_session.execute(union(*s)).all()) == 2


def test_graph_manager(job_connections_manager: JobConnectionsManager):
    center_hda, expected_graph = setup_connected_dataset(job_connections_manager.sa_session)
    job_connections_manager.get_graph(center_hda) == expected_graph
