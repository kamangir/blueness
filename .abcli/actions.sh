#! /usr/bin/env bash

function blueness_action_git_before_push() {
    blueness pypi build
}
