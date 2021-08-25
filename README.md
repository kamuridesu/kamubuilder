# kamubuilder


This is a parser for build for differents languages.

Can be used with VIM, NEOVIM or Sublime Text 3. The implementation on those editors are: run the file and pass the filename as argument, for example, in VIM/NEOVIM:

    map <F2> :w <CR>:!python ~/.main.py %<CR>

We also have the args parameter, that can be passed to any compiler or interpreter like:
cLang(path, filename, [-lm])

I've decided to separate each function to a file in case we want to add additional processing like creating a C specific function that searches for includes and chooses what to link, eg, if math is in include, we automatically use the -lm (this is going to be implemented, so we automatically searches for the header files and include the linkers needed.
