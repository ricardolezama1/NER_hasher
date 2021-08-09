# NER_news

Using the below scripts, you can extract persons and organizations. I recommend that you drop clean texts, '\n' ("new line seperated") texts. 
Count the entities and roll out with a json with the org/person entities. 

Using spacy, you can hash the entities extracted from a corpus. We will use the lighter Spanish language model from Spacy's natural language toolkit. If you can not run the below code, then you'll need to pip install that spacy language model. 
```
import spacy
import spacy.attrs
nlp = spacy.load('es_core_news_sm')
```

For example, the following line contains the first bit of code referencing spacy and individuates each relevant piece of the text. Suppose these were encyclopedic or 
news articles, then the split would probably capture paragraph or sentence level breaks in the text: 

``` python
raw_corpus = open('corpora/titularesdemx.txt','r', encoding='utf-8').read().split("\n")[1:]
```
Finally, the actual hard work involves identifying distinct entities. These NER operations are powered by the smaller language model from Spacy. One thing that should be noted is that the text has its origins in Wikipedia. This means that newer more contemporary types of text may not be sufficiently well covered - breadth doesnt imply depth in analysis. Anecdotally, over a small corpus, we see performance below 80 percent accuracy. 

The actual hashing is a simple enough method involving placing NER text with its frequency count as a value in a dictionary.

```
import org_per

entities = org_per.sacalasentidades(raw_corpus)
 
# use list of entities that are ORG or PER and count up each invidividual token.     

tokensdictionary = org_per.map_entities(entities) 
 ```
 
 The output will look like this: 
 
 ```python 
 
 {"Bill Clinton": 123,
 "Kenneth Starr" : 12,
 }
 
 ```
This final json formatted/dictionary style count for named entities along with frequencies is sufficient for pandas/matplotlib visualizations. 
