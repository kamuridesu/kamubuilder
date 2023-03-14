from src.parsers import popen
import os


def getIncludes(filename: str) -> list:
    libraries = []
    with open(filename, "r") as file:
        includes = [x.strip("\n") for x in file.readlines()]
        for include in includes:
            if include.startswith("#include"):
                name = include.split("<")[1].split(">")[0]
                libraries.append(name)
    linkers = []
    if "math.h" in libraries:
        linkers.append("-lm")
    return linkers


def cLang(path: str, filename: str, *args) -> int:
    linkers = getIncludes(filename)
    file_basename = os.path.basename(filename)
    file_basename = file_basename.split(".")
    file_basename = "".join(file_basename[: len(file_basename) - 1])
    if file_basename[0] == "/" or file_basename[0] == "\\":
        file_basename = file_basename[1:]
    if popen("gcc", "-o", file_basename, *linkers, *args, filename) == 0:
        return popen(os.path.join(path, file_basename))
