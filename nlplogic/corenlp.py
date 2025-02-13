import wikipedia
from textblob import TextBlob


def search_wikipedia(name):
    """Search for the given name"""
    print(f"searching for {name}")
    return wikipedia.search(name)


def wikipedia_smmary(name):
    """create summary for the given name"""
    print(f"Generating summary for {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """return text blob object"""
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia names and return"""
    text = wikipedia_smmary(name)
    blob = get_text_blob(text)
    return blob.noun_phrases
