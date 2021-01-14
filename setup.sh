#!/bin/sh
# To use run with the day and description
# Ex. ./setup.sh 6 snowballs
set -a
source .env
set +a
mkdir "${1}_${2}"
curl https://adventofcode.com/2020/day/${1}/input -H "cookie:${SESSION}" > ${1}_${2}/input.txt
echo "Ready to code!"
