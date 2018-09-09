#!/usr/bin/python
# -*- coding: UTF-8-*-
import sys
import analyze_sound
import json
import markup
import write_dummy

# kernsheet.py
#
# The main module for this phonology project.

__author__="John O'Leary <jo.10@princeton.edu>"
__date__ ="Last Updated: Aug 30, 2018"

def usage():
    print """
        python kernsheet.py [text_to_markup.txt] [text_type]
        """

#the input poem
text = []

#initialize dictionaries
schuessler = {}
baxter_sagart = {}
dummys = {}
tags = {}

try:
    
    dummy_dict = analyze_sound.load_dummydict()
    dummy_initgroups = analyze_sound.load_dummyinit()
    schuessler_dict = analyze_sound.load_schuesslerdict()
    markup.kernmarkup(sys.argv[1], dummy_dict, dummy_initgroups, schuessler_dict, sys.argv[2])

except UnicodeEncodeError:
    print('unicode encoding error')

except IOError:
    sys.stderr.write("ERROR: Cannot read inputfile.\n")
    sys.exit(1)
