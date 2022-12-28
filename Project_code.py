import numpy as np

# Exercise.1
# a.
    # P(A|B) = P(AB)/P(B)
    # As the Bayes formula indicates, we can calculate the probability of knowing a word from the two previous words with the following logic:
    # P(A|B) would represent the probability of knowing a word given the words before it eg. (P(like|w1, w2....wn).
    # This is the probability of the number of times "like" appears given other words in a sentence.
    # In this sense, A = like and B = the other words
    # We then need to multiply the probabilities of A and B and divide this result by P(B) in order to calculate the probablity of 
    # knowing a wi given the two words prior (w1, w2).


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
