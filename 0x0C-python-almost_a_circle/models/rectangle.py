#!/usr/bin/python3

from models.base import Base
"""_summary_

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
   
    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width
    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height
    @property
    def x(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x
    @property
    def y(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__y
    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if value <= 0:
            raise ValueError("Width must be positive")
        self.__width == value
    @height.setter
    def height(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if value <= 0:
            raise ValueError("height must be positive")
        self.__height == value
    @x.setter
    def x(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if value <= 0:
            raise ValueError("x must be positive")
        self.__x == value
    @y.setter
    def y(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if value <= 0:
            raise ValueError("y must be positive")
        self.__y == value    