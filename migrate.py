#!/usr/bin/env python
import os
import subprocess
import sys
import logging

import psutil

print("Migrations here")

database_for_init = "template1"
database = "bbc"


def execute(cmd: str):
    p = psutil.Popen(
        cmd,
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

        self.migrations_dir = "migrations"

    def init(self):
        migration_files = self.get_files_in_dir(self.migrations_dir)

        for migration_file in migration_files:
            self.run_migration(self.migrations_dir, migration_file, database=database_for_init)

    def deploy(self):
        deploy_dir = f"{self.migrations_dir}/deploy"
        migration_files = self.get_files_in_dir(deploy_dir)
        self.logger.info(migration_files)
        for migration_file in migration_files:
            if not self.is_migrated(migration_file):
                self.run_migration(deploy_dir, migration_file)
                self.add_to_plan(migration_file)

    def revert(self):
        revert_dir = f"{self.migrations_dir}/revert"
        migration_files = self.get_files_in_dir(revert_dir)
        for migration_file in migration_files:
            if self.is_migrated(migration_file):
                self.run_migration(revert_dir, migration_file)
                self.remove_from_plan(migration_file)

    def add(self, migration_name):
        migration_paths = [f"migrations/deploy/{migration_name}.sql", f"migrations/revert/{migration_name}.sql"]
        for migration_path in migration_paths:
            cmd = f"test -e {migration_path}"
            rc, o, e = execute(cmd)
            if not rc:
                self.logger.info(f"{migration_path} already exists. Skipping")
                continue
            self.logger.info(f"Creating the new {migration_path}")
            cmd = f"touch {migration_path}"
            rc, o, e = execute(cmd)
            assert not rc, e

    def remove(self, migration_name):
        migration_paths = [f"migrations/deploy/{migration_name}.sql", f"migrations/revert/{migration_name}.sql"]
        for migration_path in migration_paths:
            cmd = f"rm {migration_path}"
            rc, o, e = execute(cmd)
            assert not rc, e

    def add_to_plan(self, filename):
        sql = f"INSERT INTO migrations.plan VALUES ('{filename}')"
        self.logger.info(sql)
        self.execute_query(sql)

    def remove_from_plan(self, filename):
        sql = f"DELETE FROM migrations.plan WHERE migration = '{filename}'"
        self.logger.info(sql)
        self.execute_query(sql)

    def execute_query(self, sql):
        cmd = f"psql {database} -c \"{sql}\""
        rc, o, e = execute(cmd)
        assert not rc, e

    def run_migration(self, directory, filename, database=database):
        if filename.startswith("_"):
            return
        cmd = f"psql {database} < {directory}/{filename}"
        rc, o, e = execute(cmd)
        self.logger.info("Run Migration")
        self.logger.info(o)
        self.logger.info(e)
        assert not rc, e

    def is_migrated(self, filename):
        query = f"SELECT migration FROM migrations.plan WHERE migration = '{filename}'"
        cmd = f"psql {database} -t -c \"{query}\""
        rc, o, e = execute(cmd)
        self.logger.info(rc)
        assert not rc, e

        self.logger.info(o)
        self.logger.info(e)
        if not o:
            self.logger.info("No such entry")
            return False
        if len(o) == 1 and o[0].strip() == filename:
            self.logger.info("Entry exists")
            return True
        return False

    def list_databases(self):
        cmd = "psql --list | tail -n +4| head -n -2 | awk '{print $1}' | sed 's/|//'"
        rc, o, e = execute(cmd)
        assert not rc, e
        return o

    def get_files_in_dir(self, directory):
        cmd = f'find {directory} -maxdepth 1 -not -type d -printf "%T@ %Tc %p\n" | sort -n| awk \'{{print $7}}\''
        self.logger.info(cmd)
        _, migration_files_path, _ = execute(cmd)
        self.logger.info(migration_files_path)
        migration_files = [filename.split("/")[-1] for filename in migration_files_path]
        self.logger.info(migration_files)
        return migration_files


if __name__ == "__main__":
    args = sys.argv[1:]
    migrate = Migrate()
    func = getattr(migrate, args[0], False)
    if func:
        func(*args[1:])
    else:
        print("Not found")
