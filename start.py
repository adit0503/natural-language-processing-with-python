import nltk
from nltk.book import *

example_sent = " ".join(sent1+sent2+sent3+sent4)
print(example_sent)

text1
type(text1)
s = str(text1)
s

text1.concordance('monstrous')
text1.similar('monstrous')
text1.common_contexts(['monstrous','curious']) #<text obj>.common_contexts()

len(text1)
len(set(text1))

word_list = set(text1)
word_dict = {}
for wl in word_list:
    word_dict[wl] = text1.count(wl)
list(word_dict.keys())

fd = FreqDist(text1)
fd
fd.plot(50, cumulative=True)
len(fd.keys())
vocab = []
for k in fd.keys():
    vocab.append(k)
vocab[:10]
fd['whale']
text1.count('whale')

count_lol = text5.count('lol')
len_text5 = len(text5)
percent_lol = (count_lol / len_text5)*100
percent_lol

def word_percentage(word,text)-> float:
    count_word = text.count(word)
    len_text = len(text)
    return round((count_word/len_text)*100 , 2)
word_percentage('lol',text5)

v = set(text1)
long_words = [w for w in v if len(w)>10]
sorted(long_words)
