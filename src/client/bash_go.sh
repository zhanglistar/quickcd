#!/bin/zsh
# !!! bash array starts from 0, whereas zsh from 1 !!!
#set -x
go() {
    if [[ $# != 1 ]]; then
        echo "Usage: go dir"
        return 0
    fi
    dirs=( $(python /Users/zhanglistar/Code/quickcd/src/client/client.py $1) )
    cnt=${#dirs[@]}
    if [[ $cnt == 0 ]]; then
        echo "No such directory"
        return
    fi
    if [[ $cnt == 1 ]]; then
        echo "cd to ${dirs[0]}"
        cd ${dirs[0]}
        return 0
    fi
    echo "Select one:"
    for (( i = 0 ; i < $cnt ; i++ )) do
        echo "[$i]: ${dirs[$i]}"
    done
    read index
    while (( $index >= $cnt )) || (( $index < 0 )); do
        echo "Invalid input, again:"
        read index
    done
    echo "cd to ${dirs[$index]}"
    cd ${dirs[$index]}
}

#go $1
