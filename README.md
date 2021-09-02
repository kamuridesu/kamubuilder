# kamubuilder

This is a parser for build for differents languages.

Can be used with VIM, NEOVIM or Sublime Text 3. The implementation on those editors are: run the file and pass the filename as argument, for example, in VIM/NEOVIM:

    map <F2> :w <CR>:!python ~/.main.py %<CR>

We also have the args parameter, that can be passed to any compiler or interpreter like:
`cLang(path, filename, "-lm")`

## Currently supported languages
- Python (using Python standard interpreter)
- PHP (using PHP standard interpreter)
- JavaScript (NodeJs, npm support soon i think)
- Java (using javac and java commands, tested on OpenJDK and Oracle JDK)
- C (using GCC)
- C++ (using G++)
- Rust (using rustc with Cargo support)
- Shell (using Bourne shell, sh)
- Pascal (using FPC)

If you want to contribute and add support to more languages, feel free to do pull requests.

# Further notes
I've decided to separate each function to a file in case we want to add additional processing like creating a C specific function that searches for includes and chooses what libraries to link, eg, if math is in include, we automatically use the `-lm` (this is already implemented, so we automatically search for the header files and include the libraries needed for the linker).

### Info on Rust builder
If you add `// rust` to the first line of your rust file, it is going to be compiled with `rustc` even if it is on a Cargo project. I've made this because one can choose to test their code without compile the whole project.

Other thing that you'll need to be aware is that if the compiler returns a warning, it is going to be treated as an error by the parser. I do not plan to change this behavior at the moment because it forces you to correct (or at least suppress) the warnings.
