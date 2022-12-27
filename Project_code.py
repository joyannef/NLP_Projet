import numpy as np

# Exercise.1
# a.
# P(A|B) = P(AB)/P(B)

# b. Write the function make_trigrams which returns the list of successive triplets from a string of words.

with open ('/Users/jfoster/Documents/PluriTAL/NLP/test_reviews.txt') as test:
    data = test.read()
    x = data.replace ("\n", " ")
    splited = x.split(" ")

def make_trigrams(s):
    trigrams = [s[i: i + 3] for i in range(len(s) - 2)]
    print(trigrams)

print (make_trigrams(splited))

def make_conditional_probas(p):
