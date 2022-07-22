
"""
102-square.py
"""


class Square:
    """
    Defines a square
    """

    def __init__(self, size=0):
        """
        Creates an instance of Square
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Sets and gets the value of private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Finds area of the square
        """
        return self.__size * self. 

    def area(self):
        return (self.size ** 2)

    def __lt__(self, value):
        return (self.area() < value.area())

    def __le__(self, value):
        return (self.area() <= value.area())

    def __eq__(self, value):
        return (self.area() == value.area())

    def __ne__(self, value):
        return (self.area() != value.area())

    def __gt__(self, value):
        return (self.area() > value.area())

    def __ge__(self, value):
        return (self.area() >= value.area())
