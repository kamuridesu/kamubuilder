from parser import popen
import subprocess
import os


def java(path, filename, *args):
    # basename for the class execution
    file_basename = os.path.basename(filename)  # we need to get basename with basename() function
    # as the full path of the file can be also passed if you're using sublime text
    file_classname = file_basename.split(".")
    file_classname = "".join(file_classname[:len(file_classname) - 1])
    #compile
    if popen("javac", *args, filename) == 0:
        #run
        # the reason for using call() instead of Popen() is because i'm lazy to get
        # two commands running on Popen at same time, eg: 'x && y'
        subprocess.call(f"cd {path} && java {file_classname}", shell=True)