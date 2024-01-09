"""
In this module, you will explore the practical application of Regular Expressions (RegEx) in Natural Language Processing (NLP) using the NLTK library. Before diving into the technical details, let's clarify two essential NLP concepts: normalization and tokenization.

Normalization:
Normalization in NLP refers to the process of transforming text into a consistent and standardized format. It involves handling variations in language, such as converting words to lowercase, removing punctuation, and addressing different spellings of the same word. Normalization ensures that the text is uniform and ready for analysis, reducing the impact of irregularities in language.

For example, consider the words "Text," "text," and "TEXT." Normalizing these words would involve converting all of them to lowercase, so they are treated as the same word during analysis.

"""
import re 
# Example of string normalization. DO NOT modify this function
def sampleNormalization():
    text = "If a qu1ck, brown fox jumps! over the lazy cat and takes- a long nap themselves... does that make the fox itself lazy?"
    text = text.lower() # we first make all text lower case
    pattern = r"[^\w\d ]" # and write a regex that matches all characters that are not letters, digits, and white spaces
    normalized = re.sub(pattern, '', text) # and replace all the matches with an empty string
    return normalized

"""
TODO: Complete the following function to normalize an input string
It should do the following
1. Turn all text into Uppercase
2. Remove all non alpha-numeric characters
"""
def normalizationExercise(input_text):
  
    normalized = input_text
    return normalized

"""
Tokenization:
Tokenization is the process of breaking down a text into smaller units called tokens. Tokens are the building blocks of language, representing individual words or meaningful sub-word units. In English, tokens are typically words, but they can also be phrases or sub-word units, depending on the context.

For instance, the sentence "I love NLTK!" can be tokenized into the following words: ["I", "love", "NLTK", "!"]. Tokenization is a crucial step in NLP, as it allows us to analyze and manipulate text at a granular level, facilitating tasks like counting words, identifying patterns, and extracting meaningful information.
"""

from nltk.tokenize import word_tokenize, sent_tokenize

"""
In NLTK, we have 2 tokenization functions: word_tokenize and sent_tokenize. The usage is the same, the difference is word_tokenize separates each word into a token, where as sent_tokenize will separate sentences into a token.
"""
def sampleTokenization():
    # DO NOT modify this function
    text = "If a qu1ck, brown fox jumps! over the lazy cat and takes- a long nap themselves... does that make the fox itself lazy?"

    word_tokens = word_tokenize(text)
    return word_tokens

"""
TODO: Take input_text do the following:
1. use word_tokenize function on text
2. use sent_tokenize function on text
3. return the tokens in an object with key "words" for word tokens and "sents" for sentence tokens
"""
def tokenizationExercise(input_text):
    word_tokens = []
    sent_tokens = []
    return {"words" :word_tokens, "sents": sent_tokens}

"""
Stopwords are common words in a language that does not offer a lot of meaning or context in a sentence. In English, words such as 'a', 'the', 'this', or 'in' are examples of stopwords. We can utilize NLTK to remove such words.
"""

from nltk.corpus import stopwords
def sampleStopwordRemoval():
    # Do Not modify this function
    # create a set of nltk's english stopwords
    stop_words = set(stopwords.words('english'))

    word_tokens = sampleTokenization()

    # take the tokenized text from earlier and remove stopwords
    filtered = [w for w in word_tokens if not w in stop_words]

    return filtered


"""
nltk.text module
This module brings together a variety of NLTK functionality for text analysis, and provides simple, interactive interfaces.

1. FindAll(regexp)
Finds instances of the regular expression in the text. The text is a list of tokens, and a regexp pattern to match a single token must be surrounded by angle brackets.
"""

from nltk.book import text1, text5

def sampleFindAll():
    # Do not modify this function
    # finds 2 tokens that preceeds the word "bro", and return just the 2 preceeding tokens
    return text5.findall("(<.*><.*>)<bro>") 

"""
TODO: Text1 in NLTK book module is mobydick. Complete this function so it finds all words describing "the" whale, that is, find the adjective (one word) that is between words "the" and "whale"
"""
def findAllExercise():
    result = text1
    return result
    