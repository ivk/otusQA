#!/bin/env python 3

from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


def main():

    # positive:

    t1 = Circle(10)
    print(t1.get_area())

    t1 = Rectangle(10, 5)
    print(t1.get_area())

    t1 = Triangle(3, 4, 5)
    print(t1.get_area())

    t1 = Square(10)
    print(t1.get_area())

    s = Square(10)
    r = Rectangle(2, 5)
    ss = s.add_area(r)
    print(s.get_area(), r.get_area(), ss)

    #negative
    try:
        t3 = Circle(-2)
    except ValueError as ve:
        print ("Invalid Circle: %s" % ve)

    try:
        t4 = Circle (0)
    except ValueError as ve:
        print ("Invalid Circle: %s" % ve)

    try:
        t5 = Circle ('abc')
    except ValueError as ve:
        print("Invalid Circle: %s" % ve)

    try:
        t2 = Rectangle(-10, 100)
    except ValueError as ve:
        print("Invalid rectangle: %s" % ve)

    try:
        t3 = Rectangle("abc", 3)
    except ValueError as ve:
        print("Invalid rectangle: %s" % ve)

    try:
        t4 = Rectangle (0, 0)
    except ValueError as ve:
        print("Invalid rectangle: %s" % ve)

    try:
        t2 = Triangle(10, 100, 2)
    except ValueError as ve:
        print("Invalid Triangle: %s" % ve)

    try:
        t3 = Triangle(-2, 3,4)
    except ValueError as ve:
        print("Invalid Triangle: %s" % ve)

    try:
        t4 = Triangle (0, 5, 7)
    except ValueError as ve:
        print("Invalid Triangle: %s" % ve)

    try:
        t5 = Triangle ('abc', 5, 7)
    except ValueError as ve:
        print("Invalid Triangle: %s" % ve)


    try:
        t3 = Square(-2)
    except ValueError as ve:
        print("Invalid Square: %s" % ve)

    try:
        t4 = Square(0)
    except ValueError as ve:
        print("Invalid Square: %s" % ve)

    try:
        t5 = Square('abc')
    except ValueError as ve:
        print("Invalid Square: %s" % ve)


if __name__ == "__main__":
    main()