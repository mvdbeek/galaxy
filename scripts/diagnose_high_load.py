import os
import subprocess
import time
from datetime import (
    date,
    datetime,
)

import click
import psutil


DEFAULT_LOAD_CUTOFF = 5


def high_load_events(load_cutoff):
    while True:
        one_minute_avg, *_ = os.getloadavg()
        if one_minute_avg > load_cutoff:
            yield one_minute_avg
            time.sleep(1)
        else:
            time.sleep(30)


def get_gunicorn_pids():
    pids = []
    for p in psutil.process_iter():
        cmdline = p.cmdline()
        if len(cmdline) > 1:
            if cmdline[0].endswith("gunicorn") or cmdline[1].endswith("gunicorn"):
                pids.append(p.pid)
    return pids


def run_pyspy_on_pid(pid):
    output = subprocess.run(["py-spy", "dump", "--pid", str(pid)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return output.stdout


def write_dumps(dumps, directory="."):
    os.makedirs(directory, exist_ok=True)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    for pid, dump_d in dumps.items():
        for cpu_percent, dump in dump_d.items():
            filename = f"{date.today()}-{current_time}-{cpu_percent}-{pid}-dump.txt"
            with open(os.path.join(directory, filename), "wb") as out:
                out.write(dump)


@click.command()
@click.argument("directory", type=click.Path(file_okay=False))
@click.argument("load_cutoff", type=click.INT, default=DEFAULT_LOAD_CUTOFF)
def pyspy_on_high_load(directory, load_cutoff):
    for _ in high_load_events(load_cutoff):
        dumps = {}
        pids = get_gunicorn_pids()
        for pid in pids:
            p = psutil.Process(pid)
            # For whatever reason the first call to cpu_percent returns 0.0
            p.cpu_percent()
            dump = run_pyspy_on_pid(pid)
            dumps[pid] = {p.cpu_percent(): dump}
        write_dumps(dumps, directory)


if __name__ == "__main__":
    pyspy_on_high_load()
