#!/bin/bash

cd $(dirname "$0")

mkdir build
echo "pdflatex..."
pdflatex --output-directory=build main.tex > /dev/null
echo "biber..."
biber --output-directory=build main > ./build/biber.log
echo "pdflatex..."
pdflatex --output-directory=build main.tex > /dev/null
echo "pdflatex..."
pdflatex --output-directory=build main.tex > ./build/pdflatex.log