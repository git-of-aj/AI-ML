import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Function to map POS tag to WordNet POS tag
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.ADJ

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

"""
Man – men.
Woman – women.
Ox – oxen.
Goose – geese.
Child – children.
Tooth – teeth.
Foot – feet.
Mouse – mice.
London - London
cities - city
"""
# List of pluralized and conjugated words
plurals = ['caresses', 'flies', 'dies', 'mules', 'denied',
            'died', 'agreed', 'owned', 'humbled', 'sized',
            'meeting', 'stating', 'siezing', 'itemization',
            'sensational', 'traditional', 'reference', 'colonizer',
            'plotted','mice','oxen','men','children','teeth','cities','London']

# Tokenize the words and get POS tags
tokens = word_tokenize(' '.join(plurals))
pos_tags = nltk.pos_tag(tokens)

# Lemmatize based on POS tags
lemmatized_words = [
    lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag)) 
    for word, tag in pos_tags
]

print(lemmatized_words)
