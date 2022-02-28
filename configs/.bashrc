# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

alias ls='ls -aFl --color=auto --time-style=long-iso'

export prompt="`uname -n`:${cwd}> "

export PS1="\u@\h:\w>"

#export http_proxy=http://proxy.cse.cuhk.edu.hk:8000/
#export https_proxy=https://proxy.cse.cuhk.edu.hk:8000/
#export https_proxy=http://proxy.cse.cuhk.edu.hk:8000/
#export ftp_proxy=http://proxy.cse.cuhk.edu.hk:8000/

# export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib:/usr/lib64"
# export LIBRARY_PATH="$LD_LIBRARY_PATH"

#export SCRIPT=
