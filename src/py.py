from parser import popen


def python(path: str, filename: str, *args) -> int:
    return popen("python", *args, filename)