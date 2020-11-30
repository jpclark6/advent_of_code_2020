#!/bin/sh
mkdir "day_${1}"
curl https://adventofcode.com/2019/day/${1}/input -H "cookie: session=${SESSION}" > day_${1}/input.txt
echo "Ready to code!"
