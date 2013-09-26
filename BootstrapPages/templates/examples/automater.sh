#!/bin/bash 


cat "$1/index.html" | sed 's/'$1'.css/..\/..\/assets\/css\/'$1'.css/g'  > $1/index.html.temp

mv $1/index.html.temp $1/index.html
