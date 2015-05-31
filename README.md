# quickcd

## introduction
Blazing fast cd with features as follows:
1. use inverted index structure
2. a c/s architechture
3. local rpc
4. use watchdog monitoring changes

## install
1. clone this repo.
2. add the following line to .zshrc for zsh
    `source $REPO_DIRECTORY/zsh_go.sh`
   or the following for bash
    `source $REPO_DIRECTORY/bash_go.sh` 

3. modify server.conf
4. start server:
    `python server.py`

5. use the command:
    `go $directory`
   to where you want.

Enjoy it!

## TODO
1. sort optimazation
2. add feature of dumping to file and loading from file
3. fuzzy search directory
