#!/bin/bash 


 sed 's/'"$1"'.css/..\/..\/assets\/css\/'"$1"'.css/g' index.html > $1/index.html
