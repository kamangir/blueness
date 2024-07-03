#! /usr/bin/env bash

function blueness() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        blueness version
        return
    fi

    abcli_generic_task \
        plugin=blueness,task=$task \
        "${@:2}"
}
