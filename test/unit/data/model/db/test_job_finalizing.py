from sqlalchemy.orm import Session

from galaxy.model import Job


def test_unsaved_job_can_claim_and_resume_finalization():
    job = Job()
    job.set_state(Job.states.RUNNING)

    assert job.claim_finalization()
    assert job.state == Job.states.FINALIZING
    assert job.claim_finalization()


def test_job_rejects_finalization_from_terminal_or_new_state():
    new_job = Job()
    assert not new_job.claim_finalization()

    terminal_job = Job()
    terminal_job.set_state(Job.states.ERROR)
    assert not terminal_job.claim_finalization()


def test_nonterminal_states_do_not_replace_finalizing_state():
    job = Job()
    job.set_state(Job.states.RUNNING)
    job.claim_finalization()

    assert not job.set_state(Job.states.STOPPED)
    assert not job.set_state(Job.states.RUNNING)
    assert job.state == Job.states.FINALIZING


def test_database_claim_is_durable_and_rejects_stale_nonterminal_update(session, make_job):
    job = make_job()
    job.set_state(Job.states.RUNNING)
    session.commit()

    stale_session = Session(bind=session.get_bind())
    try:
        stale_job = stale_session.get(Job, job.id)
        assert stale_job is not None
        assert stale_job.state == Job.states.RUNNING

        assert job.claim_finalization()
        session.commit()

        # The second session still sees RUNNING in memory, but set_state's
        # compare-and-set must not overwrite FINALIZING in the database.
        assert not stale_job.set_state(Job.states.STOPPED)
        stale_session.rollback()
        stale_session.expire_all()
        finalizing_job = stale_session.get(Job, job.id)
        assert finalizing_job is not None
        assert finalizing_job.state == Job.states.FINALIZING
    finally:
        stale_session.close()
