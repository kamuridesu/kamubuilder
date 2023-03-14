from src.parsers import popen
import os


def cppLang(path: str, filename: str, *args) -> int:
    file_basename = os.path.basename(filename)
    file_basename = file_basename.split(".")
    file_basename = "".join(file_basename[: len(file_basename) - 1])
    if file_basename[0] == "/" or file_basename[0] == "\\":
        file_basename = file_basename[1:]
    targ_path = os.path.join(path, file_basename)
    if popen("g++", "-o", targ_path, *args, filename) == 0:
        return popen(targ_path)
