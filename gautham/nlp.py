import re

class SimpleStemmer:
    def __init__(self):
        self.suffixes = ['ing', 'es', 'ed', 'ly','eous', 'ous', 's', 'ies', 'ment', 'ness', 'ful','ion']    

    def stem_suff(self, word):
        word = word.lower()  
        for suffix in self.suffixes:
            if word.endswith(suffix):
                return word[:-len(suffix)]
        return word



stemmer = SimpleStemmer()

import pandas as pd

with open('sample.txt','r') as f:
    file1 = f.read()
    
with open('verbs-all.csv', 'r') as f:
    df = f.read()

df = re.sub(r'[\n\t]', ' ', df)
df = df.split(' ')

with open('verbs-all.csv', 'w') as f:
    f.write(",".join(df))

print(df)    


file1 = file1.lower()
words = {}
temp = "" 
punct = set([".", ",", "!", "?", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "-", "_", "..."]) 
stop_words = [
    'the', 'a', 'an', 'he', 'she', 'it', 'they', 'we', 'you', 'I', 'me', 'them', 'him', 'us', 
    'my', 'your', 'his', 'her', 'our', 'their', 'and', 'or', 'but', 'because', 'if', 'although', 
    'though', 'unless', 'nor', 'either', 'neither', 'in', 'on', 'at', 'by', 'for', 'with', 'about', 
    'as', 'between', 'under', 'over', 'before', 'after', 'during', 'through', 'around', 'across', 
    'behind', 'beneath', 'above', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 
    'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should', 'can', 'could', 'may', 
    'might', 'must', 'very', 'too', 'also', 'really', 'just', 'never', 'always', 'sometimes', 
    'usually', 'likely', 'actually', 'this', 'that', 'these', 'those', 'each', 'every', 'some', 
    'no', 'all', 'many', 'much', 'few', 'more', 'most', 'oh', 'well', 'hmm', 'ah', 'hey', 'oops', 
    'how', 'what', 'when', 'where', 'why', 'which', 'whose', 'who', 'whom', 'that', 'so', 'than', 
    'too', 'not'
]


for i in file1:
    if i in punct:
        continue
    elif i == " ":
        if temp not in words:
            words[temp] = 1
        else:
            words[temp]+=1
        temp = ""
    else:
        temp = temp+i

if temp:
    if temp not in words:
        words[temp] = 1
    else:
        words[temp] += 1

for key, value in list(words.items()):
    if key in stop_words:
        del words[key]


stemmed_words_1 = {}

for word, count in words.items():
    stemmed_word_suff = stemmer.stem_suff(word) 
    if word in df:
        if stemmed_word_suff in stemmed_words_1:
            stemmed_words_1[stemmed_word_suff] += count 
        else:
            stemmed_words_1[stemmed_word_suff] = count
    else:
        if word in stemmed_words_1:
            stemmed_words_1[word] += count 
        else:
            stemmed_words_1[word] = count



print(stemmed_words_1)

