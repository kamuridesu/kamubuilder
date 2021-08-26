import subprocess
import os
from parser import popen
import pathlib

def rust(path, filename, *args):
    file_basename = os.path.basename(filename)
    file_basename = file_basename.split(".")
    file_basename = "".join(file_basename[:len(file_basename) - 1])
    if file_basename[0] == "/" or file_basename[0] == "\\":
        file_basename = file_basename[1:]
    targ_path = os.path.join(path, file_basename)
    # compile
    if popen("rustc", "-o", targ_path, *args, filename) == 0:
        # run
        return popen(targ_path)


def rsCargo(path, filename, args=[]):
    parent_path = str(pathlib.Path(path).parent.absolute())
    files_in_parent = os.listdir(parent_path)
    if "Cargo.toml" in files_in_parent:
        subprocess.call(f"cd {parent_path} && cargo run", shell=True)
        return True
    return False