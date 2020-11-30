#!/bin/sh
# To use run with year then day inputs
# Ex. ./setup.sh 2020 5
set -a
source .env
set +a
mkdir "day_${2}"
curl https://adventofcode.com/${1}/day/${2}/input -H "cookie:${SESSION}" > day_${2}/input.txt
echo "Ready to code!"
