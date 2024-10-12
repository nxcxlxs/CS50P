import pytest
from working import convert


def test_period():
    assert convert("1 PM to 10 PM") == "13:00 to 22:00"
    assert convert("1 AM to 10 AM") == "01:00 to 10:00"

def test_range():
    with pytest.raises(ValueError):
        convert("25 PM to 28 PM")

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
