#!usr/bin/env python

import nltk
import itertools
import math
import networkx as nx
import matplotlib.pyplot as plt


s1 = "Businessweeks original purpose was to provide information and opinions as to what was happening in the business world  at the time"

s1_words =  nltk.word_tokenize(s1)

s2 = "Initally the magazine published sections that included topics such as marketing labour finance and management amoung others"
s2_words =  nltk.word_tokenize(s2)

s3 = "Businessweek was first published in September 1929 only weeks before the Stock Market Crash of 1929 the business world was in chaos"

s3_words =  nltk.word_tokenize(s3)


sentences = []
sentences.append(s1)
sentences.append(s2)
sentences.append(s3)
sen_by_word = []
sen_by_word.append(s1_words)
sen_by_word.append(s2_words)
sen_by_word.append(s3_words)



lst = sen_by_word[1]
lst1 = sen_by_word[1]

#print sen_by_word[0][0] - Businessweek

#index_start = 0
total_common_words = []


#for index in range(len(sen_by_word)):
# # for index2 in range(len(sen_by_word[index])):
 #  # while(sen_by_word[index][index2]):
 #     common_words = []
  #    for word in sen_by_word[index]:
   #    print index
    #   print len(sen_by_word)
     #  if (index + 1) >= len(sen_by_word):
      #      for word in sen_by_word[index_start]:
       #       for wordin in sen_by_word[index]:
        #        if word == wordin:
         #         print word 
          #        common_words.append(word)
           # break
      # for wordin in sen_by_word[index + 1]:
       #     if word == wordin:
        #      print word
         #     common_words.append(word)
          #    print common_words
    #  total_common_words.insert(index,common_words)
     # print total_common_words


#print total_common_words

#for element in itertools.product(*sen_by_word):
    # if element[1] == element[2]:
 #     print element

#result = list(itertools.product(sen_by_word))
print ""
print ""
#print result

weighted_sen = []
#wight = 0

for l1, l2 in itertools.combinations(sen_by_word, 2): # two lists are chosen, l1 and l2 catches the lists
    common_words = []  
    for e1, e2 in itertools.product(l1, l2): # a cartian product of all the words is produced, e1 and e2 catches the elements 
      if e1 == e2:
        common_words.append(e1) 
    total_common_words.append(common_words)
    wight = len(set(common_words)) / (math.log(len(l1),10) + math.log(len(l2),10))
    weighted_sen.append(wight)
 
      
# order with 3 lists, [1,2] [1,3][2,3]

#w12 = common_words_len / (math.log(len(s1_words),10) + math.log(len(s2_words),10))


print total_common_words
print ""
print ""
print weighted_sen

#print itertools.combinations('ABCD', 2)
#print list(itertools.permutations([1,2,3,4],[5,9,8,7] 2))

  
index = 0
common_words = []
#for index in range(len(sen_by_word)):
 # print index
  #for word in sen_by_word[index]:
   # if index + 1 <= len(sen_by_word):
    #  subIndex = index 
     # if subIndex + 1 > len(sen_by_word):
      #   break
      #for wordin in sen_by_word[subIndex + 1]: 
       # if word == wordin:
        #  common_words.append(word)
         # print common_words

#print common_words
