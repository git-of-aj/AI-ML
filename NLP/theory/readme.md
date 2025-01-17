### corpus / corpora
A **corpus** is a large, structured collection of text data used in natural language processing (NLP). It serves as a resource for training models, testing algorithms, and performing linguistic analysis. Examples include datasets of news articles, books, or conversations for various NLP tasks.

## how to get Prod level 
1. create unit test for tokenizer, lemmetizer - fix issues
2. Use step-by-step data pre-processing:
- POS Tagging: nltk.pos_tag() tags each word with its corresponding part of speech. This helps in understanding whether the word is a verb, noun, adjective, etc.
- POS Mapping: The get_wordnet_pos() function maps the POS tags from NLTK’s format (Treebank format) to WordNet POS tags, which are used by the WordNetLemmatizer.
- Lemmatization: After identifying the POS, the lemmatizer is applied according to whether the word is a verb, noun, adjective, or adverb.
