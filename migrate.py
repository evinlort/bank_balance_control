#!/usr/bin/env python


import subprocess

print("Migrations here")


def execute(cmd: list):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    out, err = p.communicate()
    rc = p.returncode

    if out:
        out = [line for line in out.decode("utf-8").split("\n") if line]
    if err:
        err = [line for line in err.decode("utf-8").split("\n") if line]
    return rc, out, err


print(execute(["ls", "-lt", "migrations"]))
