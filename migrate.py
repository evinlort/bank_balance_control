#!/usr/bin/env python
import os
import subprocess
import sys
import logging

import psutil

print("Migrations here")

database = "bbc"


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
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(funcName)s:%(lineno)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

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
            self.run_migration(migration_file)

    def add_to_plan(self, filename):
        sql = f"""
            INSERT INTO migrations.plan VALUES ('{filename}')
        """
        cmd = [
            "psql",
            database,
            "-c",
            f'"{sql}"'
        ]
        rc, o, e = execute(cmd)
        assert not rc, e

    def run_migration(self, filename):
        if filename.startswith("_"):
            return
        if self.is_migrated(filename):
            self.logger.info(f"{filename} already executed")
            return
        cmd = [
            "psql",
            database,
            "<",
            f"migrations/{filename}"
        ]
        rc, o, e = execute(cmd)
        assert not rc, e
        self.add_to_plan(filename)

    def is_migrated(self, filename):
        query = f"""
            SELECT migration FROM migrations.plan WHERE migration = '{filename}'
        """
        cmd = [
            "psql",
            database,
            "-t",
            "-c",
            f'"{query}"',

        ]
        rc, o, e = execute(cmd)
        assert not rc, e

        self.logger.info(o)
        self.logger.info(e)
        if len(o) == 1 and o[0].strip() == filename:
            return True
        return False

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
