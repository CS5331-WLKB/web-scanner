sudo apt-get update

# install tmux
sudo apt-get install tmux

# update the settings
ln -s /media/sf_Documents/dotfiles/.tmux.conf .tmux.conf
ln -s /media/sf_Documents/dotfiles/.tmux.conf.local .tmux.conf.local

# load tmux settings
tmux source-file ~/.tmux.conf

# install nvim
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:neovim-ppa/stable
sudo apt-get install neovim

# setup nvim
sudo apt-get install git exuberant-ctags ncurses-term curl

# install pip
sudo apt-get install python-pip
pip install Scrapy
