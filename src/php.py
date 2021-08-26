from parser import popen


def php(path: str, filename: str, *args) -> int:
    return popen("php", *args, filename)