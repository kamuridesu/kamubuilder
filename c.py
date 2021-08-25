from parser import popen
import os


def cLang(path, filename, args=[]):
    file_basename = os.path.basename(filename)
    file_basename = file_basename.split(".")
    file_basename = "".join(file_basename[:len(file_basename) - 1])
    if file_basename[0] == "/" or file_basename[0] == "\\":
        file_basename = file_basename[1:]
    if popen('gcc', "-o", file_basename, *args, filename) == 0:
        return popen(os.path.join(path, file_basename))