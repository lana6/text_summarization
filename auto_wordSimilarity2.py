#!/usr/bin/env python


import nltk
import itertools
import math
import networkx as nx
import matplotlib.pyplot as plt


file_variable = open('/home/lana/Documents/text_summarisation/business_papers/airlineIndustry.txt', 'r')

file_lines = []
line = file_variable.readline()

while line != '':
    file_lines.append(line)
    line = file_variable.readline()

tokenize_file_lines = []

for index in file_lines:
   tokenize_file_lines.append(nltk.word_tokenize(index))


for index in tokenize_file_lines:
    print index
    print "" # todo 20th June 2012 - take out any comma's full stops abreviations etc....

total_common_words = []
weighted_sen = []
cnt = 1
cnt2 = 2
element_names = []
tot_element_names = []
ele = []
ele2 = []
for l1, l2 in itertools.combinations(tokenize_file_lines, 2): # two lists are chosen, l1 and l2 catches the lists
    common_words = [] 
    ele = [] # create a new list
    ele.append(l1)
    if not ele2:   
       ele2 = [] + ele 
    for e1, e2 in itertools.product(l1, l2): # a cartian product of all the words is produced, e1 and e2 catches the elements 
      if e1 == e2:
        common_words.append(e1) 
    total_common_words.append(common_words)
    #wight = len(set(common_words)) / (math.log(len(l1),10) + math.log(len(l2),10))
    #weighted_sen.append(wight)
    element_names = [] # create a new list 
    if ele != ele2:
      cnt +=1
      cnt2 = cnt + 1
      ele2 = []    
    #if wight != 0.0:
     #   element_names.append(cnt)
      #  element_names.append(cnt2)       
       # cnt2+=1    
    #tot_element_names.append(element_names)

#print total_common_words



