from parser import popen


def python(path, filename, *args):
    return popen("python", *args, filename)