#!/usr/bin/python
# -*- coding: UTF-8-*-
import sys
import re
import json

# analyze_sound.py
#
# This program contains the methods needed for phonological analysis of Chinese characters.

__author__="John O'Leary <jo.10@princeton.edu>"
__date__ ="Last Updated: Aug 30, 2018"

ignore = tuple(('，'.decode('utf-8'), ' ','．'.decode('utf-8'), '。'.decode('utf-8'), '？'.decode('utf-8'), '、'.decode('utf-8'),'（'.decode('utf-8'),'）'.decode('utf-8'), '；'.decode('utf-8'),' ','\t', '①'.decode('utf-8'),'②'.decode('utf-8'),'③'.decode('utf-8'),'④'.decode('utf-8'),'⑤'.decode('utf-8'),'【'.decode('utf-8'),'】'.decode('utf-8'),'◎'.decode('utf-8'),'〔'.decode('utf-8'),'〕'.decode('utf-8'),'：'.decode('utf-8'),' ', '\n','！'.decode('utf-8'), '「'.decode('utf-8'), '」'.decode('utf-8'),'《'.decode('utf-8'),'》'.decode('utf-8'), '-'.decode('utf-8'), '\r'.decode('utf-8')))

def open_file(file_path, parse_criteria):
    file = open(file_path, "r")
    text= file.read().decode('utf-8')
    lines = re.split(r'%s+' % parse_criteria, text)
    return lines

def get_dummies():
    soundtable_fp = '../data/tables/sound_table.txt'
    data = open_file(soundtable_fp, '\n')
    
    info = []
    
    initgroup_count = 0
    initgroup_dict = {}
    
    dummy_dict = {}
    dummy_list = []

    for line in data:
        chunks = re.split(r'\t', line)
        if len(chunks[0]) > 1:
            initial = initgroup_count
            initgroup_dict[initgroup_count] = chunks[0]
            initgroup_count += 1
        rhyme = chunks[1]
        dummy = chunks[2][0]
        for char in chunks[2]:
            match = 0
            if char != '\r' and char != '-'.decode('utf-8'):
                for unit in dummy_list:
                    if char == unit[0]:
                        match = 1
                        dummy_match = 0
                        for group in unit[1:]:
                            if group[-1] == dummy:
                                dummy_match = 1
                        if dummy_match == 0:
                            unit.append([initial, rhyme, dummy])
                if match == 0:
                    dummy_list.append([char, [initial, rhyme, dummy]])

        for unit in dummy_list:
            dummy_dict[unit[0]] = unit[1:]
    json_dump('dummy_dict', dummy_dict)
    json_dump('dummy_initgroup_dict', initgroup_dict)

def get_schuessler():
    schuessler_fp = '../data/tables/hunter_schuessler_table.txt'
    schuessler_dict = {}
    reconstructions = []
    
    with open(schuessler_fp) as fp:
        lines = open_file(schuessler_fp, '\n')
        line_count = 0
        group_number = 0
        while line_count < len(lines):
            reading_list = []
            char = lines[line_count][0]
            match = 0

            #mark which character is being analyzed in first position of list
            reading_list.append(char)
            readings = lines[line_count][5:-3].split('$')
    
            #connect all readings to character
            for reading in readings:
                reading_list.append(reading)
            
            #check to see if character appears elsewhere in database with other set of readings, if so, append these readings to that list, otherwise append new list as standalone
            for entry in reconstructions:
                if entry[0] == reading_list[0]:
                    entry.append(reading_list[1:])
                    match = 1
            if match == 0:
                reconstructions.append(reading_list)
            
            sys.stdout.write('\rReading Hunter file: %s/%s done.' % (line_count, len(lines)-1))
            sys.stdout.flush()
            line_count += 1

    #populate dictionary with reconstructions for easy retrieval
    for reconstruction in reconstructions:
        schuessler_dict[reconstruction[0]] = reconstruction[1:]

    json_dump('schuessler_dict', schuessler_dict)

def load_dummydict():
    with open('../data/json/dummy_dict.json', "r") as f:
        data = f.read()
    dummy_dict = json.loads(data)
    return dummy_dict

def load_schuesslerdict():
    with open('../data/json/schuessler_dict.json', "r") as f:
        data = f.read()
    schuessler_dict = json.loads(data)
    return schuessler_dict

def load_dummyinit():
    with open('../data/json/dummy_initgroup_dict.json', "r") as f:
        data = f.read()
    dummy_dict = json.loads(data)
    return dummy_dict

def json_dump(file_name, file):
    with open('../data/json/%s.json' % file_name, 'w') as write_file:
        json.dump(file, write_file)

def set_dummytags():
    soundtable_fp = '../data/tables/sound_table.txt'

def dict_printstatus(dict_type, line_count, lines_len):
    if dict_type == 1:
        sys.stdout.write('\rReading Schuessler file: %s/%s done.' % (line_count, lines_len-1))
    elif dict_type == 2:
        sys.stdout.write('\rReading Baxter file: %s/%s done.' % (line_count, lines_len-1))
    sys.stdout.flush()

def get_tags():
    if tag_list == {}:
        set_dummytags()
        return tag_list
    else:
        return tag_list
