#! /usr/bin/env bash

function blueness() {
    local task=$1

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

    bluer_ai_generic_task \
        plugin=blueness,task=$task \
        "${@:2}"
}
