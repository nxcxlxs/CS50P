from bank import value

def test_first_h():
    assert value("hey") == 20

def test_no_h():
    assert value("what's up?") == 100

def test_case():
    assert value("Hi") == 20
    assert value("hi") == 20

