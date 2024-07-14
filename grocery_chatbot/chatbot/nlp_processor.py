import spacy

class NLPProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_input(self, user_input):
        doc = self.nlp(user_input)
        intent = None
        item = None
        quantity = None

        for token in doc:
            if token.dep_ == "ROOT":
                intent = token.lemma_
            if token.pos_ == "NOUN":
                item = token.text
            if token.pos_ == "NUM":
                quantity = int(token.text)

        return intent, item, quantity