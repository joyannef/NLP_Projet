import pprint as pp
from collections import defaultdict
import numpy as np

# Exercise.1
# a.
# P(A|B) = P(AB)/P(B)
# As the Bayes formula indicates, we can calculate the probability of knowing a word from the two previous words with the following logic:
# P(A|B) would represent the probability of knowing a word given the words before it eg. (P(like|w1, w2....wn)).
# This is the probability of the number of times "like" appears given other words in a sentence.
# In this sense, A = like and B = the other words
# We then need to multiply the probabilities of A and B and divide this result by P(B) in order to calculate the probablity of
# knowing a wi given the two words prior (w1, w2).

# b.
# reading model file to calculate proba of words/ sentences
# read with readlines() as strings


wordList = []
tupList = []
templine = []
occurence = defaultdict(list)
val_count = 0


# create trigrams for each line
# appending to a list of tuples
def get_trigrams(sentStr):
    tri_length = 3

    i = 0
    wordList = sentStr.replace('\n', '').replace('.', ' .').split(' ')
    # print(wordList)

    while i < len(wordList) - 2:
        templine = wordList[i: (i + tri_length)]
        tupList.append(tuple(templine))
        i += 1
    print(tupList)


with open("/Users/jfoster/Documents/PluriTAL/NLP/test_reviews.txt") as file:
    rows = file.readlines()
    for row in rows:
        get_trigrams(row)
        print(len(tupList))

''' 
# this should be a function

'''


# c.
# takes each tuple and append to dict
# occurrence represents the count table of each bi-gram

def make_conditional_probas(dict_List):
    for tup in tupList:
        new_key = tup[0:2]
        new_value = {tup[2]: val_count + 1}
        if new_key not in occurence.keys():
            if occurence[new_key] != new_value:
                # new_value = {tup[2] : val_count+1}
                occurence[new_key] = new_value
        else:
            # if new_key already in dict, update it's value (which itself is a dict of one or several elements)
            check_key = occurence[new_key]
            # print(check_key.keys())
            if new_key in occurence:
                if tup[2] in check_key.keys():
                    # then update new_value
                    # print("yes")
                    new_value[tup[2]] += 1
                else:
                    new_value.update(check_key)

                occurence[new_key] = new_value

    for k, v in occurence.items():
        # total occurence of bi_gram = dividor
        dividor = (sum(v.values()))
        for ele in v:
            # replacing count by proba
            # occurence of tri_gram = v[ele] = divident, for each element of v
            v[ele] = round((v[ele] / dividor), 2)

    pp.pprint(occurence)
    print(len(occurence))

print(make_conditional_probas(occurence))


# d.
# Since we are calculating the probability of a word considering the two words before it,
# we need two words at the beginning of each sentences, to indicate the probability of
# which word should be at the beginning of the sentence. Thus, given that the indicators of the beginning
# of a sentence are " 'BEGIN' 'NOW' ", we can observe, which word is likely to start the sentence of a review.

# Exercise 2.

def sample_from_discrete_distrib(distrib):
    words, probas = zip(*distrib.items())
    probas = np.asarray(probas).astype('float64')/np.sum(probas)
    return np.random.choice(words, p=probas)

# 2.1
#In order to initialize this, we could append the results obtained as items in a list.

# 2.2
def generate ():
    print_list = []

    for k, v in occurence.items():
        print_list.append(sample_from_discrete_distrib(v))

    print(' '.join(print_list))

    print(sample_from_discrete_distrib(occurence))

print (generate())

# Some of the sentences obtained from the algorithm were the following:
# "I like chocolate ice-cream . END not like chocolate . END"
# "I like chocolate pudding . END not like chocolate . END"
# "I do chocolate pudding . END not like chocolate . END"
# The sentences obtained are comprehensible to a point, but we can observe the unnecessary spaces before the
# periods and the fact that the words that follow the period are grammatical but non-sensical. As a remark from question 1.d
# it can also be noted that all sentences start with "I", which proves the hypothesis that the words "BEGIN NOW" serves as a
# purpose to indicate the word that should start each sentence.

#2.3
#To estimate the quality of the sentences, we could compare the generated sentences to the ones provided in the wine_txt file.



