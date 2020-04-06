from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

#nltk is only a toolkit - not used to perform analytics but to pre-process data to fit into other analytical models
# stemming - normalization of words i.e going to the root of the words. (used to remove redundancy by storing only one variation of all the words.)

ps = PorterStemmer()

example_sentence = "NLP is important for scientific, economic, social, and cultural reasons. NLP is experiencing rapid growth as its theories and methods are deployed in a variety of new language technologies. For this reason it is important for a wide range of people to have a working knowledge of NLP. Within industry, this includes people in human-computer interaction, business information analysis, and web software development. Within academia, it includes people in areas from humanities computing and corpus linguistics through to computer science and artificial intelligence. (To many people in academia, NLP is known by the name of 'Computational Linguistics.')"
tokenized = word_tokenize(example_sentence)

stemmed_words = set()
before_stemming_words = set()

for t in tokenized:
    t = t.lower()
    if t.isalnum():
        before_stemming_words.add(t)
        stemmed_words.add(ps.stem(t))
print(stemmed_words)
print(before_stemming_words)
print(len(before_stemming_words),len(stemmed_words)) #63 60
