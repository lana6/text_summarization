#!/usr/bin/env python

from __future__ import division  
import itertools
import copy 
#from itertools import *
import decimal
import re
import math
import nltk
from nltk.corpus import stopwords


file_variable = open('/home/lana/Documents/text_summarisation/business_papers/airlineIndustry.txt', 'r')
#file_variable = open('/home/lana/Documents/text_summarisation/business_papers/tv_for_the_blind.txt', 'r')

file_lines = []
line = file_variable.readline()
out = []

while line != '':        
    file_lines.append(line)
    line = file_variable.readline()

refined_file_lines = []

# \w+ is a regular expression, it transfers the data into letters, digits and underscore. Removes everything else.

for sentence in file_lines: # For characters such as letters, digits and underscore only
    index = file_lines.index(sentence)
    if re.findall(r"\w+",file_lines[index]):# \w+ identifies only letters, digits and underscore.
        refined_file_lines.append(re.findall(r"\w+",file_lines[index]))

file_len = len(refined_file_lines)
file_document = []

for i in range(0, file_len): # Creates bag of words.
   file_document = file_document + refined_file_lines[i]

sorted_file_document = sorted(set(file_document)) # Sorting bag of words into unique words and alphabetical order
x = len(sorted_file_document)
#cnt = 0

vector_dot_product = []
weighted_sentence = []
for i in range(0, len(refined_file_lines) + 1): # Initializing weighted_sentence and vector_dot_product     
     weighted_sentence.append([i,0])
     vector_dot_product.append([i,0])

# Create query sentence.

stopwords = stopwords.words('english')

content = []
for w in file_document: 
    if w.lower() not in stopwords:             
         content.append(w)

fdist = nltk.FreqDist(content)
vocabulary = fdist.keys()
query_sentence = vocabulary[:15]
query_sentence_len = len(query_sentence)


# Create weighted sentences


temp_word_list = {}
#test = 0
test2 = 0
flag = "negative"
#cnt_sen = 0
sen_position = len(refined_file_lines) + 1
query_flag = "negative"
weighted_query = 0



for i in range(0,x):   
  temp_word_list = {}
  sub_test = 0
  for sen in range(0, len(refined_file_lines)):
    cnt_sen = sen    
    query_flag = "negative"
    cnt = sen
    test = 0 
    for word in refined_file_lines[sen]:
         if sorted_file_document[i] == word and sen == cnt:            
             test +=1
             if sorted_file_document[i] == word:                
                 temp_word_list[sen+1] = test 
  if (math.log(len(temp_word_list.keys()),10)) != 0:  
      sub_test = round((math.log(len(refined_file_lines),10)),5) / round((math.log(len(temp_word_list.keys()),10)),5)                   
      for m in range(0, sen_position):
       if temp_word_list.has_key(m):       
        temp = weighted_sentence[m][1]
        temp2 = sub_test * temp_word_list[m]
        pow_2 = pow(temp2,2)  # weighted word times by the power of two    
        weighted_sentence[m][1] = temp + pow_2

  if query_flag == "negative" and fdist.freq(sorted_file_document[i]) > 0:
      temp_sub_test = pow(sub_test,2)                           
      weighted_query = weighted_query + temp_sub_test 
      query_flag = "positive"
      for x in range(0, sen_position): #Creates the dot product between to vectors, query and sentence, based on word in query
       if temp_word_list.has_key(x):       
        temp = vector_dot_product[x][1]
        vector_dot_product[x][1] = temp + ((sub_test * temp_word_list[x])*sub_test)

# Calculate vector lengths for each sentence and query

weighted_sentence_len = len(weighted_sentence)

for n in range(0, weighted_sentence_len):
    weighted_sentence[n][1] = math.sqrt(weighted_sentence[n][1])
   

weighted_query = math.sqrt(weighted_query)

    
# Calculate the similarity between the query and the individual sentences.

for c in range(0, weighted_sentence_len):
  if (weighted_sentence[c][1] * weighted_query) != 0:
    temp_sim =  vector_dot_product[c][1] / (weighted_sentence[c][1] * weighted_query)
    weighted_sentence[c][1] = temp_sim

weighted_sentence.sort(lambda x, y,: cmp(y[1],x[1]))

print weighted_sentence

for b in range(0 , weighted_sentence_len):
    print weighted_sentence[b]
    print ""
    temp_line = weighted_sentence[b][0]
    if temp_line != 0:
      print refined_file_lines[temp_line - 1]







