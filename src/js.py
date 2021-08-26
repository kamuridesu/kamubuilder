from parser import popen


def js(path, filename, *args):
    return popen("node", *args, filename)