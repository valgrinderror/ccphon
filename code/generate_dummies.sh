#!/bin/sh

LIST="../data/filelists/chuci_CTXT.txt"
while read line
do
    FILE="$line"
    python main.py $FILE 1
done < $LIST

LIST="../data/filelists/chuci_scripta.txt"
while read line
do
    FILE="$line"
    python main.py $FILE 2
done < $LIST

LIST="../data/filelists/shijing_CTXT.txt"
while read line
do
    FILE="$line"
    python main.py $FILE 3
done < $LIST

LIST="../data/filelists/testfiles.txt"
while read line
do
FILE="$line"
python main.py $FILE 0
done < $LIST
