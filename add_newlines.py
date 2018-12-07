#!/usr/bin/python
# -*- coding: UTF-8-*-
import sys
import re

# list_homophogroup.py
#
# This program takes the main table of characters and reconstructions and inserts the Baxter homophone group head after each character, for the sake of comparing organization choices.

__author__="John O'Leary <jo.10@princeton.edu>"
__date__ ="Last Updated: Jun 21, 2018"


def usage():
    print """
        python list_homophogroup.py [sound_table.txt]
        """

homophogroups = []

try:
    
    #miscellaneous characters to be ignored
    punctuation = tuple(('，'.decode('utf-8'), ' ','．'.decode('utf-8'), '。'.decode('utf-8'), '？'.decode('utf-8'), '、'.decode('utf-8'),'（'.decode('utf-8'),'）'.decode('utf-8'), '；'.decode('utf-8'),' ','\t', '①'.decode('utf-8'),'②'.decode('utf-8'),'③'.decode('utf-8'),'④'.decode('utf-8'),'⑤'.decode('utf-8'),'【'.decode('utf-8'),'】'.decode('utf-8'),'◎'.decode('utf-8'),'〔'.decode('utf-8'),'〕'.decode('utf-8'),'：'.decode('utf-8'),' ', '\n','！'.decode('utf-8'), '「'.decode('utf-8'), '」'.decode('utf-8'),'《'.decode('utf-8'),'》'.decode('utf-8')))
    
    #read in arguments
    #read in input file
    input_file_path = '../data/%s' % (sys.argv[1])
    newchar_file_name = '../output/%s_homophogroup.txt' % sys.argv[1][:-4]
    newchar_file = open(newchar_file_name, "w")
    
    #read in master list
    check_db = tuple()
    master_list_path = '../data/baxter.txt'
    with open(master_list_path) as fp:
        master_list = open(master_list_path, "r")
        master_text= master_list.read()
        #break down into homonym groups (single lines in spreadsheet)
        lines = re.split(r'\n+', master_text)
        print len(lines)
        #ignore first line (headers)
        line_count = 1
        group_number = 0
        while line_count < len(lines):
            match = 0
            line_parts = re.split(r'\t+', lines[line_count])
            for group in homophogroups:
                if group[0] == line_parts[1].decode('utf-8'):
                    print 'Match %s' % line_parts[0].decode('utf-8')
                    group.append(line_parts[8].decode('utf-8'))
                    match = 1
                if match == 1:
                    break
            if match == 0:
                print 'New One: %s' % (line_parts[0]).decode('utf-8')
                new_entry = []
                new_entry.append(line_parts[1].decode('utf-8'))
                new_entry.append(line_parts[8].decode('utf-8'))
                homophogroups.append(new_entry)
            line_count +=1

    print 'text processed'

except IOError:
    sys.stderr.write("ERROR: Cannot read inputfile.\n")
    sys.exit(1)
