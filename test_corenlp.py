from nlplogic.corenlp import *

def test_get_phrases():
    assert 'microsoft' in get_phrases("Microsoft")