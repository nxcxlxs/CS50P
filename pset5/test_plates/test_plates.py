from plates import is_valid


def test_beginning():
    assert is_valid("50") == False
    assert is_valid("CS") == True


def test_length():
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCDEF") == True


def test_number_placement():
    assert is_valid("AAA11A") == False
    assert is_valid("AAA111") == True


def test_zero_placement():
    assert is_valid("AAA011") == False
    assert is_valid("AAA110") == True


def test_alphanumeric_only():
    assert is_valid("AAA.11") == False
