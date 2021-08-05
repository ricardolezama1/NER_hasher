# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:25:20 2020

@author: Ricardo Lezama
Count the number of tames ANY
"""

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
    return list 

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

    
    
import matplotlib.pyplot as plt
import numpy as np


def plot_terms(topic, data):
    """
    Args: Topic is the name of the plot/category. 
    
    Return frecuencia en encabezados.    
    """
    filter_ones = {term:frequency for term, frequency in data.items() if frequency != 1}  
    terms = filter_ones.keys()
    frequency = filter_ones.values()   
    y_pos = np.arange(len(terms),step=1)
    x_pos = np.arange(1,15, step=1)
    plt.barh(y_pos, frequency, align='center', alpha=1)
    plt.yticks(y_pos, terms, fontsize=12)
    plt.xticks(x_pos)
    plt.xlabel('Frecuencia en encabezados')
    plt.title(str(topic), fontsize=14)
    plt.tight_layout()
    plt.show()
    
