from src.parsers import popen


def shell(path: str, filename: str, *args) -> int:
    return popen("sh", *args, filename)
