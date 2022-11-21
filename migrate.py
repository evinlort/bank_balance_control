#!/usr/bin/env python
import os
import subprocess
import sys

import psutil

print("Migrations here")

database_init = "template1"


def execute(cmd: list):
    execline = " ".join(cmd)
    p = psutil.Popen(
        execline,
        env=os.environ,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    out, err = p.communicate()
    rc = p.returncode

    if out:
        out = [line for line in out.decode("utf-8").split("\n") if line]
    else:
        out = ""
    if err:
        err = [line for line in err.decode("utf-8").split("\n") if line]
    else:
        err = ""
    return rc, out, err


class Migrate:
    def init(self):
        cmd = [
            "ls",
            "-ltr",
            "migrations",
            "| awk",
            "'{print $9}'"
        ]
        _, migration_files, _ = execute(cmd)

        for migration_file in migration_files:
            print(migration_file)
            cmd = [
                "psql",
                database_init,
                "<",
                f"migrations/{migration_file}"
            ]
            rc, o, e = execute(cmd)
            print(o)
            print(e)
            assert not rc, e

    def list_databases(self):
        cmd = ["psql --list | tail -n +4| head -n -2 | awk '{print $1}' | sed 's/|//'"]
        rc, o, e = execute(cmd)
        assert not rc, e
        return o


if __name__ == "__main__":
    args = sys.argv[1:]
    migrate = Migrate()
    for arg in args:
        func = getattr(migrate, arg, False)
        if func:
            func()
        else:
            print("Not found")
