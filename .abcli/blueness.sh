#! /usr/bin/env bash

function blueness() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        blueness version
        return
    fi

    if [ "$task" == "init" ]; then
        abcli_init blueness "${@:2}"
    fi

    if [[ "|pylint|pytest|test|" == *"|$task|"* ]]; then
        abcli_${task} plugin=blueness,$2 \
            "${@:3}"
        return
    fi

    if [[ "|pypi|" == *"|$task|"* ]]; then
        abcli_${task} "$2" \
            plugin=blueness,$3 \
            "${@:4}"
        return
    fi

    python3 -m blueness "$@"
}

abcli_log $(blueness version --show_icon 1)
