from parser import popen


def php(path, filename, *args):
    return popen("php", *args, filename)