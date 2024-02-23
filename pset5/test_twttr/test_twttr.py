from twttr import shorten

def test_vowels():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""

def test_consonants():
    assert shorten("qwerty") == "qwrty"
    assert shorten("QWERTY") == "QWRTY"

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten(":;.,") == ":;.,"