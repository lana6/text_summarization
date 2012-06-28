#!/usr/bin/env python

import itertools
import copy 
from itertools import *
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

for sentence in file_lines: # For characters such as letters, digits and underscore only
    index = file_lines.index(sentence)
    if re.findall(r"\w+",file_lines[index]):# \w+ identifies only letters, digits and underscore.
        refined_file_lines.append(re.findall(r"\w+",file_lines[index]))

total_common_words = []
weighted_sen = []
ele_name = []
tot_element_names = []

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
       ele_name.append(wight)      
   if ele_name: # Only do if ele_name is not empty
     tot_element_names.append(ele_name)

# Begin to create PageRank

#1 create multi-dimentional list. Each list begins with a new sentence ie [[[1,3,1.77],[1,7,098]],[[2,4,1.33],[2,6,0.77]]]

grouped_nodes= []
tot_grouped_nodes = []
var = 1
for (i,j,x) in tot_element_names:   
    index1 = tot_element_names.index([i,j,x]) # current index
    if var == tot_element_names[index1][0]:
     grouped_nodes.append([i,j,x]) # linked nodes with with weights info, grouped by [index][0](sentence)
    if var  != tot_element_names[index1][0]:
        tot_grouped_nodes.append(grouped_nodes) # Allows each sentence list to be separated
        grouped_nodes = []
        grouped_nodes.append([i,j,x])
        var += 1 
grouped_nodes = []  
grouped_nodes.append([i,j,x])
tot_grouped_nodes.append(grouped_nodes)       


# Each list group needs a11 references to connected lists, this function appends linked lists where necessary 
# A copy of tot_grouped_nodes is created as appending lists to it. A static list is needed in function.


cpy_grouped_nodes = []
cpy_grouped_nodes = copy.deepcopy(tot_grouped_nodes) # Copy of original created
var_len = len(cpy_grouped_nodes)
flag = "negative"

for i in range(0, var_len):
  for j in range(0, len(cpy_grouped_nodes[i])):
      for i2 in range(0, var_len):
        flag = "negative"
        for j2 in range(0, len(cpy_grouped_nodes[i2])):
          if cpy_grouped_nodes[i][j][1] == cpy_grouped_nodes[i2][j2][0]:
             if flag == "negative": # Ensures that only one list is copied into the new group
                 temp_list = cpy_grouped_nodes[i][j] # Identifies list to be copied
                 tot_grouped_nodes[i2].extend([temp_list]) # List appened to group
                 flag = "positive" # Closes the door, this list cannot be copied to this group again



# For each node add up all the weighted linked values and save total to respected list


#Using networkx to create a graph of linked nodes

G = nx.Graph()

pos=nx.spring_layout(G)

total_var = []

for index in range(len(file_lines)):
    var = "S" + str(index + 1)
    G.add_node(var)
    total_var.append(var)

for index in range(len(tot_element_names)):
     if tot_element_names[index]:
       var = 'S' + str(tot_element_names[index][0])
       var1 = 'S' + str(tot_element_names[index][1])
       var3 = tot_element_names[index][2]
       G.add_edge(var,var1,{'weight':var3})

print ""
print ""
print G.edges()
print ""
print ""
print G.nodes()

nx.draw_circular(G,node_color='m',node_size=500)

plt.show()
print ""
print ""
print nx.pagerank(G)

pagerank_values = nx.pagerank(G)

print pagerank_values
print ""
print pagerank_values.keys()
print ""
print pagerank_values.values()

for index in pagerank_values:
  print ""
  print index
