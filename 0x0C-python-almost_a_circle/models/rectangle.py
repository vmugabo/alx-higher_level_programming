#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
       self.width = width
       self.height = height
       self.x = x
       self.y = y
       super().__init__(id)
   
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self.__width == value
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be positive")
        self.__height == value
    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("x must be positive")
        self.__x == value
    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("y must be positive")
        self.__y == value    