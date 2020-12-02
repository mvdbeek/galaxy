"""
API operations on a jobs.

.. seealso:: :class:`galaxy.model.Jobs`
"""

import logging
import typing
from functools import lru_cache

from fastapi import (
    Body,
    Depends,
)
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter as APIRouter
from pydantic import (
    BaseModel,
    Field,
)
from sqlalchemy import (
    or_,
)

from galaxy import (
    exceptions,
    model,
    util,
)
from galaxy.app import UniverseApplication
from galaxy.managers import hdas
from galaxy.managers.jobs import (
    JobManager,
    JobSearch,
    summarize_destination_params,
    summarize_job_metrics,
    summarize_job_parameters,
)
from galaxy.schema.fields import EncodedDatabaseIdField
from galaxy.web import (
    expose_api,
    expose_api_anonymous,
    require_admin,
)
from galaxy.webapps.base.controller import (
    BaseAPIController,
    UsesVisualizationMixin
)
from galaxy.work.context import (
    SessionRequestContext,
    WorkRequestContext,
)
from . import (
    get_admin_user,
    get_app,
    get_trans,
)

log = logging.getLogger(__name__)

router = APIRouter(tags=["jobs"])


@lru_cache()
def get_job_manager(app: UniverseApplication = Depends(get_app)) -> JobManager:
    return JobManager(app=app)


@lru_cache()
def get_job_search(app: UniverseApplication = Depends(get_app)) -> JobSearch:
    return JobSearch(app=app)


@lru_cache()
def get_hda_manager(app: UniverseApplication = Depends(get_app)) -> hdas.HDAManager:
    return hdas.HDAManager(app=app)


class JobLock(BaseModel):
    active: bool = Field(title="Job lock status", description="If active, jobs will not dispatch")


@cbv(router)
class FastAPIJobs:
    job_manager: JobManager = Depends(get_job_manager)
    job_search: JobSearch = Depends(get_job_search)
    hda_manager: hdas.HDAManager = Depends(get_hda_manager)
    trans: SessionRequestContext = Depends(get_trans)

    @router.get('/job_lock')
    def job_lock_status(self, admin_user=Depends(get_admin_user)) -> JobLock:
        """Get job lock status."""
        return JobLock(active=self.trans.app.job_manager.job_lock)

    @router.put('/job_lock')
    def update_job_lock(self, admin_user=Depends(get_admin_user), job_lock: JobLock = Body(...)) -> JobLock:
        """Set job lock status."""
        self.trans.app.queue_worker.send_control_task('admin_job_lock', kwargs={'job_lock': job_lock.active}, get_response=True)
        return JobLock(active=self.trans.app.job_manager.job_lock)

    @router.get("/{id}")
    def show(self, id: EncodedDatabaseIdField, full: typing.Optional[bool] = False) -> typing.Dict:
        """
        Return dictionary containing description of job data

        Parameters
        - id: ID of job to return
        - full: Return extra information ?
        """
        trans = self.trans
        id = trans.app.security.decode_id(id)
        job = self.job_manager.get_accessible_job(trans, id)
        is_admin = trans.user_is_admin
        job_dict = trans.app.security.encode_all_ids(job.to_dict('element', system_details=is_admin), True)
        if full:
            job_dict.update(dict(
                tool_stdout=job.tool_stdout,
                tool_stderr=job.tool_stderr,
                job_stdout=job.job_stdout,
                job_stderr=job.job_stderr,
                stderr=job.stderr,
                stdout=job.stdout,
                job_messages=job.job_messages
            ))

            if is_admin:
                if job.user:
                    job_dict['user_email'] = job.user.email
                else:
                    job_dict['user_email'] = None

                job_dict['job_metrics'] = summarize_job_metrics(trans, job)
        return job_dict


class JobController(BaseAPIController, UsesVisualizationMixin):

    def __init__(self, app):
        super().__init__(app)
        self.job_manager = JobManager(app)
        self.job_search = JobSearch(app)
        self.hda_manager = hdas.HDAManager(app)

    @expose_api
    def index(self, trans, **kwd):
        """
        index( trans, state=None, tool_id=None, history_id=None, date_range_min=None, date_range_max=None, user_details=False )
        * GET /api/jobs:
            return jobs for current user

            !! if user is admin and user_details is True, then
                return jobs for all galaxy users based on filtering - this is an extended service

        :type   state: string or list
        :param  state: limit listing of jobs to those that match one of the included states. If none, all are returned.
        Valid Galaxy job states include:
                'new', 'upload', 'waiting', 'queued', 'running', 'ok', 'error', 'paused', 'deleted', 'deleted_new'

        :type   tool_id: string or list
        :param  tool_id: limit listing of jobs to those that match one of the included tool_ids. If none, all are returned.

        :type   user_details: boolean
        :param  user_details: if true, and requestor is an admin, will return external job id and user email.

        :type   date_range_min: string '2014-01-01'
        :param  date_range_min: limit the listing of jobs to those updated on or after requested date

        :type   date_range_max: string '2014-12-31'
        :param  date_range_max: limit the listing of jobs to those updated on or before requested date

        :type   history_id: string
        :param  history_id: limit listing of jobs to those that match the history_id. If none, all are returned.

        :rtype:     list
        :returns:   list of dictionaries containing summary job information
        """
        state = kwd.get('state', None)
        is_admin = trans.user_is_admin
        user_details = kwd.get('user_details', False)

        if is_admin:
            query = trans.sa_session.query(trans.app.model.Job)
        else:
            query = trans.sa_session.query(trans.app.model.Job).filter(trans.app.model.Job.user == trans.user)

        def build_and_apply_filters(query, objects, filter_func):
            if objects is not None:
                if isinstance(objects, str):
                    query = query.filter(filter_func(objects))
                elif isinstance(objects, list):
                    t = []
                    for obj in objects:
                        t.append(filter_func(obj))
                    query = query.filter(or_(*t))
            return query

        query = build_and_apply_filters(query, state, lambda s: trans.app.model.Job.state == s)

        query = build_and_apply_filters(query, kwd.get('tool_id', None), lambda t: trans.app.model.Job.tool_id == t)
        query = build_and_apply_filters(query, kwd.get('tool_id_like', None), lambda t: trans.app.model.Job.tool_id.like(t))

        query = build_and_apply_filters(query, kwd.get('date_range_min', None), lambda dmin: trans.app.model.Job.table.c.update_time >= dmin)
        query = build_and_apply_filters(query, kwd.get('date_range_max', None), lambda dmax: trans.app.model.Job.table.c.update_time <= dmax)

        history_id = kwd.get('history_id', None)
        if history_id is not None:
            try:
                decoded_history_id = self.decode_id(history_id)
                query = query.filter(trans.app.model.Job.history_id == decoded_history_id)
            except Exception:
                raise exceptions.ObjectAttributeInvalidException()

        out = []
        if kwd.get('order_by') == 'create_time':
            order_by = trans.app.model.Job.create_time.desc()
        else:
            order_by = trans.app.model.Job.update_time.desc()
        for job in query.order_by(order_by).all():
            job_dict = job.to_dict('collection', system_details=is_admin)
            j = self.encode_all_ids(trans, job_dict, True)
            if user_details:
                j['user_email'] = job.user.email
            out.append(j)

        return out

    @expose_api_anonymous
    def show(self, trans, id, **kwd):
        """
        show( trans, id )
        * GET /api/jobs/{id}:
            return jobs for current user

        :type   id: string
        :param  id: Specific job id

        :type   full: boolean
        :param  full: whether to return extra information

        :rtype:     dictionary
        :returns:   dictionary containing full description of job data
        """
        job = self.__get_job(trans, id)
        is_admin = trans.user_is_admin
        job_dict = self.encode_all_ids(trans, job.to_dict('element', system_details=is_admin), True)
        full_output = util.asbool(kwd.get('full', 'false'))
        if full_output:
            if job.copied_from_job_id is not None:
                encoded_copied_from_job_id = trans.security.encode_id(job.copied_from_job_id)
            else:
                encoded_copied_from_job_id = None
            job_dict.update(dict(
                tool_stdout=job.tool_stdout,
                tool_stderr=job.tool_stderr,
                tool_version=job.tool_version,
                copied_from_job_id=encoded_copied_from_job_id,
                job_stdout=job.job_stdout,
                job_stderr=job.job_stderr,
                stderr=job.stderr,
                stdout=job.stdout,
                job_messages=job.job_messages
            ))

            if is_admin:
                if job.user:
                    job_dict['user_email'] = job.user.email
                else:
                    job_dict['user_email'] = None

                job_dict['job_metrics'] = summarize_job_metrics(trans, job)
        return job_dict

    @expose_api
    def common_problems(self, trans, id, **kwd):
        """
        * GET /api/jobs/{id}/common_problems
            check inputs and job for common potential problems to aid in error reporting
        """
        job = self.__get_job(trans, id)
        seen_ids = set()
        has_empty_inputs = False
        has_duplicate_inputs = False
        for job_input_assoc in job.input_datasets:
            input_dataset_instance = job_input_assoc.dataset
            if input_dataset_instance is None:
                continue
            if input_dataset_instance.get_total_size() == 0:
                has_empty_inputs = True
            input_instance_id = input_dataset_instance.id
            if input_instance_id in seen_ids:
                has_duplicate_inputs = True
            else:
                seen_ids.add(input_instance_id)
        # TODO: check percent of failing jobs around a window on job.update_time for handler - report if high.
        # TODO: check percent of failing jobs around a window on job.update_time for destination_id - report if high.
        # TODO: sniff inputs (add flag to allow checking files?)
        return {"has_empty_inputs": has_empty_inputs, "has_duplicate_inputs": has_duplicate_inputs}

    @expose_api
    def inputs(self, trans, id, **kwd):
        """
        show( trans, id )
        * GET /api/jobs/{id}/inputs
            returns input datasets created by job

        :type   id: string
        :param  id: Encoded job id

        :rtype:     dictionary
        :returns:   dictionary containing input dataset associations
        """
        job = self.__get_job(trans, id)
        return self.__dictify_associations(trans, job.input_datasets, job.input_library_datasets)

    @expose_api
    def outputs(self, trans, id, **kwd):
        """
        outputs( trans, id )
        * GET /api/jobs/{id}/outputs
            returns output datasets created by job

        :type   id: string
        :param  id: Encoded job id

        :rtype:     dictionary
        :returns:   dictionary containing output dataset associations
        """
        job = self.__get_job(trans, id)
        return self.__dictify_associations(trans, job.output_datasets, job.output_library_datasets)

    @expose_api
    def delete(self, trans, id, **kwd):
        """
        delete( trans, id )
        * Delete /api/jobs/{id}
            cancels specified job

        :type   id: string
        :param  id: Encoded job id
        :type   message: string
        :param  message: Stop message.
        """
        payload = kwd.get("payload") or {}
        job = self.__get_job(trans, id)
        message = payload.get("message", None)
        return self.job_manager.stop(job, message=message)

    @expose_api
    def resume(self, trans, id, **kwd):
        """
        * PUT /api/jobs/{id}/resume
            Resumes a paused job

        :type   id: string
        :param  id: Encoded job id

        :rtype:     dictionary
        :returns:   dictionary containing output dataset associations
        """
        job = self.__get_job(trans, id)
        if not job:
            raise exceptions.ObjectNotFound("Could not access job with id '%s'" % id)
        if job.state == job.states.PAUSED:
            job.resume()
        else:
            exceptions.RequestParameterInvalidException("Job with id '%s' is not paused" % (job.tool_id))
        return self.__dictify_associations(trans, job.output_datasets, job.output_library_datasets)

    @expose_api_anonymous
    def metrics(self, trans, **kwd):
        """
        * GET /api/jobs/{job_id}/metrics
        * GET /api/datasets/{dataset_id}/metrics
            Return job metrics for specified job. Job accessibility checks are slightly
            different than dataset checks, so both methods are available.

        :type   job_id: string
        :param  job_id: Encoded job id

        :type   dataset_id: string
        :param  dataset_id: Encoded HDA or LDDA id

        :type   hda_ldda: string
        :param  hda_ldda: hda if dataset_id is an HDA id (default), ldda if
                          it is an ldda id.

        :rtype:     list
        :returns:   list containing job metrics
        """
        job = self.__get_job(trans, **kwd)
        return summarize_job_metrics(trans, job)

    @require_admin
    @expose_api
    def destination_params(self, trans, **kwd):
        """
        * GET /api/jobs/{job_id}/destination_params
            Return destination parameters for specified job.

        :type   job_id: string
        :param  job_id: Encoded job id

        :rtype:     list
        :returns:   list containing job destination parameters
        """
        job = self.__get_job(trans, **kwd)
        return summarize_destination_params(trans, job)

    @expose_api_anonymous
    def parameters_display(self, trans, **kwd):
        """
        * GET /api/jobs/{job_id}/parameters_display
        * GET /api/datasets/{dataset_id}/parameters_display

            Resolve parameters as a list for nested display. More client logic
            here than is ideal but it is hard to reason about tool parameter
            types on the client relative to the server. Job accessibility checks
            are slightly different than dataset checks, so both methods are
            available.

            This API endpoint is unstable and tied heavily to Galaxy's JS client code,
            this endpoint will change frequently.

        :type   job_id: string
        :param  job_id: Encoded job id

        :type   dataset_id: string
        :param  dataset_id: Encoded HDA or LDDA id

        :type   hda_ldda: string
        :param  hda_ldda: hda if dataset_id is an HDA id (default), ldda if
                          it is an ldda id.

        :rtype:     list
        :returns:   job parameters for for display
        """
        job = self.__get_job(trans, **kwd)
        return summarize_job_parameters(trans, job)

    @expose_api_anonymous
    def build_for_rerun(self, trans, id, **kwd):
        """
        * GET /api/jobs/{id}/build_for_rerun
            returns a tool input/param template prepopulated with this job's
            information, suitable for rerunning or rendering parameters of the
            job.

        :type   id: string
        :param  id: Encoded job id

        :rtype:     dictionary
        :returns:   dictionary containing output dataset associations
        """

        job = self.__get_job(trans, id)
        if not job:
            raise exceptions.ObjectNotFound("Could not access job with id '%s'" % id)
        tool = self.app.toolbox.get_tool(job.tool_id, kwd.get('tool_version') or job.tool_version)
        if tool is None:
            raise exceptions.ObjectNotFound("Requested tool not found")
        if not tool.is_workflow_compatible:
            raise exceptions.ConfigDoesNotAllowException("Tool '%s' cannot be rerun." % (job.tool_id))
        return tool.to_json(trans, {}, job=job)

    def __dictify_associations(self, trans, *association_lists):
        rval = []
        for association_list in association_lists:
            rval.extend(self.__dictify_association(trans, a) for a in association_list)
        return rval

    def __dictify_association(self, trans, job_dataset_association):
        dataset_dict = None
        dataset = job_dataset_association.dataset
        if dataset:
            if isinstance(dataset, model.HistoryDatasetAssociation):
                dataset_dict = dict(src="hda", id=trans.security.encode_id(dataset.id))
            else:
                dataset_dict = dict(src="ldda", id=trans.security.encode_id(dataset.id))
        return dict(name=job_dataset_association.name, dataset=dataset_dict)

    def __get_job(self, trans, job_id=None, dataset_id=None, **kwd):
        if job_id is not None:
            decoded_job_id = self.decode_id(job_id)
            return self.job_manager.get_accessible_job(trans, decoded_job_id)
        else:
            hda_ldda = kwd.get("hda_ldda", "hda")
            # Following checks dataset accessible
            dataset_instance = self.get_hda_or_ldda(trans, hda_ldda=hda_ldda, dataset_id=dataset_id)
            return dataset_instance.creating_job

    @expose_api
    def create(self, trans, payload, **kwd):
        """ See the create method in tools.py in order to submit a job. """
        raise exceptions.NotImplemented('Please POST to /api/tools instead.')

    @expose_api
    def search(self, trans, payload, **kwd):
        """
        search( trans, payload )
        * POST /api/jobs/search:
            return jobs for current user

        :type   payload: dict
        :param  payload: Dictionary containing description of requested job. This is in the same format as
            a request to POST /apt/tools would take to initiate a job

        :rtype:     list
        :returns:   list of dictionaries containing summary job information of the jobs that match the requested job run

        This method is designed to scan the list of previously run jobs and find records of jobs that had
        the exact some input parameters and datasets. This can be used to minimize the amount of repeated work, and simply
        recycle the old results.
        """
        tool_id = payload.get('tool_id')
        if tool_id is None:
            raise exceptions.RequestParameterMissingException("No tool id")
        tool = trans.app.toolbox.get_tool(tool_id)
        if tool is None:
            raise exceptions.ObjectNotFound("Requested tool not found")
        if 'inputs' not in payload:
            raise exceptions.RequestParameterMissingException("No inputs defined")
        inputs = payload.get('inputs', {})
        # Find files coming in as multipart file data and add to inputs.
        for k, v in payload.items():
            if k.startswith('files_') or k.startswith('__files_'):
                inputs[k] = v
        request_context = WorkRequestContext(app=trans.app, user=trans.user, history=trans.history)
        all_params, all_errors, _, _ = tool.expand_incoming(trans=trans, incoming=inputs, request_context=request_context)
        if any(all_errors):
            return []
        params_dump = [tool.params_to_strings(param, self.app, nested=True) for param in all_params]
        jobs = []
        for param_dump, param in zip(params_dump, all_params):
            job = self.job_search.by_tool_input(trans=trans,
                                                tool_id=tool_id,
                                                tool_version=tool.version,
                                                param=param,
                                                param_dump=param_dump,
                                                job_state=payload.get('state'))
            if job:
                jobs.append(job)
        return [self.encode_all_ids(trans, single_job.to_dict('element'), True) for single_job in jobs]

    @expose_api_anonymous
    def error(self, trans, id, payload, **kwd):
        """
        error( trans, id )
        * POST /api/jobs/{id}/error
            submits a bug report via the API.

        :type   id: string
        :param  id: Encoded job id

        :rtype:     dictionary
        :returns:   dictionary containing information regarding where the error report was sent.
        """
        # Get dataset on which this error was triggered
        dataset_id = payload.get('dataset_id')
        if not dataset_id:
            raise exceptions.RequestParameterMissingException('No dataset_id')
        decoded_dataset_id = self.decode_id(dataset_id)
        dataset = self.hda_manager.get_accessible(decoded_dataset_id, trans.user)

        # Get job
        job = self.__get_job(trans, id)
        if dataset.creating_job.id != job.id:
            raise exceptions.RequestParameterInvalidException('dataset_id was not created by job_id')
        tool = trans.app.toolbox.get_tool(job.tool_id, tool_version=job.tool_version) or None
        email = payload.get('email')
        if not email and not trans.anonymous:
            email = trans.user.email
        messages = trans.app.error_reports.default_error_plugin.submit_report(
            dataset=dataset,
            job=job,
            tool=tool,
            user_submission=True,
            user=trans.user,
            email=email,
            message=payload.get('message')
        )

        return {'messages': messages}

    @require_admin
    @expose_api
    def show_job_lock(self, trans, **kwd):
        """
        * GET /api/job_lock
            return boolean indicating if job lock active.
        """
        return {"active": self.app.job_manager.job_lock}

    @require_admin
    @expose_api
    def update_job_lock(self, trans, payload, **kwd):
        """
        * PUT /api/job_lock
            return boolean indicating if job lock active.
        """
        job_lock = payload.get("active")
        self.app.queue_worker.send_control_task('admin_job_lock', kwargs={'job_lock': job_lock}, get_response=True)
        return {"active": self.app.job_manager.job_lock}
