from src.parser import popen
import os


def pascal(path: str, filename: str, *args) -> int:
    file_basename = os.path.basename(filename)
    file_basename = file_basename.split(".")
    file_basename = "".join(file_basename[:len(file_basename) - 1])
    if file_basename[0] == "/" or file_basename[0] == "\\":
        file_basename = file_basename[1:]
    if popen("fpc", *args, filename) == 0:
        print("##### RESULT #####")
        return popen(os.path.join(path, file_basename))



if __name__ == '__main__':
    pascal("asd", "asd.pas")
