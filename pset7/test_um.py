from um import count


def test_isolated():
    assert count("yum") == 0
    assert count("umbrella") == 0
    assert count("hummus") == 0

def test_case():
    assert count("Um... Is this alright?") == 1
