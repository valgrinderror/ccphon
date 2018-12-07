#!/usr/bin/python
# -*- coding: UTF-8-*-
import sys
import re

# analyze_sound.py
#
# This program analyzes the phonology an input text on the basis of information from a preformatted master list of Chinese characters that has already been read into memory. It then tells the user various phonological features of the text.

__author__="John O'Leary <jo.10@princeton.edu>"
__date__ ="Last Updated: Jun 16, 2018"


def usage():
    print """
        python analyze_sound.py [text_to_check.txt]
        """

#opens a file defined in input, decodes it, and returns an initial parsting
def open_file(file_path, parse_criteria):
    file = open(file_path, "r")
    text= file.read().decode('utf-8')
    #break down into homonym groups (single lines in spreadsheet)
    lines = re.split(r'%s+' % parse_criteria, text)
    return lines

def prepare_readings_string(phonology_dictionary, lookup):
    readings_string = ''
    count = 0
    
    if lookup in phonology_dictionary:
        while count < len(phonology_dictionary[lookup]):
            readings_string = readings_string + '%s' % (phonology_dictionary[lookup][count])
            count += 1
        return readings_string

    else:
        return 'NULL'

try:
    #miscellaneous characters to be ignored
    punctuation = tuple(('，'.decode('utf-8'), ' ','．'.decode('utf-8'), '。'.decode('utf-8'), '？'.decode('utf-8'), '、'.decode('utf-8'),'（'.decode('utf-8'),'）'.decode('utf-8'), '；'.decode('utf-8'),' ','\t', '①'.decode('utf-8'),'②'.decode('utf-8'),'③'.decode('utf-8'),'④'.decode('utf-8'),'⑤'.decode('utf-8'),'【'.decode('utf-8'),'】'.decode('utf-8'),'◎'.decode('utf-8'),'〔'.decode('utf-8'),'〕'.decode('utf-8'),'：'.decode('utf-8'),' ', '\n','！'.decode('utf-8'), '「'.decode('utf-8'), '」'.decode('utf-8'),'《'.decode('utf-8'),'》'.decode('utf-8')))
    
    #various files to be opened for background data
    master_list_path = '../data/sound_table.txt'
    phonology_file_path = '../data/hunter_schuessler_table.txt'
    
    #data storage
    master_chars = []
    reconstructions = []
    reconstruction_dictionary = {}
    
    #read in arguments
    #read in input file
    input_file_path = '../data/%s' % (sys.argv[1])
    reconstruction_file_name = '../output/%s_reconstructions.txt' % sys.argv[1][:-4]
    reconstruction_file = open(reconstruction_file_name, "w")
    
    #read in master list
    
    with open(master_list_path) as fp:
        lines = open_file(master_list_path, '\n')
        line_count = 0
        group_number = 0
        while line_count < len(lines):
            line_parts = re.split(r'\t+', lines[line_count])
            for char in line_parts[2]:
                if char != '-':
                    master_chars.append(char)
            line_count += 1

    #read in Hunter's phonology file
    with open(phonology_file_path) as fp:
        lines = open_file(phonology_file_path, '\n')
        line_count = 0
        group_number = 0
        while line_count < len(lines):
            reading_list = []
            char = lines[line_count][0]
            match = 0
            
            #mark which character is being analyzed in first position of list
            reading_list.append(char)
            readings = re.split(r'|', lines[line_count][1:])
            readings[0] = readings[0][4:]
            readings[-1] = readings[-1][0:-3]
            
            #connect all readings to characer
            for reading in readings:
                reading_list.append(reading)
            
            #check to see if character appears elsewhere in database with other set of readings, if so, append these readings to that list, otherwise append new list as standalone
            for entry in reconstructions:
                if entry[0] == reading_list[0]:
                    entry.append(reading_list[1:])
                    match = 1
            if match == 0:
                reconstructions.append(reading_list)
            
            line_count += 1

        #populate dictionary with reconstructions for easy retrieval
        for reconstruction in reconstructions:
            reconstruction_dictionary[reconstruction[0]] = reconstruction[1:]

    #begin check of input file
    with open(input_file_path) as fp:
            input_raw = open(input_file_path, "r")
            input_text = input_raw.read().decode('utf-8')
            for char in input_text:
                if char not in punctuation:
                    readings = prepare_readings_string(reconstruction_dictionary, char)
                    reconstruction_file.write('%s %s \n' % (char.encode('utf-8'), readings.encode('utf-8')))

    print 'text processed'

except IOError:
    sys.stderr.write("ERROR: Cannot read inputfile.\n")
    sys.exit(1)
