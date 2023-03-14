# This is a parser for build for differents languages
# Can be used with VIM, NEOVIM or Sublime Text 3
# The implementation on those editors are:
# run the file and pass the filename as argument
# for example, in VIM/NEOVIM:
# map <F2> :w <CR>:!python3 ~/.config/kamubuilder/main.py %<CR>
# We also have the args parameter, that can be passed to any compiler or interpreter like:
# cLang(path, filename, [-lm])
# i've decided to separate each function to a file in case we want to add additional processing
# like creating a c specific function that searches for includes and chooses what to link, eg, if
# math is in include, we automatically use the -lm.

import sys
import pathlib

# Our processors
from src import (
    cLang,
    cppLang,
    java,
    python,
    rust,
    rsCargo,
    php,
    js,
    shell,
    pascal,
    julia,
    go,
)


def main(args: list) -> None:
    filename = args[0]
    extension = filename.split(".")
    extension = extension[len(extension) - 1]
    path = str(pathlib.Path(filename).parent.absolute())
    is_cargo = rsCargo(path, filename)
    builders = {
        "py": python,
        "rs": rust,
        "c": cLang,
        "cpp": cppLang,
        "java": java,
        "php": php,
        "js": js,
        "sh": shell,
        "go": go,
        "jl": julia,
        "pp": pascal,
        "pas": pascal,
    }
    if not is_cargo:
        builder = builders.get(extension)
        if builder:
            return builder(path, filename)
        raise Exception("Language not recognized or not supported!")


if __name__ == "__main__":
    main(sys.argv[1:])
