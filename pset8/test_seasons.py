from seasons import convert
import pytest

def test_iso_format():
    with pytest.raises(SystemExit):
        convert("01-01-1990")

def test_convert():
    assert convert("2023-10-29") == "Five hundred twenty-seven thousand forty minutes"
