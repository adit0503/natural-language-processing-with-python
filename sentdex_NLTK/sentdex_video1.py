import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

#tokenizing, corpora, lexicon

example_sentence = "NLP is important for scientific, economic, social, and cultural reasons. NLP is experiencing rapid growth as its theories and methods are deployed in a variety of new language technologies. For this reason it is important for a wide range of people to have a working knowledge of NLP. Within industry, this includes people in human-computer interaction, business information analysis, and web software development. Within academia, it includes people in areas from humanities computing and corpus linguistics through to computer science and artificial intelligence. (To many people in academia, NLP is known by the name of 'Computational Linguistics.')"

#example_sentence needs to be a string !!

tokenized_sentence = sent_tokenize(example_sentence)
print(type(tokenized_sentence[0]))
print(type(tokenized_sentence))

for s in tokenized_sentence:
    print(s)

tokenized_word = word_tokenize(example_sentence)
print(tokenized_word)
for w in tokenized_word:
    if w.isalpha():
        print(w)
