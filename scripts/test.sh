#!/bin/bash

### Parte A ###
origin="1 -3"
points=("5 4" "2 3" "-4 3" "-3 1" "-2 -1" "-5 -3" "4 -3" "2 -4")
number_of_points=${#points[@]}

args="$origin\n$number_of_points\n"

for point in "${points[@]}"; do
  args+="$point\n"
done

### Parte B ###
x=2
y=3
time=7

args+="$x\n$y\n$time"

echo -e "$args" | python ../main.py
