[nltk data](https://www.nltk.org/data.html)
Prebuilt corpora such as stopwords, punkt, and wordnet help with text preprocessing and advanced tasks like lemmatization, part-of-speech tagging, and sentiment analysis. [complete list](https://www.nltk.org/nltk_data/)

Access NLTK Data: NLTK provides a simple interface to download data.

1. You can use the following Python code to download specific datasets, corpora, or models:
```py
import nltk
nltk.download('punkt')  # For sentence/tokenization
nltk.download('stopwords')  # For stop words
nltk.download('wordnet')  # For lemmatization
```
2. Tokenize
```py
from nltk.tokenize import sent_tokenize, word_tokenize

# Example text
text = "Hello! How are you? I hope you're doing well."

# Sentence tokenization
sentences = sent_tokenize(text)
print(sentences)

# Word tokenization
words = word_tokenize(text)
print(words)
```
3. Lemmatize: If you need to perform tasks like lemmatization or find synonyms and antonyms, NLTK provides access to WordNet. This lexical database is an incredibly useful tool for semantic analysis.
```py
from nltk.corpus import wordnet

# Find synonyms and definitions
synonyms = wordnet.synsets("happy")
print(synonyms)
```
4. Parts of speech (POS) tagging: For tasks like Part-of-Speech tagging, which involves identifying the grammatical role of words in a sentence (e.g., noun, verb, adjective), NLTK offers pre-trained taggers.
```py
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# Example text
text = "NLTK is a great tool for NLP."

# Tokenize and perform POS tagging
words = word_tokenize(text)
tags = pos_tag(words)
print(tags)
```
