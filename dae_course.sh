#!/bin/bash

for i in {1..15}
do
  folder="week$i"
  mkdir "$folder"
  echo "# Week $i Read Me" > "$folder/readme.md"
done
