#!/usr/bin/python
# -*- coding: UTF-8-*-
import sys
import re

# markup.py
#
# This program marks up a Chinese text with phonological information in HTML.

__author__="John O'Leary <jo.10@princeton.edu>"
__date__ ="Last Updated: Aug 30, 2018"

ignore = tuple(('、'.decode('utf-8'), '，'.decode('utf-8'), '\n'.decode('utf-8'), '\r'.decode('utf-8'), '．'.decode('utf-8'), '。'.decode('utf-8'), '？'.decode('utf-8'),'；'.decode('utf-8'), '「'.decode('utf-8'), '」'.decode('utf-8'), '：'.decode('utf-8'), '《'.decode('utf-8'),'》'.decode('utf-8'), '\t', ' ', '（'.decode('utf-8'),'）'.decode('utf-8'),'【'.decode('utf-8'),'】'.decode('utf-8'),'◎'.decode('utf-8'),'〔'.decode('utf-8'),'〕'.decode('utf-8'), '！'.decode('utf-8'), ' '.decode('utf-8'), '\n', '\r'))



def usage():
    print """
        python write_dummy.py [poem]
        """

def get_inputfilepath(text_type, poem_file):
    if text_type == '1':
        file_path = '../data/raw_text/Chuci/CTXT/%s' % poem_file
    elif text_type == '2':
        file_path = '../data/raw_text/Chuci/scripta_sinica/%s' % poem_file
    elif text_type == '3':
        file_path = '../data/raw_text/Chuci/CHANT/%s' % poem_file
    elif text_type == '4':
        file_path = '../data/raw_text/Chuci/CHANT/chuci_parts/%s' % poem_file
    elif text_type == '5':
        file_path = '../data/raw_text/Shijing/CTXT/%s' % poem_file
    elif text_type == '6':
        file_path = '../data/raw_text/Shijing/CHANT/%s' % poem_file
    elif text_type == '7':
        file_path = '../data/raw_text/kernfiles/%s' % poem_file
    else:
        file_path = '../data/test/%s' % poem_file
    return file_path

def get_outputfilepath(text_type, poem_file):
    if text_type == '1':
        file_path = '../output/dummies/Chuci/CTXT/%s_dummy.txt' % poem_file[:-4]
    elif text_type == '2':
        file_path = '../output/dummies/Chuci/scripta_sinica/%s_dummy.txt' % poem_file[:-4]
    elif text_type == '3':
        file_path = '../output/dummies/Chuci/CHANT/%s_dummy.txt' % poem_file[:-4]
    elif text_type == '4':
        file_path = '../output/dummies/Chuci/chuci_parts/%s_dummy.txt' % poem_file[:-4]
    elif text_type == '5':
        file_path = '../output/dummies/Shijing/CTXT/%s_dummy.txt' % poem_file[:-4]
    elif text_type == '6':
        file_path = '../output/dummies/Shijing/CHANT/%s_dummy.txt' % poem_file[:-4]
    elif text_type == '7':
        file_path = '../output/dummies/kern_markup/%s_dummy.txt' % poem_file[:-4]
    else:
        file_path = '../output/dummies/misc_markup/%s_dummy.txt' % poem_file[:-4]
    return file_path

def write_chars(dummy_file, tocheck, dummy_dict):
    for char in tocheck:
        if char in dummy_dict:
            dummy_info = dummy_dict[char]
            #dummy_init = dummy_info[0][0]
            #dummy_rhyme = dummy_info[0][1]
            dummy = dummy_info[0][2]
            dummy_file.write('%s' % dummy.encode('utf-8'))
        else:
            dummy_file.write('%s' % char.encode('utf-8'))

def write_kerndummy(text_type, file_name, dummy_dict):
    inputfilepath = get_inputfilepath(text_type, file_name)
    outputfilepath = get_outputfilepath(text_type, file_name)
    dummy_file = open(outputfilepath, 'w')
        
    #begin check of input file
    with open(inputfilepath) as fp:
            
        input_raw = open(inputfilepath, "r")
        input_text = input_raw.readlines()
        for line in input_text:
            tocheck = line.decode('utf-8')
            if text_type == '3':
                if tocheck[0:7] == '[TITLE]':
                    write_chars(dummy_file, tocheck[7:], dummy_dict)
                elif tocheck[0:10] == '[SUBTITLE]':
                    write_chars(dummy_file, tocheck[10:], dummy_dict)
                else:
                    write_chars(dummy_file, tocheck, dummy_dict)
            else:
                if tocheck[0:9] == '[SECTION]':
                    write_chars(dummy_file, tocheck[9:], dummy_dict)
                elif tocheck[0:12] == '[SUBSECTION]':
                    write_chars(dummy_file, tocheck[12:], dummy_dict)
                elif tocheck[0:6] == '[POEM]':
                    write_chars(dummy_file, tocheck[6:], dummy_dict)
                else:
                    write_chars(dummy_file, tocheck, dummy_dict)
        print '%s dummy written' % file_name

def write_dummy(text_type, file_name, dummy_dict):
    try:
        inputfilepath = get_inputfilepath(text_type, file_name)
        outputfilepath = get_outputfilepath(text_type, file_name)
        dummy_file = open(outputfilepath, 'w')
    
        #begin check of input file
        with open(inputfilepath) as fp:

            input_raw = open(inputfilepath, "r")
            input_text = input_raw.read().decode('utf-8')
            for reading in input_text:
                parts = re.split('\t+', reading)
                char = parts[0]
                if char in dummy_dict:
                    dummy_info = dummy_dict[char]
                    #dummy_init = dummy_info[0][0]
                    #dummy_rhyme = dummy_info[0][1]
                    dummy = dummy_info[0][2]
                    dummy_file.write('%s' % dummy.encode('utf-8'))
                else:
                    dummy_file.write('%s' % char.encode('utf-8'))
        print '%s dummy written' % file_name

    except IOError:
        sys.stderr.write("ERROR: Cannot read inputfile.\n")
        sys.exit(1)
