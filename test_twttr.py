from twttr import shorten


def test_sentence():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""


def test_numbers_and_symbols():
    assert shorten("123456@#$") == "123456@#$"


def test_single_letters():
    assert shorten("A") == ""
    assert shorten("B") == "B"
    assert shorten("a") == ""
    assert shorten("b") == "b"


def test_punctuation():
    assert shorten("Hi!") == "H!"
    assert shorten("Why?") == "Why?"
