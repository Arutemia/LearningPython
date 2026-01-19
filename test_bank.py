from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello, Bob!") == 0


def test_h_without_hello():
    assert value("hi!") == 20
    assert value("how are you?") == 20


def test_any_other_response():
    assert value("why are you here?") == 100
    assert value("Good morning!") == 100
