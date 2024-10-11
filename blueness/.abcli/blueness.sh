#! /usr/bin/env bash

function blueness() {
    local task=$(abcli_unpack_keyword $1 help)

    if [ $task == "help" ]; then
        blueness upgrade "$@"
        blueness version
        return
    fi

    if [ $task == "upgrade" ]; then
        local module
        for module in blueness \
            blue_options \
            blue_objects \
            blue_geo \
            notebooks_and_scripts; do
            pip install --upgrade $module
        done
        return
    fi

    abcli_generic_task \
        plugin=blueness,task=$task \
        "${@:2}"
}
