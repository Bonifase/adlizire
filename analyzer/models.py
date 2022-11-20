import nltk

# Create your models here.
class Word(object):
    """
    A model class of a 'word'
    """
    def __init__(self, word, intensifiers=None, compulsive_hedgers=None, vague_words=None):
        self.syllables = None
        self.word = word.strip().lower()
        self.intensifiers = intensifiers
        self.compulsive_hedgers = compulsive_hedgers
        self.vague_words = vague_words


class Sentence(object):
    """
    A model class that represents a sentence.
    """
    def __init__(self, sentence):
        self.sentence = sentence
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word.isalpha() or word.isdigit()]
        self._words = [word for word in words]


class Paragraph(object):
    """
    A model class that represents a paragraph.
    """
    def __init__(self, paragraph):
        self.paragraph = self.paragraph_parser(paragraph)
        self.tokenized_sentences = nltk.sent_tokenize(paragraph)
        self._sentences = [Sentence(sentence) for sentence in self.tokenized_sentences]

    @staticmethod
    def paragraph_parser(self, paragraph):
        p = paragraph.replace('—', ' ')
        return nltk.parse_paragraph(p)
