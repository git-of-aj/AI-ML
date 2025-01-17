import unittest
import nltk
from nltk.tokenize import word_tokenize

# Ensure that you have downloaded the necessary resources
nltk.download('punkt')

class TestWordTokenizer(unittest.TestCase):

    def test_basic_tokenization(self):
        text = "Hello world."
        expected_tokens = ['Hello', 'world', '.']
        result = word_tokenize(text)
        self.assertEqual(result, expected_tokens)

    def test_tokenization_with_punctuation(self):
        text = "It's a beautiful day!"
        expected_tokens = ["It", "'s", 'a', 'beautiful', 'day', '!']
        result = word_tokenize(text)
        self.assertEqual(result, expected_tokens)

    def test_tokenization_with_special_characters(self):
        text = "Email me at test@example.com."
        expected_tokens = ['Email', 'me', 'at', 'test@example.com', '.']
        result = word_tokenize(text)
        self.assertEqual(result, expected_tokens)

    def test_tokenization_with_numbers(self):
        text = "There are 100 apples."
        expected_tokens = ['There', 'are', '100', 'apples', '.']
        result = word_tokenize(text)
        self.assertEqual(result, expected_tokens)

    def test_tokenization_with_line_break(self):
        text = "Hello world.\nThis is a test."
        expected_tokens = ['Hello', 'world', '.', '\n', 'This', 'is', 'a', 'test', '.']
        result = word_tokenize(text, preserve_line=True)
        self.assertEqual(result, expected_tokens)

    def test_tokenization_without_line_break(self):
        text = "Hello world.\nThis is a test."
        expected_tokens = ['Hello', 'world', '.', 'This', 'is', 'a', 'test', '.']
        result = word_tokenize(text, preserve_line=False)
        self.assertEqual(result, expected_tokens)

    def test_tokenization_with_empty_string(self):
        text = ""
        expected_tokens = []
        result = word_tokenize(text)
        self.assertEqual(result, expected_tokens)

    def test_tokenization_with_multiline_text(self):
        text = "This is a test.\nHere's another line."
        expected_tokens = ['This', 'is', 'a', 'test', '.', '\n', 'Here', "'s", 'another', 'line', '.']
        result = word_tokenize(text, preserve_line=True)
        self.assertEqual(result, expected_tokens)

    def test_tokenization_with_different_language(self):
        text = "Ceci est un test."
        expected_tokens = ['Ceci', 'est', 'un', 'test', '.']
        result = word_tokenize(text, language='french')
        self.assertEqual(result, expected_tokens)

if __name__ == '__main__':
    unittest.main()
