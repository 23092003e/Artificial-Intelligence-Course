import pandas as pd
import numpy as np
import sys

class NaiveBayesFilter:
    def __init__(self):
        self.data = []
        self.vocabulary = []  # returns tuple of unique words
        self.p_spam = 0  # Probability of Spam
        self.p_ham = 0  # Probability of Ham
        # Initiate parameters
        self.parameters_spam = {unique_word: 0 for unique_word in self.vocabulary}
        print('parameters_spam: ', self.parameters_spam)
        self.parameters_ham = {unique_word: 0 for unique_word in self.vocabulary}
        print('parameters_ham: ', self.parameters_spam)

    def fit(self, X, y):
        "*** YOUR CODE HERE ***"
        return self.data

    def predict(self, X):
        prob = []
        "*** YOUR CODE HERE ***"
        return prob

    def predict_proba(self, X):
        proba = []
        "*** YOUR CODE HERE ***"
        return proba

    def score(self, true_labels, predict_labels):
        recall = 0
        "*** YOUR CODE HERE ***"
        return recall

