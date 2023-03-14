from src.parsers import popen


def julia(path: str, filename: str, *args) -> int:
    return popen("julia", *args, filename)
