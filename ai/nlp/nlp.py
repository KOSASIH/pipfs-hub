import spacy

class NLP:
    def __init__(self, model='en_core_web_sm'):
        self.nlp = spacy.load(model)

    def process(self, text):
        """Process text using the spaCy NLP library."""
        return self.nlp(text)

    def extract_entities(self, text):
        """Extract entities from text using the spaCy NLP library."""
        doc = self.nlp(text)
        return [(X.text, X.label_) for X in doc.ents]
