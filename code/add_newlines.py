#!/usr/bin/python
# -*- coding: UTF-8-*-
import sys
import re
import json

# add_newlines.py
#
# This script was written to automatically insert newline files into the complete Chuci and Shijing files.

__author__="John O'Leary <jo.10@princeton.edu>"
__date__ ="Last Updated: Aug 30, 2018"

def get_inputfilepath(poem_file, text_type):
    if text_type == '1':
        file_path = '../data/raw_text/Chuci/CHANT/%s' % poem_file
    elif text_type == '2':
        file_path = '../data/raw_text/Shijing/CHANT/%s' % poem_file
    else:
        file_path = '../data/raw_text/%s' % poem_file
    return file_path

try:

    input_filepath = get_inputfilepath(sys.argv[1], sys.argv[2])
    output_filepath = '../output/dummyplus_%s' % sys.argv[1]
    
    output_file = open(output_filepath, 'w')
    with open(input_filepath) as fp:
        input_raw = open(input_filepath, 'r')
        input_text = input_raw.read().decode('utf-8')
        for char in input_text:
            print char
            output_file.write('%s' % char.encode('utf-8'))
            '''
            towrite = ''
            if char == '。'.decode('utf-8'):
                towrite = '%s\n' % char.encode('utf-8')
                output_file.write(towrite)
            else:
                towrite = '%s' % char.encode('utf-8')
                output_file.write(towrite)
                '''

except UnicodeEncodeError:
    print('unicode encoding error')

except IOError:
    sys.stderr.write("ERROR: Cannot read inputfile.\n")
    sys.exit(1)
