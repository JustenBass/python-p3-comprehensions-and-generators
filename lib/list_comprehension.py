#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [n for n in num_list if n % 2 == 0]
    return num_list

return_evens([0,1,2,3,4])

def make_exclamation(sentence_list):
    sentence_list = [s + '!' for s in sentence_list]
    return sentence_list
