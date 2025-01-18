## Python Tips:
1. List Comprehension:
> new_list = [expression for item in iterable if condition]
- it runs reverse (bottom line ==> right side)
- item which should be present in list in left side 
2. Regex
> re.sub(pattern, repl, string, count=0, flags=0)

Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern isn’t found, string is returned unchanged

### corpus / corpora
A **corpus** is a large, structured collection of text data used in natural language processing (NLP). It serves as a resource for training models, testing algorithms, and performing linguistic analysis. Examples include datasets of news articles, books, or conversations for various NLP tasks.

## how to get Prod level 
1. create unit test for tokenizer, lemmetizer - fix issues
2. Use step-by-step data pre-processing:
- POS Tagging: nltk.pos_tag() tags each word with its corresponding part of speech. This helps in understanding whether the word is a verb, noun, adjective, etc.
- POS Mapping: The get_wordnet_pos() function maps the POS tags from NLTK’s format (Treebank format) to WordNet POS tags, which are used by the WordNetLemmatizer.
- Lemmatization: After identifying the POS, the lemmatizer is applied according to whether the word is a verb, noun, adjective, or adverb.
