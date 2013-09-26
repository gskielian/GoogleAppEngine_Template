#!/bin/bash 

#ran this script in a bash for loop to change the paths for the local .css file in the index.html of each example

 sed 's/'"$1"'.css/..\/..\/assets\/css\/'"$1"'.css/g' index.html > $1/index.html
