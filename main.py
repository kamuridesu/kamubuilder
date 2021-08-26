# This is a parser for build for differents languages
# Can be used with VIM, NEOVIM or Sublime Text 3
# The implementation on those editors are:
# run the file and pass the filename as argument
# for example, in VIM/NEOVIM:
# map <F2> :w <CR>:!python ~/Documents/Programming/build/parser.py %<CR>
# We also have the args parameter, that can be passed to any compiler or interpreter like:
# cLang(path, filename, [-lm])

# i've decided to separate each function to a file in case we want to add additional processing
# like creating a c specific function that searches for includes and chooses what to link, eg, if 
# math is in include, we automatically use the -lm.

import sys
import os
import pathlib

# Our processors
from c import cLang
from cpp import cppLang
from java import java
from py import python
from rs import rust, rsCargo
from php import php
from js import js


def main(args):
    filename = args[0]
    extension = filename.split(".")
    extension = extension[len(extension) - 1]
    path = str(pathlib.Path(filename).parent.absolute())
    # print(filename)
    # print(extension)
    # print(path)
    is_cargo = rsCargo(path, filename)
    if not is_cargo:
        if extension == "py":
            python(path, filename)
        if extension == "rs":
            rust(path, filename)
        if extension == "c":
            cLang(path, filename)
        if extension == "cpp":
            cppLang(path, filename)
        if extension == "java":
            java(path, filename)
        if extension == "php":
            php(path, filename)
        if extension == "js":
            js(path, filename)


if __name__ == "__main__":
    main(sys.argv[1:])