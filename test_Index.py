from unittest import TestCase

from Index import isHelloCorrect


class Test(TestCase):
    def test_is_hello_correct(self):
        word = "Hello World"
        self.assertTrue(isHelloCorrect(word))
