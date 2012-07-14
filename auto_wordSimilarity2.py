#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division  
import itertools
import copy 
import codecs
import re
import math
import networkx as nx
import matplotlib.pyplot as plt


#file_variable = codecs.open('/home/lana/Documents/text_summarisation/business_papers/airlineIndustry.txt', 'r', 'utf-8')
file_variable = codecs.open('/home/lana/Documents/text_summarisation/business_papers/tv_for_the_blind.txt', 'r', 'utf-8')

file_lines = []
line = file_variable.readline()

while line != '':
    line = line.replace('\n', '')
    if line != '':
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
ele_name = []
tot_element_names = []
wight2 = 0.00

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
   wight = len(set(common_words)) / (math.log(len(w1),10) + (math.log(len(w2),10)))   
   wight2 = round(wight,6)   
   ele_name = [] # create a new list  
   if wight != 0.0:
       ele_name.append(index1)
       ele_name.append(index2)
       ele_name.append(wight2)      
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
q3 = len(tot_grouped_nodes)
index_list = []
sentences_scores = {}
# The damping factor (d) is 0.85. Therefore the initial value of a sentence is 1 - d.
initial_score = 0.15
index_done = "negative"
for q in range(0, var_len):
    index_done = "negative"
    for w in range(0, len(cpy_grouped_nodes[q])):
        flag = 0
        temp_list = cpy_grouped_nodes[q][w] # Identifies list to be copied
        temp_list2 = [[temp_list[1],temp_list[0],temp_list[2]]]        
        endnode = cpy_grouped_nodes[q][w][1]
        if index_done == "negative": # Create index for groups. Set up Dictionary for each group, for sentence scores
            index_list.append([cpy_grouped_nodes[q][w][0],q,w])
            sentences_scores[cpy_grouped_nodes[q][w][0]] = initial_score
            index_done = "positive"
        for q2 in range(0, var_len): # first check original groups
            if endnode == cpy_grouped_nodes[q2][0][0]:
                print q2 , "q2"
                tot_grouped_nodes[q2].extend(temp_list2) # List appended to group              
                flag =  1 # indicate that the matching group has been found
                break
        if flag == 0: # if we didn't find a matching group in the original groups check the new groups
            for q4 in range(q2+1,q3):
                print q2 + 1 , "q2"
                print ""
                print q3
                if endnode == tot_grouped_nodes[q4][0][0]:
                    tot_grouped_nodes[q4].extend(temp_list2) # List appended to group                   
                    flag = 1 # indicate that the matching group has been found
                    break
        if flag == 0: # if we didn't find a matching group in the original or new groups we need to create a new group
            tot_grouped_nodes.extend([temp_list2])
            temp = q3 + 1
            index_list.append([temp,q3,0])
            sentences_scores[tot_grouped_nodes[q3][0][0]] = initial_score                     
            q3 += 1
# For each node add up all the weighted linked values connected to it and save total to respective list.

cpy_grouped_nodes = []
cpy_grouped_nodes = copy.deepcopy(tot_grouped_nodes) # Copy of original created
var_len = len(cpy_grouped_nodes)
sum_weights = 0.00
temp_weights = 0.00
#list_index = 0.00

for n in range(0, var_len):  
  for m in range(0, len(cpy_grouped_nodes[n])): 
    sum_weights = 0
    for n2 in range(0, var_len):
     for m2 in range(0, len(cpy_grouped_nodes[n2])):
        if cpy_grouped_nodes[n][m][1] == cpy_grouped_nodes[n2][m2][0]:                  
           temp_weights = cpy_grouped_nodes[n2][m2][2]
           round_temp_weights = round(temp_weights,6)        
           sum_weights = sum_weights + round_temp_weights
    tot_grouped_nodes[n][m].append(sum_weights)    
  #list_index +=1  

# Evaluate ranks for sentences

   
var_len = len(tot_grouped_nodes)
sub_score = 0.0000
current_list_weight = 0.00
temp_var =  0.00
temp_score = 0.00
total_score = 0.00
final_score = 0.00

cnt = 0

while (cnt <= 100):
 for z in range (0, var_len):
    for x in range(0, len(tot_grouped_nodes[z])):
        startNode = tot_grouped_nodes[z][x][0]
        for z2 in range(0, var_len):            
            if startNode == index_list[z2][0]:
              for c in tot_grouped_nodes[index_list[z2][1]]:
                    sub_score += c[2]
            current_list_weight = int(tot_grouped_nodes[z][x][2])                            
            sub_score += current_list_weight
            if sub_score != 0:
             temp_var = tot_grouped_nodes[z][x][2] / sub_score
            temp_score = round(temp_var,6) * sentences_scores[tot_grouped_nodes[z][x][0]]
        total_score += round(temp_score,6)
        sub_score = 0.00
        temp_var = 0.00
        temp_score = 0.00
    final_score = 0.15 + 0.85 * total_score
    #print total_score , "total score"
    sentences_scores[tot_grouped_nodes[z][x][0]] = final_score
    #print tot_grouped_nodes[z][x][0] , " tot_grouped_nodes" , z , "z" , x , "x" , final_score   
    total_score = 0.0000
    final_score = 0.0000 
 cnt +=1

ordered_sentences = {}

ordered_sentences = sorted(sentences_scores.items(), key=lambda x: x[1])
ordered_sentences.reverse()
#print sentences_scores
#print ordered_sentences


summarized_file = open('summarized_file.txt', 'w')


for sen in range(0, len(ordered_sentences)):
   var = ordered_sentences[sen][0]
  # print file_lines[(var - 1)].encode('utf-8')
   #summarized_file.write(refined_file_lines[(var - 1)])
   #summarized_file.write("")
  # print ""
   

#print ""
#print ""
#print file_lines
#summarized_file.write("")
#summarized_file.write("")
#summarized_file.write(file_lines)



           

