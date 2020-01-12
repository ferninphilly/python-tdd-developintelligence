#!/bin/bash
# loop through each lambda directory in each stack.  In each lambda sub directory compile and zip payload.

for dir in $1/*/; 
  do 
    (cd $dir && zip $(basename "$dir").zip $(basename "$dir") && rm $(basename "$dir")); 
  done
