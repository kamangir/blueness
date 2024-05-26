#! /usr/bin/env bash

function blueness_action_git_before_push() {
    [[ "$(abcli_git get_branch)" == "main" ]] &&
        blueness pypi build
}
