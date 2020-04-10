import gc
import json
import os
import resource

import psutil

from db_shell import (
    install_model,
    install_session,
    get_install_session,
    combined_install_database,
    install_db_url,
    sa_session,
)
from sqlalchemy.orm import defer


process = psutil.Process(os.getpid())
state = {'current_memory': [], 'max_memory': []}


def my_function():
    q = install_session.context.query(install_model.ToolShedRepository)
    q = q.options(defer(install_model.ToolShedRepository.metadata))
    q.all()
    mm = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    state['max_memory'].append(mm)
    print('Max  Memory usage: %s (KB)' % mm)
    cm = process.memory_info().rss / 1024
    state['current_memory'].append(cm)
    print('Curr Memory usage: %s (KB)' % cm)


if __name__ == '__main__':
    for _ in range(100):
        install_session.context.expire_all()
        install_session.context.close_all()
        install_session.engine.dispose()
        install_session = get_install_session(combined_install_database, install_db_url, sa_session)
        my_function()
    with open('memory_gc_collect.json', 'w') as out:
        out.write(json.dumps(state))
