import argparse
import datetime
import os
import sys

from sqlalchemy import (
    create_engine,
    text,
)

sys.path.insert(
    1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, os.pardir, "lib"))
)

from galaxy.model.orm.scripts import get_config

DESCRIPTION = """Remove old galaxy_session and expired session_refresh_token records from database."""


def main():
    args = _get_parser().parse_args()
    config = get_config(sys.argv, use_argparse=False, cwd=os.getcwd())
    engine = create_engine(config["db_url"])
    run(engine=engine, max_update_time=args.updated)


def _get_parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "--updated",
        type=datetime.datetime.fromisoformat,
        help="most recent `updated` date/time in ISO format  (for example, March 11, 1952 is represented as '1952-03-11')",
    )
    return parser


def run(engine, max_update_time=None):
    max_update_time = max_update_time or _get_default_max_update_time()
    """Delete galaxy_session records updated prior to `max_update_time`
    and expired/revoked refresh tokens."""
    with engine.begin() as conn:
        # Clean up old galaxy_session rows
        stmt = text("DELETE FROM galaxy_session WHERE update_time < :update_time")
        conn.execute(stmt, {"update_time": max_update_time})

        # Clean up expired or revoked refresh tokens
        _cleanup_refresh_tokens(conn)


def _cleanup_refresh_tokens(conn):
    """Delete expired or revoked session_refresh_token rows."""
    try:
        stmt = text("DELETE FROM session_refresh_token WHERE expires_at < NOW() OR is_valid = false")
        conn.execute(stmt)
    except Exception:
        # Table may not exist yet (pre-migration)
        pass


def _get_default_max_update_time():
    """By default, do not delete galaxy_sessions updated less than a month ago."""
    today = datetime.date.today()
    return today.replace(month=today.month - 1)


if __name__ == "__main__":
    main()
