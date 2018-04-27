# copy from local machine to remote machine
# scp -i privateky -v localfile user@host:/path/to/whereyouwant/thefile

# copy from remote machine to local machine
# scp user@host:/path/to/remotefile localfile

sudo apt-get update

# install tmux
sudo apt-get install tmux
ln -s dotfiles/.tmux.conf ~/.tmux.conf
ln -s dotfiles/.tmux.conf.local ~/.tmux.conf.local

# install vim
sudo apt -y install vim
ln -s generate.vm ~/.vimrc

# install other libs
sudo apt-get install git curl python-pip python-dev build-essential

pip install -r requirements.txt

# install mitmproxy
sudo apt-get install python-dev
sudo pip install mitmproxy

# install xsspy
git clone https://github.com/faizann24/XssPy/

# load tmux settings
# tmux source-file ~/.tmux.conf
