from src.parsers import popen


def go(path: str, filename: str, *args) -> int:
    return popen("go", "run", *args, filename)
