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
        return self.__width == value
    @height.setter
    def height(self, value):
        return self.__height == value
    @x.setter
    def x(self, value):
        return self.__x == value
    @property
    def y(self, value):
        return self.__y == value    