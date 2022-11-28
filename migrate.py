#!/usr/bin/env python
import os
import subprocess
import sys
import logging

import psutil

db_init = "template1"
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
            if not migration_file.startswith("_"):
                self.run_migration(self.migrations_dir, migration_file, db_init)

    def deploy(self):
        deploy_dir = f"{self.migrations_dir}/deploy"

        migration_files = self.get_files_in_dir(deploy_dir)
        migration_plan_files = self.get_plan_files()

        migrations_files = self.build_migrations_files_list(migration_files, migration_plan_files)

        for migration_file in migrations_files:
            if not self.is_migrated(migration_file):
                self.run_migration(deploy_dir, migration_file, database)
                self.add_to_migrated(migration_file)

    def revert(self):
        revert_dir = f"{self.migrations_dir}/revert"

        migration_files = self.get_files_in_dir(revert_dir)
        migration_plan_files = self.get_plan_files()

        migrations_files = self.build_migrations_files_list(migration_files, migration_plan_files)

        for migration_file in migrations_files:
            if self.is_migrated(migration_file):
                self.run_migration(revert_dir, migration_file, database)
                self.remove_from_migrated(migration_file)

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
        self.add_to_plan(f"{migration_name}.sql")

    def remove(self, migration_name):
        # TODO if in migrations.plan - firstly revert the migration (to the point)
        migration_paths = [f"migrations/deploy/{migration_name}.sql", f"migrations/revert/{migration_name}.sql"]
        for migration_path in migration_paths:
            cmd = f"rm {migration_path}"
            rc, o, e = execute(cmd)
            assert not rc, e

    def add_to_migrated(self, filename):
        sql = f"INSERT INTO migrations.migrated VALUES ('{filename}')"
        self.execute_query(sql)

    def add_to_plan(self, filename):
        sql1 = "SELECT apply_order + 1 AS next_value FROM migrations.plan ORDER BY apply_order DESC LIMIT 1;"
        cmd = f"psql {database} -c \"{sql1}\" | tail -n +3| head -n -2 | awk \'{{print $1}}\'"
        rc, o, e = execute(cmd)
        assert not rc, e
        if len(o) == 0:
            o = 1
        else:
            o = int(o[0])
        self.logger.info(o)
        sql2 = f"INSERT INTO migrations.plan VALUES ('{filename}', {o});"
        self.execute_query(sql2)

    def get_plan_files(self):
        query = "SELECT migration FROM migrations.plan ORDER BY apply_order ASC;"
        files = self.execute_query(query)
        return files

    def build_migrations_files_list(self, arr1, arr2):
        unordered_files = []
        for val1 in arr1:
            if val1 not in arr2:
                unordered_files.append(val1)
        return unordered_files + arr2

    def remove_from_migrated(self, filename):
        sql = f"DELETE FROM migrations.migrated WHERE migration = '{filename}'"
        self.execute_query(sql)

    def execute_query(self, sql):
        cmd = f"psql {database} -c \"{sql}\""
        rc, o, e = execute(cmd)
        assert not rc, e
        return [v.strip() for v in o[2:-1]]

    def run_migration(self, directory, filename, database):
        cmd = f"psql {database} < {directory}/{filename}"
        rc, o, e = execute(cmd)
        self.logger.info(f"Run Migration - {filename}")
        assert not rc, e

    def is_migrated(self, filename):
        query = f"SELECT migration FROM migrations.migrated WHERE migration = '{filename}'"
        cmd = f"psql {database} -t -c \"{query}\""
        rc, o, e = execute(cmd)
        assert not rc, e

        if not o:
            self.logger.info(f"No such entry - {filename}")
            return False
        if len(o) == 1 and o[0].strip() == filename:
            self.logger.info(f"Entry {filename} exists")
            return True
        return False

    def drop(self):
        if input("Are you sure? Y/N :").lower() == "y":
            migration_files = self.get_files_in_dir(self.migrations_dir)
            for migration_file in migration_files:
                if migration_file.startswith("_"):
                    self.run_migration(self.migrations_dir, migration_file, db_init)

    def list_databases(self):
        cmd = "psql --list | tail -n +4| head -n -2 | awk '{print $1}' | sed 's/|//'"
        rc, o, e = execute(cmd)
        assert not rc, e
        return o

    def list(self):
        sql = "\dt"
        tables = self.execute_query(sql)
        table_names = [table.split("|")[1].strip() for table in tables[1:]]
        print("\n".join(table_names))

    def get_files_in_dir(self, directory):
        cmd = f'find {directory} -maxdepth 1 -not -type d -printf "%T@ %Tc %p\n" | sort -n| awk \'{{print $7}}\''
        _, migration_files_path, _ = execute(cmd)
        migration_files = [filename.split("/")[-1] for filename in migration_files_path]
        return migration_files


if __name__ == "__main__":
    args = sys.argv[1:]
    migrate = Migrate()
    func = getattr(migrate, args[0], False)
    if func:
        func(*args[1:])
    else:
        print("Not found")
