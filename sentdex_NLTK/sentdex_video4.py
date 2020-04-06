import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize,sent_tokenize,PunktSentenceTokenizer
#part of speech tagging - tagging each word to its corresponding noun/adj/verb etc
'''
Number Tag Description
1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
'''
state_union.fileids()

text = state_union.raw('2006-GWBush.txt')

train_text = state_union.raw('2005-GWBush.txt')
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized1 = custom_sent_tokenizer.tokenize(text)
tagged1 = []

tokenized2 = sent_tokenize(text)
tagged2 = []

for sent in tokenized1:
    words = word_tokenize(sent)
    tagged = nltk.pos_tag(words)
    tagged1.append(tagged)
tagged1[0] #every sentence is a list of tuples (<Word> , <Tag>)

for sent in tokenized2:
    words = word_tokenize(sent)
    tagged = nltk.pos_tag(words)
    tagged2.append(tagged)
tagged2[0]
