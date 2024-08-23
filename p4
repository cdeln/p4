#!/usr/bin/env bash

cmd_regex="record|report"

usage="p4 $cmd_regex [args...]"

if (( $# < 1 )); then
    echo "Missing command"
    echo "Usage: $usage"
    exit 1
fi

cmd=$1

if ! [[ $cmd =~ $cmd_regex ]]; then
    echo "Command $cmd does not match regex $cmd_regex"
    echo "$usage"
    exit 1
fi

cwd=$(dirname ${BASH_SOURCE[0]})
$cwd/p4-$cmd ${@:2}
