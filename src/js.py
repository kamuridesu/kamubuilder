from src.parser import popen


def js(path: str, filename: str, *args) -> int:
    return popen("node", *args, filename)