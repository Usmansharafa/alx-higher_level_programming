#!/usr/bin/python3
""""Module that defines a MyInt class that inherits from int class"""


class MyInt(int):
    """Class representing my int"""

    def __eq__(self, value):
        """Override == operator with != behaviour"""
        return self.real != self.value

    def __ne__(self, value):
        """Override != operator with == behaviour"""
        return self.real == self.value
