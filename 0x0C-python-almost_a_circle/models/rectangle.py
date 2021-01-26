#!/usr/bin/python3
# rectangle.py
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        # Validate variables

        # Validate width
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        # validate height
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        # validate x
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        # validate y
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """width getter function
        """

        return self._width

    @width.setter
    def width(self, width):
        """Sets the width attribute
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self._width = width

    @property
    def height(self):
        """height getter function
        """

        return self._height

    @height.setter
    def height(self, height):
        """Sets the height attribute
        """

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self._height = height

    @property
    def x(self):
        """x getter function
        """

        return self._x

    @x.setter
    def x(self, x):
        """Sets the x attribute
        """

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self._x = x

    @property
    def y(self):
        """y getter function
        """

        return self._y

    @y.setter
    def y(self, y):
        """Sets the x attribute
        """

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self._y = y

    def area(self):
        """Returns the area of the current
        rectangle"""

        return self._width * self._height

    def display(self):
        """prints the rectangle
        """

        if self._width == 0 or self._height == 0:
            print()
            return

        if self._y != 0:
            print("\n" * (self._y - 1))
        for y in range(self._height):
            if self._x != 0:
                print(" " * self._x, end="")
            print("#" * self._width)

    def __str__(self):
        """string representaaion of the class
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self._x,
                                                       self._y,
                                                       self._width,
                                                       self._height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

         Args:
             *args (ints): New attribute values.
                 - 1st argument represents id attribute
                 - 2nd argument represents width attribute
                 - 3rd argument represent height attribute
                 - 4th argument represents x attribute
                 - 5th argument represents y attribute
             **kwargs (dict): New key/value pairs of attributes.
        """

        new_args = [self.id, self._width, self._height, self._x, self._y]
        if len(args) == 0 or args is None:
            if len(kwargs) == 0:
                return
            else:
                try:
                    new_args[0] = kwargs['id']
                except KeyError:
                    pass
                try:
                    new_args[1] = kwargs['width']
                except KeyError:
                    pass
                try:
                    new_args[2] = kwargs['height']
                except KeyError:
                    pass
                try:
                    new_args[3] = kwargs['x']
                except KeyError:
                    pass
                try:
                    new_args[4] = kwargs['y']
                except KeyError:
                    pass
        else:
            for x in range(len(args)):
                if x < len(new_args):
                    new_args[x] = args[x]
        self.__init__(new_args[1],
                      new_args[2],
                      new_args[3],
                      new_args[4],
                      new_args[0])

    def to_dictionary(self):
        """Returns a dictionary representation of the the
        object"""

        obj_dic = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return obj_dic
