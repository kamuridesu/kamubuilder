from src.parsers import popen
from src.checkDistro import checkDistro


def python(path: str, filename: str, *args) -> int:
    cmd = "python"
    if checkDistro("apt-get") or checkDistro("apt"):
        cmd = "python3"
    return popen(cmd, *args, filename)
