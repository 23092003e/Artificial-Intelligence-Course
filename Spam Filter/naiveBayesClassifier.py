import sys

import numpy as np
import pandas as pd


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
        from collections import defaultdict
        word_counts_spam = defaultdict(int)
        word_counts_ham = defaultdict(int)
        spam_messages = 0
        ham_messages = 0
        vocabulary_set = set()

        for message, label in zip(X, y):
            for word in message:
                vocabulary_set.add(word)
                if label == 'spam':
                    word_counts_spam[word] += 1
                else:
                    word_counts_ham[word] += 1
            if label == 'spam':
                spam_messages += 1
            else:
                ham_messages += 1

        total_messages = spam_messages + ham_messages
        self.p_spam = spam_messages / total_messages
        self.p_ham = ham_messages / total_messages

        self.vocabulary = list(vocabulary_set)
        self.parameters_spam = {word: word_counts_spam[word] for word in self.vocabulary}
        self.parameters_ham = {word: word_counts_ham[word] for word in self.vocabulary}

        self.data = [(X[i], y[i]) for i in range(len(X))]

        return self.data

    def predict(self, X):
        prob = []
        "*** YOUR CODE HERE ***"
        for message in X:
            p_spam_given_message = self.p_spam
            p_ham_given_message = self.p_ham

            total_spam_words = sum(self.parameters_spam.values())
            total_ham_words = sum(self.parameters_ham.values())
            vocab_size = len(self.vocabulary)

            for word in message:
                p_word_spam = (self.parameters_spam.get(word, 0) + 1) / (total_spam_words + vocab_size)
                p_word_ham = (self.parameters_ham.get(word, 0) + 1) / (total_ham_words + vocab_size)

                p_spam_given_message *= p_word_spam
                p_ham_given_message *= p_word_ham

            if p_spam_given_message > p_ham_given_message:
                prob.append('spam')
            else:
                prob.append('ham')

        return prob

    def predict_proba(self, X):
        proba = []
        "*** YOUR CODE HERE ***"
        for message in X:
            p_spam_given_message = self.p_spam
            p_ham_given_message = self.p_ham

            total_spam_words = sum(self.parameters_spam.values())
            total_ham_words = sum(self.parameters_ham.values())
            vocab_size = len(self.vocabulary)

            for word in message:
                p_word_spam = (self.parameters_spam.get(word, 0) + 1) / (total_spam_words + vocab_size)
                p_word_ham = (self.parameters_ham.get(word, 0) + 1) / (total_ham_words + vocab_size)

                p_spam_given_message *= p_word_spam
                p_ham_given_message *= p_word_ham

            total = p_spam_given_message + p_ham_given_message
            if total > 0:
                proba.append([p_ham_given_message / total, p_spam_given_message / total])
            else:
                proba.append([self.p_ham, self.p_spam])

        return proba

    def score(self, true_labels, predict_labels):
        recall = 0
        "*** YOUR CODE HERE ***"
        correct = sum(t == p for t, p in zip(true_labels, predict_labels))
        recall = correct / len(true_labels)
        return recall
