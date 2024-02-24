from fuel import convert, gauge
import pytest


def test_gauge_convert():
    assert gauge(convert("3/4")) == "75%"
    assert gauge(convert("1/100")) == "E"
    assert gauge(convert("99/100")) == "F"


def test_error():
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
