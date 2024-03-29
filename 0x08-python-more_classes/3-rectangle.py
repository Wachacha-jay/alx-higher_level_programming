#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:                                                                                                                self.__width = value

    @property
    def height(self):                                                                                                   return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:                                                           
            raise TypeError("height must be an integer")                                                        
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return " "
        rec = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return rec
