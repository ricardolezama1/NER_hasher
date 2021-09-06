# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:25:20 2020


@author: Ricardo Lezama

The functions here are designed to extract entities from text.
They are hard coded to GEO entities and PER entities from the Spacy-NER module(s).
The loaded module is `es_core_news_sm`.  
Count the number of times a word appears inside of a corpus. 

"""

import matplotlib.pyplot as plt

import numpy as np

import spacy

import spacy.attrs

nlp = spacy.load('es_core_news_sm')


def sacalasentidades(docs):
    """"
    Identifica entidades sin importar la categoría. 
    
    Arg: toma como argumento una lista de oraciones.  
    
    Return: Una lista de los tokens individuales. 
    """
    list =[]
    for doc in docs: 
        nah = nlp(doc)
        for ent in nah.ents:
            if ent.label_ == 'GEO' or ent.label_ == 'PER':
                list.append(ent.text) 
    stopwords = open('corpora/stopwords.txt', 'r', encoding='utf-8').read().split("\n")
    cancelled = [content for content in list if content not in stopwords]
    return cancelled 

def map_entities(tokens):
    """
    cuenta los terminos.
    
    Arg: tokens son los terminos dentro de sacalasentidades --- 
        
    Return: hash_map hace un diccionario con terminos y conteos.    
    """
    hash_map = {}
    if tokens is not None:
        for element in tokens:
            # Remove Punctuation
            word = element.replace(",","")
            word = word.replace(".","")
            
            # Word Exist?
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1
       
        return hash_map
    else:
        return None

 
