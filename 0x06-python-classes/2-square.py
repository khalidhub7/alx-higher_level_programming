#!/usr/bin/python3
"""Class python."""


class Square:
    """Def square hhh."""

    def __init__(self, size = 0):
        """Constructor.

        Args:
            size: len of side of the square.

        Raises:
            TypeError: if not int
            ValueError: if negative
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
