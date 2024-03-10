from numb3rs import validate


def test_limit():
    assert validate("256.1.2.3") == False


def test_letters():
    assert validate("cat") == False


def test_five_bytes():
    assert validate("1.2.3.4.5") == False


def test_1st_byte():
    assert validate("255.256.255.255") == False
