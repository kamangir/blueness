#! /usr/bin/env bash

function blueness() {
    abcli_blueness "$@"
}

function abcli_blueness() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "upgrade" ]; then
        local module
        for module in blueness \
            blue_options \
            blue_objects \
            blue_geo \
            blueflow \
            abcli; do
            pip install --upgrade $module
        done
        return
    fi

    abcli_generic_task \
        plugin=blueness,task=$task \
        "${@:2}"
}
