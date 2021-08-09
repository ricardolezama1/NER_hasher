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

    
    
import matplotlib.pyplot as plt
import numpy as np


def plot_terms_body(topic, data):
    """
The no.aranage attribution is to understand how to best and programmatically 
    plot the data. Intervals are determined by the counts within the dictionary. 
    The user does not need to predefine the graph. Instead, the second line takes the 
    frequency. Appropriate for body  metadata. 
    
    Args: Topic is the name of the plot/category. Data is a dictionary with frequency counts.
    
    No object returned. However, plot is automatically generated.
        """
    #The bar plot should be optimized for the max and min size of
    #individual 
    filter_ones = {term:frequency for term, frequency in data.items() if frequency > 10}  
    filtered = {term:frequency for term, frequency in data.items() if frequency > round(sum(filter_ones.values())/len(filter_ones))  }   
    print(round(sum(filtered.values())/len(filtered)), "Average count as result of total terms minus once identified terms divided by all terms.")
    terms = filtered.keys()
    frequency = filtered.values()   
    y_pos = np.arange(len(terms),step=1)
    # min dictionary value, max filtered value ; 
    x_pos = np.arange(min(filtered.values()), max(filtered.values()), step=round(sum(filtered.values())/len(filtered)))
    plt.barh(y_pos, frequency, align='center', alpha=1)
    plt.yticks(y_pos, terms, fontsize=12)
    plt.xticks(x_pos)
    plt.xlabel('Frecuencia en encabezados')
    plt.title(str(topic), fontsize=14)
    plt.tight_layout()
    plt.show()
    
def plot_terms_headline(topic, data):
    """
    The no.aranage attribution is to understand how to best and programmatically 
    plot the data. Intervals are determined by the counts within the dictionary. 
    The user does not need to predefine the graph. Instead, the second line takes the 
    frequency
    
    Args: Topic is the name of the plot/category. Data is a dictionary with frequency counts.
    
    No object returned. However, plot is automatically generated.
    """
    filter_ones = {term:frequency for term, frequency in data.items() if frequency > 1}  
    filtered = {term:frequency for term, frequency in filter_ones.items() if frequency > round(sum(filter_ones.values())/len(filter_ones))}  
    print(round(sum(filtered.values())/len(filtered)), "Average count as result of total terms minus once identified terms divided by all terms.")
    terms = filtered.keys()
    frequency = filtered.values()   
    y_pos = np.arange(len(terms),step=1)
    x_pos = np.arange(min(filtered.values()), max(filtered.values()), step=round(sum(filtered.values())/len(filtered)))
    plt.barh(y_pos, frequency, align='center', alpha=1)
    plt.yticks(y_pos, terms, fontsize=12)
    plt.xticks(x_pos)
    plt.xlabel('Frecuencia en encabezados')
    plt.title(str(topic), fontsize=14)
    plt.tight_layout()
    plt.show()
