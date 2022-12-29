# reading model file to calculate proba of words/ sentences 
# read with readlines() as strings 


import pprint as pp 
from collections import defaultdict 
import numpy as np

wordList = []
tupList = []
templine = []
occurence = defaultdict(list)
val_count = 0



#def make_conditional_probas(dict_List):
    


# create trigrams for each line
# appending to a list of tuples 
def get_trigrams(sentStr):
    tri_length = 3
    
    i = 0
    wordList = sentStr.replace('\n','').replace('.', ' .').split(' ')
    #print(wordList)

    while i < len(wordList) - 2:
        templine = wordList[i: (i+tri_length)]
        tupList.append(tuple(templine))
        i += 1
    return tupList    




with open("test_reviews.txt") as file: 
    rows = file.readlines()
    for row in rows:
        get_trigrams(row)
        #print(len(tupList))
    
    
''' 
# this should be a function

'''


#now take each tuple and append to dict
# occurrence represents the count table of each bi-gram
for tup in tupList: 
    new_key = tup[0:2]
    new_value = {tup[2] : val_count+1}
    if new_key not in occurence.keys():
        if occurence[new_key] != new_value:
            #new_value = {tup[2] : val_count+1}
            occurence[new_key]  = new_value
    else:
        #if new_key already in dict, update it's value (which itself is a dict of one or several elements)
        check_key = occurence[new_key]
        #print(check_key.keys())
        if new_key in occurence:
            if tup[2] in check_key.keys():
                #then update new_value
                #print("yes")
                new_value[tup[2]] += 1
            else :
                new_value.update(check_key)

            occurence[new_key]  = new_value


for k, v in occurence.items():
    #total occurence of bi_gram = dividor    
    dividor = (sum(v.values()))
    for ele in v:  
        #replacing count by proba       
        #occurence of tri_gram = v[ele] = divident, for each element of v
        v[ele] = round((v[ele] / dividor), 2)
        

pp.pprint(occurence)
#print(len(occurence))  
    
##### should be end of function  #######


'''
def sample_from_discrete_distrib(distrib):
    words, probas = zip(*distrib.items())
    probas = np.asarray(probas).astype('float64')/np.sum(probas)
    return np.random.choice(words, p=probas)

print_list = []

for k, v in occurence.items():
    print_list.append(sample_from_discrete_distrib(v))

print(' '.join(print_list))


'''




