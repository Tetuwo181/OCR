# -*- coding: utf-8 -*-
from keras.models import Sequential  
from keras.layers.core import Dense, Activation  
from keras.layers.recurrent import LSTM
import json
import os


class WordConverter(object):
    def __init__(self, word2num:dict):
        index = 1
        self.__word2num = word2num
        
    def letter2num(self, letter):
        if letter in self.__word2num:
            return self.__word2num[letter]
        return 0
    
    def sentence2indexlist(self, sentence):
        return [self.letter2num(letter) for letter in sentence]
    
    def recordIndex(self, output_path:str = os.path.join(os.getcwd(), "word_data"), file_name:str = "file_default.json"):
        file_path = os.path.join(output_path, file_name)
        with open(file_path, "w"):
            json.dump(self.__word2num)

def build_word_converter_from_sentences(sentence_list)->WordConverter:
    index = 1
    word2num = {}
    for sentence in sentence_list:
        for letter in sentence:
            if letter not in word2num:
                word2num[letter] = index
                index = index + 1
    return WordConverter(word2num)


def build_word_converter_from_recorded(recorded_path:str)->WordConverter:
    with open(recorded_path, "r") as recorded_json:
        recorded_data = json.load(recorded_json)
    return WordConverter(recorded_data)
      

def build_LSTM(conf):
    input_shape = (conf[""])
    LSTM(conf["hidden_neurons"], batch_input_shape=(None, length_of_sequences, in_out_neurons), return_sequences=False)

def build_model(conf):
    model = Sequential()
    model.add()