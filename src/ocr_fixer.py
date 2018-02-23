# -*- coding: utf-8 -*-
from keras.models import Sequential

class WordConverter(object):
    def __init__(self, sentence_list):
        index = 1
        self.__word2num = {}
        for sentence in sentence_list:
            for letter in sentence:
                if letter not in self.__word2num:
                    self.__word2num[letter] = index
                    index = index + 1
    
    def letter2num(self, letter):
        if letter in self.__word2num:
            return self.__word2num[letter]
        return 0
    
    def sentence2indexlist(self, sentence):
        return [self.letter2num(letter) for letter in sentence]


def build_model(conf):