#!usr/bin/env python

import nltk
#import pprint
import math
import networkx as nx
import matplotlib.pyplot as plt

s1 = "Businessweeks original purpose was to provide information and opinions as to what was happening in the business world  at the time"

s1_words =  nltk.word_tokenize(s1)

s2 = "Initally the magazine published sections that included topics such as marketing labour finance and management amoung others"

s2_words =  nltk.word_tokenize(s2)

s3 = "Businessweek was first published in September 1929 only weeks before the Stock Market Crash of 1929 the business world was in chaos"

s3_words =  nltk.word_tokenize(s3)


print s1_words
print ""
print len(s1_words)
print ""
print s2_words
print ""
print len(s2_words)
print ""
print s3_words
print ""
print len(s3_words)
print ""

#count = 0
common_words = []

for word in s1_words:
    for wordin in s2_words:
     # print word, wordin
      if word == wordin:
          common_words.append(word)          
         # count += 1
         # print word, wordin, count

common_words_len = len(set(common_words))

# print ""
# print ""
# print count
# print common_words
# print set(common_words)
# common_words_len = len(set(common_words))
# print "" 
# print common_words_len

common_words2 = []

for word in s2_words:
    for wordin in s3_words:     
      if word == wordin:
          common_words2.append(word)          
                
common_words_len2 = len(set(common_words2))


common_words3 = []

for word in s3_words:
    for wordin in s1_words: 
      if word == wordin:
          common_words3.append(word)          
                
common_words_len3 = len(set(common_words3))

print common_words_len3
print common_words_len2
print common_words_len



w12 = common_words_len / (math.log(len(s1_words),10) + math.log(len(s2_words),10))
print ""
print w12
# len-s1_words = 1.32221929473
# len-s1_words = 1.23044892138
# w12 = 1.17524086408
# w12-(with a word count of 2) - 0.783493909384

w23 = common_words_len2 / (math.log(len(s2_words),10) + math.log(len(s3_words),10))
w13 = common_words_len3 / (math.log(len(s1_words),10) + math.log(len(s3_words),10))

print ""
print w23
print ""
print w13

G = nx.Graph()
#G.add_node("a")
#G.add_node("b")
#G.add_node("c")

#G.add_edge(1,2)
#G.add_edge(2,3,{'weight':3.145})

#print G.nodes()
#print ""
#print G.edges()

 # Import the module and instantiate a graph object
 # Add nodes
#G.add_nodes_from(['X','Y','Z'])
#G.add_nodes_from(['A','B','C'])
 # Add edges
#G.add_edge('X','Y',{'weight':1.077})
#G.add_edge('X','Z',{'weight':2.088})
#G.add_edge('A','B',{'weight':0.999})
#G.add_edge('A','C',{'weight':0.155})
#G.add_edge('Y','B',{'weight':0.155})
#G.add_edge('Y','C')
#G.add_edge('Y','A')
#G.add_edge('Y','Z')
#G.add_edge('Y','X')
#G.add_edge('C','X')
#G.add_edge('A','Z')
#G.add_edge('C','B')

G.add_nodes_from([1,2,3])
G.add_edge(1,2,{'weight':w12})
G.add_edge(2,3,{'weight':w23})
G.add_edge(1,3,{'weight':w13})

print ""
print G.nodes()
print G.edges()
nodes = G.nodes()
graph_size = len(nodes)
#graph.incidents
print ""
print graph_size
print ""
print nx.pagerank(G)

#nx.draw(G)
nx.draw_circular(G)

plt.show()
 

 
