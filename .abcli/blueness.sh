#! /usr/bin/env bash

function blueness() {
    python3 -m blueness "$@"
}

abcli_log $(blueness version --show_icon 1)
