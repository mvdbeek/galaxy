from typing import TYPE_CHECKING

from ...models.job_lock import JobLock
from ...models.job_lock_job_lock_status_param_run_as import JobLockJobLockStatusParamRunAs
from ...models.job_lock_update_job_lock_param_run_as import JobLockUpdateJobLockParamRunAs

if TYPE_CHECKING:
    pass


class MockJobLockClient:
    """
    Mock implementation of JobLockClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestJobLockClient(MockJobLockClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def job_lock_job_lock_status(
        self,
        run_as: JobLockJobLockStatusParamRunAs | None = None,
    ) -> JobLock:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobLockClient.job_lock_job_lock_status() not implemented. Override this method in your test subclass."
        )

    async def job_lock_update_job_lock(
        self,
        body: JobLock,
        run_as: JobLockUpdateJobLockParamRunAs | None = None,
    ) -> JobLock:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobLockClient.job_lock_update_job_lock() not implemented. Override this method in your test subclass."
        )
