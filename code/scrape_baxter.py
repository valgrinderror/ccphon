#!/usr/bin/python
# -*- coding: UTF-8-*-
import sys
import xlrd

# scrape_baxter
#
# This scrapes the Baxter excel file and converts it into a tab-delimited text file.

__author__="John O'Leary <jo.10@princeton.edu>"
__date__ ="Last Updated: Jul 16, 2018"


def usage():
    print """
        python scrape_baxter.py
        """

try:
    
    #prep output file
    output_file_path = '../output/baxter.txt'
    output_file = open(output_file_path, "w")
    
    #read in Baxter file to memory
    check_db = tuple()
    baxter_workbook_name = '../data/SongBenGuangYunMiddleChineseBeta-1.xlsx'
    baxter_workbook = xlrd.open_workbook(baxter_workbook_name, encoding_override='utf-8')
    baxter_data = baxter_workbook.sheet_by_index(0)
    row_count = 0
    char_rows = [1,7,9,11,12,13,14,15]
    while row_count < 25956:
        row = baxter_data.row(row_count)
        row_pos = 0
        for item in row:
            item_text = '%s' % item.value
            if row_pos == len(row)-1:
                output_file.write('%s\n' % item_text.encode('utf-8'))
            
            else:
                output_file.write('%s\t' % item_text.encode('utf-8'))
                row_pos += 1
        sys.stdout.write('\rCopying Baxter file: %s/25955 done.' % row_count)
        sys.stdout.flush()
        row_count += 1

    sys.stdout.write('\n')

    print 'text processed'

except IOError:
    sys.stderr.write("ERROR: Cannot read inputfile.\n")
    sys.exit(1)

