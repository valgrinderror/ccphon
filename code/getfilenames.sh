#!/bin/sh

FILE='../data/filelists/chuci_CTXT.txt'
for file in ../data/raw_text/Chuci/CTXT/*; do
echo ${file##*/}
done > $FILE

FILE='../data/filelists/chuci_scripta.txt'
for file in ../data/raw_text/Chuci/scripta_sinica/*; do
echo ${file##*/}
done > $FILE

FILE='../data/filelists/shijing_CTXT.txt'
for file in ../data/raw_text/Shijing/CTXT/*; do
echo ${file##*/}
done > $FILE

FILE='../data/filelists/testfiles.txt'
for file in ../data/test/*; do
echo ${file##*/}
done > $FILE
