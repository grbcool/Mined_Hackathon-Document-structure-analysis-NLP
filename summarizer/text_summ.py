import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize,sent_tokenize
import dill as pickle

from heapq import nlargest
from collections import defaultdict

nltk.download('stopwords')

stop_words = stopwords.words('english')
stop_punct_words = stop_words + list(punctuation + '\n')

nltk.download('punkt')

def text_summ(word_tokens):
    '''
    word_tokens : tokens obtained from ocr
    '''
    sentences = ' '.join(word_tokens)
    #frequency table
    freq = {}
    tokens = word_tokenize(sentences)
    for word in tokens:
        if word.lower() not in stop_punct_words:
            if not freq.get(word.lower(),False):
                freq[word.lower()] = 1
            else:
                freq[word.lower()] +=1
    max_value = max(freq.values())
    for word in freq.keys():
        freq[word] = freq[word]/max_value
        
    #weighted importance of sentences
    sentence_weight = defaultdict()
    count2sent = {}
    count = 0
    for sentence in sent_tokenize(sentences):
        for word in freq.keys():
            if word in sentence.lower():
                if not sentence_weight.get(sentence,False) :
                    sentence_weight[count] = freq[word]
                    count2sent[count] = sentence
                else:
                    sentence_weight[count] += freq[word]
        count += 1            
    
    #selecting nlargest sentences as summary
    select_len = int(len(sentence_weight)*0.3)
    
    ids = nlargest(select_len,sentence_weight,sentence_weight.get)
    summary = [count2sent[i] for i in ids ]
    
    return summary

pickle.dump(text_summ,open(f'summarizer.pickle','wb'))

