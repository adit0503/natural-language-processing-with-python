import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# text-preprocessing : stopwords - useless words that dont provide any insight to what you are doing. contextual based. remove fluffy words !

example_sentence = "NLP is important for scientific, economic, social, and cultural reasons. NLP is experiencing rapid growth as its theories and methods are deployed in a variety of new language technologies. For this reason it is important for a wide range of people to have a working knowledge of NLP. Within industry, this includes people in human-computer interaction, business information analysis, and web software development. Within academia, it includes people in areas from humanities computing and corpus linguistics through to computer science and artificial intelligence. (To many people in academia, NLP is known by the name of 'Computational Linguistics.')"
tokenized = word_tokenize(example_sentence)

stop_words = set(stopwords.words('english'))

filtered_sentence = set()

for t in tokenized:
    t = t.lower()
    if (t not in stop_words) and t.isalnum():
        filtered_sentence.add(t)
print(list(filtered_sentence))
# ['scientific', 'industry', 'interaction', 'analysis', 'range', 'areas', 'many', 'intelligence', 'reasons', 'theories', 'technologies', 'business', 'known', 'linguistics', 'artificial', 'name', 'nlp', 'within', 'new', 'cultural', 'information', 'development', 'social', 'working', 'methods', 'web', 'academia', 'important', 'computing', 'growth', 'deployed', 'economic', 'variety', 'reason', 'knowledge', 'includes', 'humanities', 'computer', 'experiencing', 'wide', 'corpus', 'rapid', 'software', 'people', 'language', 'science']


print(len(tokenized),len(filtered_sentence)) #114,46
