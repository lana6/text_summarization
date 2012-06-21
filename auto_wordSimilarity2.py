#!/usr/bin/env python


#import nltk
import itertools
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


#tokenize_file_lines = []

#for index in file_lines: 
 #  tokenize_file_lines.append(nltk.word_tokenize(index))

refined_file_lines = []

for sentence in file_lines: # For characters such as letters, digits and underscore only
    index = file_lines.index(sentence)
    if re.findall(r"\w+",file_lines[index]):# \w+ identifies only letters, digits and underscore.
        refined_file_lines.append(re.findall(r"\w+",file_lines[index]))

#tokenize_file_lines = []

#for index in refined_file_lines: 
  # tokenize_file_lines.append(nltk.word_tokenize(index))

total_common_words = []
weighted_sen = []
ele_name = []
tot_element_names = []
#print refined_file_lines
#print ""
#if not tokenize_file_lines[1]:
  # print "this list is empty"
 #  print tokenize_file_lines[1]
   #del tokenize_file_lines[1]
#print ""
#print ""
#print tokenize_file_lines[1]
#print ""
#print ""
#refind = re.findall(r"\w+",file_lines[2])
#print refind
#print ""
#print ""
for w1, w2 in itertools.combinations(refined_file_lines, 2): 
   common_words = []
   index1 = refined_file_lines.index(w1) + 1
   index2 = refined_file_lines.index(w2) + 1
   for e1, e2 in itertools.product(w1, w2):
      if e1 == e2:  
        common_words.append(e1)
   total_common_words.append(common_words)
   wight = len(set(common_words)) / (math.log(len(w1),10) + math.log(len(w2),10))
   weighted_sen.append(wight)
   ele_name = [] # create a new list  
   if wight != 0.0:
       ele_name.append(index1)
       ele_name.append(index2)  
   if ele_name:
     tot_element_names.append(ele_name)
  # print ""
  # print ""
  # print tot_element_names 

print total_common_words
print weighted_sen
print tot_element_names


print ""
print ""


G = nx.Graph()


for index in range(len(file_lines)):
    var = "S" + str(index + 1)
    G.add_node(var)

#print G.nodes()

for index in range(len(tot_element_names)):
   #  if tot_element_names[index]:
    #   print tot_element_names[index]     
     if tot_element_names[index]:
       var = 'S' + str(tot_element_names[index][0])
       var1 = 'S' + str(tot_element_names[index][1])
       G.add_edge(var,var1)

print ""
print ""      
print G.edges()
print ""
print ""
print G.nodes()

nx.draw_circular(G)

plt.show()
print ""
print ""
print nx.pagerank(G)



















##for l1, l2 in itertools.combinations(tokenize_file_lines, 2): # two lists are chosen, l1 and l2 catches the lists
  ##  common_words = []     
   ## index1 = tokenize_file_lines.index(l1) + 1
   ## print "l1", l1
   ## print ""
    ##print ""
    ##print "l2" , l2
    ##index2 = tokenize_file_lines(l2) + 1
    ##for e1, e2 in itertools.product(l1, l2): # a cartian product of all the words is produced, e1 and e2 catches the elements 
     ## if e1 == e2:
       ## common_words.append(e1) 
    ##total_common_words.append(common_words)
    #wight = len(set(common_words)) / (math.log(len(l1),10) + math.log(len(l2),10))
    #weighted_sen.append(wight)
    #ele_name = [] # create a new list 
    #if wight != 0.0:
     #   ele_name.append(index1)
      #  ele_name.append(index2)       
       # cnt2+=1    
    #tot_element_names.append(ele_name)

##print total_common_words



