#!/bin/bash
clear
FILES="test/*"
FILES1="training/*"
export CLASSPATH=stanford-parser.jar
for f in $FILES
do
    echo "Processing $f file test..."
    java edu.stanford.nlp.process.DocumentPreprocessor $f > $f.tok.txt
    # take action on each file. $f store current file name
done
echo "Traning folder..."
for f in $FILES1
do
    echo "Processing $f file training..."
    java edu.stanford.nlp.process.DocumentPreprocessor $f > $f.tok.txt
# take action on each file. $f store current file name
done