# Standard Libary
import subprocess
from subprocess import PIPE


def popen(*args) -> int:
    # We use primarily subprocess.Popen as a way to execute and retrieve input
    p = subprocess.Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    if err:
        print(err.decode("utf-8"))
        return 1
    print(out.decode("utf-8"))
    return 0
