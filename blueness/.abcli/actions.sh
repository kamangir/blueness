#! /usr/bin/env bash

function blueness_action_git_before_push() {
    [[ "$(bluer_ai_git get_branch)" != "main" ]] &&
        return 0

    blueness pypi build
}
