import json
import shutil
import tempfile
from pathlib import Path
from unittest import mock

import pytest

from galaxy import model
from galaxy.app_unittest_utils import galaxy_mock
from galaxy.app_unittest_utils.tools_support import UsesApp
from galaxy.tools.errors import EmailErrorReporter
from galaxy.util.unittest import TestCase
from galaxy.workflow.errors import WorkflowEmailErrorReporter

# The email the user created their account with.
TEST_USER_EMAIL = "mockgalaxyuser@galaxyproject.org"
# The email the user supplied when submitting the error
TEST_USER_SUPPLIED_EMAIL = "fake@example.org"
TEST_SERVER_EMAIL_FROM = "email_from@galaxyproject.org"
TEST_SERVER_ERROR_EMAIL_TO = "admin@email.to"  # setup in mock config


class TestErrorReporter(TestCase, UsesApp):
    def setUp(self):
        self.setup_app()
        self.app.config.email_from = TEST_SERVER_EMAIL_FROM
        self.tmp_path = Path(tempfile.mkdtemp())
        self.email_path = self.tmp_path / "email.json"
        smtp_server = f"mock_emails_to_path://{self.email_path}"
        self.app.config.smtp_server = smtp_server
        self.app.workflow_manager = mock.MagicMock()

    def tearDown(self):
        shutil.rmtree(self.tmp_path)

    def test_basic(self):
        user, hda = self._setup_model_objects()

        email_path = self.email_path
        assert not email_path.exists()
        error_report = EmailErrorReporter(hda, self.app)
        error_report.send_report(user, email=TEST_USER_SUPPLIED_EMAIL, message="My custom message")
        assert email_path.exists()
        text = email_path.read_text()
        email_json = json.loads(text)
        assert email_json["from"] == TEST_SERVER_EMAIL_FROM
        assert email_json["to"] == f"{TEST_SERVER_ERROR_EMAIL_TO}, {TEST_USER_SUPPLIED_EMAIL}"
        assert f"Galaxy tool error report from {TEST_USER_SUPPLIED_EMAIL}" == email_json["subject"]
        assert "cat1" in email_json["body"]
        assert "cat1" in email_json["html"]
        assert TEST_USER_EMAIL == email_json["reply_to"]

    @pytest.mark.parametrize("dependencies", [None, []])
    def test_environment_not_recorded(self, dependencies):
        user, hda = self._setup_model_objects()
        job = hda.creating_job
        job.dependencies = dependencies
        self._commit_objects([job])

        EmailErrorReporter(hda, self.app).send_report(user, email=TEST_USER_SUPPLIED_EMAIL)

        email_json = json.loads(self.email_path.read_text())
        assert "container id: Not recorded" in email_json["body"]
        assert "container type: Not recorded" in email_json["body"]
        assert "job dependencies:\nNot recorded" in email_json["body"]
        assert "<td>Container ID</td><td>Not recorded</td>" in email_json["html"]
        assert "<td>Container Type</td><td>Not recorded</td>" in email_json["html"]
        assert "<h4>Job Dependencies</h4>" in email_json["html"]

    def test_recorded_dependencies(self):
        user, hda = self._setup_model_objects()
        job = hda.creating_job
        dependencies = [
            {
                "name": "samtools",
                "version": "1.10",
                "dependency_type": "conda",
                "environment_path": "/conda/envs/samtools<1.10>",
            },
            {
                "name": "bwa",
                "version": "0.7.17",
                "dependency_type": "conda",
                "environment_path": "/jobs/1/conda-env",
            },
            {
                "name": "other",
                "version": "1.0",
                "dependency_type": "galaxy_package",
                "path": "/dependencies/other/1.0",
            },
        ]
        job.dependencies = dependencies
        self._commit_objects([job])

        EmailErrorReporter(hda, self.app).send_report(user, email=TEST_USER_SUPPLIED_EMAIL)

        email_json = json.loads(self.email_path.read_text())
        reported_dependencies = email_json["body"].split("job dependencies:\n", 1)[1].split("\n---", 1)[0]
        assert json.loads(reported_dependencies) == dependencies
        assert "/conda/envs/samtools&lt;1.10&gt;" in email_json["html"]
        assert "/conda/envs/samtools<1.10>" not in email_json["html"]
        assert "/jobs/1/conda-env" in email_json["html"]
        assert "/dependencies/other/1.0" in email_json["html"]

    @pytest.mark.parametrize("container_type", ["docker", "singularity"])
    def test_recorded_container_metrics(self, container_type):
        user, hda = self._setup_model_objects()
        job = hda.creating_job
        container_id = "quay.io/biocontainers/samtools:1.10<test>"
        job.add_metric("core", "container_id", container_id)
        job.add_metric("core", "container_type", container_type)
        job.add_metric("env", "container_id", "unrelated-container")
        job.add_metric("env", "SECRET_TOKEN", "secret-value")
        self._commit_objects([job])

        EmailErrorReporter(hda, self.app).send_report(user, email=TEST_USER_SUPPLIED_EMAIL)

        email_json = json.loads(self.email_path.read_text())
        assert f"container id: {container_id}" in email_json["body"]
        assert f"container type: {container_type}" in email_json["body"]
        assert "quay.io/biocontainers/samtools:1.10&lt;test&gt;" in email_json["html"]
        assert container_id not in email_json["html"]
        assert f"<td>Container Type</td><td>{container_type}</td>" in email_json["html"]
        for report in (email_json["body"], email_json["html"]):
            assert "unrelated-container" not in report
            assert "secret-value" not in report

    def test_workflow_error_reporting(self):
        user, invocation, trans = self._setup_invocation_model_objects()

        email_path = self.email_path
        assert not email_path.exists()
        error_report = WorkflowEmailErrorReporter(invocation, self.app)
        error_report.send_report(user, email=TEST_USER_SUPPLIED_EMAIL, message="My custom message", trans=trans)
        assert email_path.exists()
        text = email_path.read_text()
        email_json = json.loads(text)
        assert email_json["from"] == TEST_SERVER_EMAIL_FROM
        assert email_json["to"] == f"{TEST_SERVER_ERROR_EMAIL_TO}, {TEST_USER_SUPPLIED_EMAIL}"
        assert f"Galaxy workflow run error report from {TEST_USER_SUPPLIED_EMAIL}" == email_json["subject"]
        assert "Test Workflow" in email_json["body"]
        assert "Test Workflow" in email_json["html"]
        assert TEST_USER_EMAIL == email_json["reply_to"]

    def test_workflow_error_reporting_inaccessible_history(self):
        _, invocation, trans = self._setup_invocation_model_objects()
        other_user = model.User(email="otheruser@galaxyproject.org", password="mockpass2")
        self._commit_objects([other_user])

        email_path = self.email_path
        assert not email_path.exists()
        error_report = WorkflowEmailErrorReporter(invocation, self.app)
        self.app.workflow_manager.check_security.side_effect = Exception("Invocation is not accessible")  # type: ignore[attr-defined]
        error_report.send_report(other_user, email=TEST_USER_SUPPLIED_EMAIL, message="My custom message", trans=trans)
        # Same comment as in `test_hda_security`, but for accessibility of the invocation:
        # Without accessibility, the email still gets sent but the supplied email is ignored
        assert email_path.exists()
        text = email_path.read_text()
        email_json = json.loads(text)
        assert email_json["from"] == TEST_SERVER_EMAIL_FROM
        assert email_json["to"] == f"{TEST_SERVER_ERROR_EMAIL_TO}"

    def test_hda_security(self, tmp_path):
        user, hda = self._setup_model_objects()
        error_report = EmailErrorReporter(hda, self.app)
        security_agent = self.app.security_agent
        private_role = security_agent.create_private_user_role(user)
        access_action = security_agent.permitted_actions.DATASET_ACCESS.action
        manage_action = security_agent.permitted_actions.DATASET_MANAGE_PERMISSIONS.action
        permissions = {access_action: [private_role], manage_action: [private_role]}
        security_agent.set_all_dataset_permissions(hda.dataset, permissions)

        other_user = model.User(email="otheruser@galaxyproject.org", password="mockpass2")
        self._commit_objects([other_user])
        security_agent = self.app.security_agent
        email_path = self.email_path
        assert not email_path.exists()
        error_report.send_report(other_user, email=TEST_USER_SUPPLIED_EMAIL, message="My custom message")
        # Without permissions, the email still gets sent but the supplied email is ignored
        # I'm not saying this is the right behavior but it is what the code does at the time of test
        # writing -John
        assert email_path.exists()
        text = email_path.read_text()
        email_json = json.loads(text)
        assert "otheruser@galaxyproject.org" not in email_json["to"]

    def test_html_sanitization(self, tmp_path):
        user, hda = self._setup_model_objects()
        email_path = self.email_path
        assert not email_path.exists()
        error_report = EmailErrorReporter(hda, self.app)
        error_report.send_report(
            user, email=TEST_USER_SUPPLIED_EMAIL, message='My custom <a href="http://sneaky.com/">message</a>'
        )
        assert email_path.exists()
        text = email_path.read_text()
        email_json = json.loads(text)
        html = email_json["html"]
        assert "&lt;a href=&#34;http://sneaky.com/&#34;&gt;message&lt;/a&gt;" in html

    def test_redact_user_details_in_bugreport(self, tmp_path):
        user, hda = self._setup_model_objects()

        email_path = self.email_path
        assert not email_path.exists()
        error_report = EmailErrorReporter(hda, self.app)
        error_report.send_report(
            user, email=TEST_USER_SUPPLIED_EMAIL, message="My custom message", redact_user_details_in_bugreport=True
        )
        assert email_path.exists()
        text = email_path.read_text()
        email_json = json.loads(text)
        assert "The user redacted (user: 1) provided the following information:" in email_json["body"]
        assert (
            """The user <span style="font-family: monospace;">redacted (user: 1)</span> provided the following information:"""
            in email_json["html"]
        )

    def test_no_redact_user_details_in_bugreport(self, tmp_path):
        user, hda = self._setup_model_objects()

        email_path = self.email_path
        assert not email_path.exists()
        error_report = EmailErrorReporter(hda, self.app)
        error_report.send_report(
            user, email=TEST_USER_SUPPLIED_EMAIL, message="My custom message", redact_user_details_in_bugreport=False
        )
        assert email_path.exists()
        text = email_path.read_text()
        email_json = json.loads(text)
        assert (
            f"The user '{TEST_USER_EMAIL}' (providing preferred contact email '{TEST_USER_SUPPLIED_EMAIL}') provided the following information:"
            in email_json["body"]
        )
        assert (
            f"""The user <span style="font-family: monospace;">&#39;{TEST_USER_EMAIL}&#39; (providing preferred contact email &#39;{TEST_USER_SUPPLIED_EMAIL}&#39;)</span> provided the following information:"""
            in email_json["html"]
        )

    def _setup_model_objects(self):
        user = model.User(email=TEST_USER_EMAIL, password="mockpass")
        job = model.Job()
        job.tool_id = "cat1"
        job.history = model.History()
        job.user = user
        job.history.user = user
        hda = model.HistoryDatasetAssociation(history=job.history)
        hda.dataset = model.Dataset()
        hda.dataset.state = "ok"
        job.add_output_dataset("out1", hda)
        self._commit_objects([job, hda, user])
        return user, hda

    def _setup_invocation_model_objects(self):
        user = model.User(email=TEST_USER_EMAIL, password="mockpass")
        invocation = model.WorkflowInvocation()
        invocation.workflow = model.Workflow()
        invocation.workflow.name = "Test Workflow"
        invocation.workflow.stored_workflow = model.StoredWorkflow()
        invocation.workflow.stored_workflow.user = user
        invocation.history = model.History()
        invocation.history.user = user
        trans = galaxy_mock.MockTrans(app=self.app, history=invocation.history, user=user)
        self._commit_objects([user, invocation])
        return user, invocation, trans

    def _commit_objects(self, objects):
        session = self.app.model.context
        session.add_all(objects)
        session.commit()
