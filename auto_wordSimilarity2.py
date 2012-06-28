#!/usr/bin/env python

from __future__ import division  
import itertools
import copy 
#from itertools import *
import decimal
import re
import math
import networkx as nx
import matplotlib.pyplot as plt


file_variable = open('/home/lana/Documents/text_summarisation/business_papers/airlineIndustry.txt', 'r')

file_lines = []
line = file_variable.readline()

while line != '':
    file_lines.append(line)
    line = file_variable.readline()


refined_file_lines = []


# \w+ is a regular expression, it transfers the data into letters, digits and underscore. Removes everything else.

for sentence in file_lines: # For characters such as letters, digits and underscore only
    index = file_lines.index(sentence)
    if re.findall(r"\w+",file_lines[index]):# \w+ identifies only letters, digits and underscore.
        refined_file_lines.append(re.findall(r"\w+",file_lines[index]))

number_sentences = len(refined_file_lines)
total_common_words = []
weighted_sen = []
ele_name = []
tot_element_names = []

# Looks at each pair of sentences and checks for similar words. For each pair of sentences with similar words a 
# weight is created.

for w1, w2 in itertools.combinations(refined_file_lines, 2): 
   common_words = []
   index1 = refined_file_lines.index(w1) + 1
   index2 = refined_file_lines.index(w2) + 1
   for e1, e2 in itertools.product(w1, w2):
      if e1 == e2:  
        common_words.append(e1)
   total_common_words.append(common_words)
   #w1_len_Decimal = decimal.Decimal(len(w1))
   #w2_len_Decimal = decimal.Decimal(len(w2))
   #wight = len(set(common_words)) / w1_len_Decimal.log10() + w1_len_Decimal.log10()
   wight = len(set(common_words)) / (math.log(len(w1),10) + (math.log(len(w2),10)))   
   weighted_sen.append(wight)
   ele_name = [] # create a new list  
   if wight != 0.0:
       ele_name.append(index1)
       ele_name.append(index2)
       ele_name.append(wight)      
   if ele_name: # Only do if ele_name is not empty
     tot_element_names.append(ele_name)

# Begin to create PageRank

#1 create multi-dimentional list. Each list begins with a new sentence ie [[[1,3,1.77],[1,7,098]],[[2,4,1.33],[2,6,0.77]]]
#using tot_element_names list. 


grouped_nodes= []
tot_grouped_nodes = []
var = 1
## this algorithm assumes that triplets of tot_element_names with the same first element/node 
## are next to each other in tot_element_names
for (i,j,x) in tot_element_names:   
    if var == i:
        grouped_nodes.append([i,j,x]) # linked nodes with with weights info, grouped by [index][0](sentence)
    else:
        tot_grouped_nodes.append(grouped_nodes) # Allows each sentence list to be separated
        grouped_nodes = []
        grouped_nodes.append([i,j,x])
        var = i
## final grouped_nodes has not yet been appended, so do it now
tot_grouped_nodes.append(grouped_nodes)


# Each list group created above needs to contain lists of a11 nodes linked to it.  This function appends linked lists where necessary 
# A copy of tot_grouped_nodes is created as appending lists to the original. A static list is needed in function.


cpy_grouped_nodes = []
cpy_grouped_nodes = copy.deepcopy(tot_grouped_nodes) # Copy of original created
var_len = len(cpy_grouped_nodes)
flag = 0
i3 = len(tot_grouped_nodes)
for i in range(0, var_len):
    for j in range(0, len(cpy_grouped_nodes[i])):
        flag = 0
        temp_list = cpy_grouped_nodes[i][j] # Identifies list to be copied
        temp_list2 = [[temp_list[1],temp_list[0],temp_list[2]]]
        endnode = cpy_grouped_nodes[i][j][1]
        for i2 in range(0, var_len): # first check original groups
            if endnode == cpy_grouped_nodes[i2][0][0]:
                tot_grouped_nodes[i2].extend(temp_list2) # List appended to group
                flag =  1 # indicate that the matching group has been found
                break
        if flag == 0: # if we didn't find a matching group in the original groups check the new groups
            for i4 in range(i2+1,i3): 
                if endnode == tot_grouped_nodes[i4][0][0]:
                    tot_grouped_nodes[i4].extend(temp_list2) # List appended to group
                    flag = 1 # indicate that the matching group has been found
                    break
        if flag == 0: # if we didn't find a matching group in the original or new groups we need to create a new group
            tot_grouped_nodes.extend([temp_list2])
            i3 += 1
# For each node add up all the weighted linked values connected to it and save total to respective list.

cpy_grouped_nodes = []
cpy_grouped_nodes = copy.deepcopy(tot_grouped_nodes) # Copy of original created
var_len = len(cpy_grouped_nodes)
sum_weights = 0
list_index = 0

for i in range(0, var_len):  
  for j in range(0, len(cpy_grouped_nodes[i])): 
    sum_weights = 0
    for i2 in range(0, var_len):
     for j2 in range(0, len(cpy_grouped_nodes[i2])):
        if cpy_grouped_nodes[i][j][1] == cpy_grouped_nodes[i2][j2][0]:                  
           sum_weights = sum_weights + cpy_grouped_nodes[i2][j2][2]        
    tot_grouped_nodes[i][j].append(sum_weights)    
  list_index +=1  


# Set the initial score for each sentence. ie (1 - d) where d is the damping factor of 0.85

str_damping_factor = str(0.15)
d = decimal.Decimal(str_damping_factor)
sentence_score = [1,1,1,0.15]
#sentence_score.append([0.15]) 

for i in tot_grouped_nodes:
   i.extend([sentence_score])


# Evaluate ranks for sentences

cpy_grouped_nodes = []
cpy_grouped_nodes = copy.deepcopy(tot_grouped_nodes) # Copy of original created
var_len = len(cpy_grouped_nodes)
sum_weights = 0
list_index = 0
flag = "negative"
sub_score = 0.0000
tot_score = 0.0000

for i in range(0, var_len):
   tot_score = 0
   sub_score = 0
   for j in range(0, len(cpy_grouped_nodes[i])): 
     for i2 in range(0, var_len):
         flag = "negative"  
         print flag , "outside i2"
         for j2 in range(0, len(cpy_grouped_nodes[i2])):
           #if cpy_grouped_nodes[i][j] == cpy_grouped_nodes[i2][j2]:
              print flag , "j2"                  
              if flag == "negative":
               decimal_weight1 = cpy_grouped_nodes[i][j][2]
               decimal_weight2 = cpy_grouped_nodes[i][j][3]
               print cpy_grouped_nodes[i][j][2] , "nom" , cpy_grouped_nodes[i][j][3] , "dom" , cpy_grouped_nodes[i][j]
               if decimal_weight2 != 0:
                sub_score = round(decimal_weight1 / decimal_weight2, 6)
                print decimal_weight1 / decimal_weight2 , "direct cal"
                node_len = len(cpy_grouped_nodes[i2])
                previous_score = round(tot_grouped_nodes[i2][node_len - 1][3],6)
                #print tot_grouped_nodes[i2][node_len - 1][3]
                print previous_score , "previous score" , sub_score , "sub_score"
                #print int(previous_score) , "int(previous_score)"
                #sub_score = sub_score * int(previous_score)
                sub_score = sub_score * previous_score 
                print sub_score , "sub_score"
              flag = "positive"
   tot_score += sub_score
   print ""
   print tot_score , "total"
   print ""
   print sub_score , "sub_score2"       
   node_len2 = len(cpy_grouped_nodes[i])  
   tot_grouped_nodes[i][j][3] = tot_score
   





