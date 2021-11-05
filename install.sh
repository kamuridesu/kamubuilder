git clone https://github.com/kamuridesu/kamubuilder.git ~/.config/kamubuilder

if which vim 2>&1 > /dev/null; then
	echo "map <F2> :w <CR>:!python3 ~/.config/kamubuilder/main.py %<CR>" >> ~/.vimrc
fi
if which nvim 2>&1 > /dev/null; then
	mkdir ~/.config/nvim
	echo "map <F2> :w <CR>:!python3 ~/.config/kamubuilder/main.py %<CR>" >> ~/.config/nvim/init.vim
fi
if which subl 2>/dev/null 1>/dev/null; then
	echo "{\n    \"cmd\": [\"python3\", \"/home/$USER/.config/kamubuilder/main.py\", \"$file\"]\n}" >> ~/.config/sublime-text/Packages/User/kamubuilder.sublime-build
fi
