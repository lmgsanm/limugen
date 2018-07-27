# coding=gbk
'''
Created on 2018年7月19日

@author: limugen
'''
import sys
import os

file_data = "merge_input_tfidf_dir.data"
idf_data = "idf.data"
doc_number = 9
keyword = "糊"

file_data_dict = {}
idf_data_dict = {}

def file_open_handler(f):
    lines = open(f,'r',encoding='utf-8')
    return lines

file_data_list = file_open_handler(file_data).read().strip()
idf_data_list = file_open_handler(idf_data).read().strip()
print(idf_data_list)
sys.exit()
for lines in idf_data_list:
    ss = lines.strip().split("\t")
    key,value = ss
    print(key,value)