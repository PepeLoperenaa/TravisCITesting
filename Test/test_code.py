import pytest
from Index import isHelloCorrect


def test_hello():
    word = 'Hello World'
    assert (isHelloCorrect(word))
