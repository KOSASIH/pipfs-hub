import nltk


def preprocess_text(text, config):
    # Preprocess text using the specified configuration
    # For example, tokenize, remove stop words, or stem the words

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    return filtered_tokens
