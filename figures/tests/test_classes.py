import os.path
import sys

SUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../src")
sys.path.append(SUT)
# print(sys.path)

import pytest
import math
from rectangle import Rectangle
from square import Square
from circle import Circle
from triangle import Triangle

EPSILON = 0.05


@pytest.fixture(scope="session", autouse=True)
def run_stop_tests():
    print('\nTests started')

    yield

    print('\nTests finished')


@pytest.mark.positive
@pytest.mark.parametrize(("figure", "sides", "expected_area"), [
    (Triangle, (3, 4, 5), 6),
    (Rectangle, (3, 4), 12),
    (Square, (3,), 9),
    (Circle, (1,), math.pi)
])
def test_figure_area_positive(figure, sides, expected_area):
    f = figure(*sides)

    if isinstance(expected_area, float):
        assert f.get_area() == pytest.approx(expected_area, EPSILON)
    else:
        assert expected_area == f.get_area()

@pytest.mark.positive
@pytest.mark.parametrize(("figure", "sides", "expected_perimeter"), [
    (Triangle, (3, 4, 5), 12),
    (Rectangle, (3, 4), 14),
    (Square, (3,), 12),
    (Circle, (2,), 4*math.pi)
])
def test_figure_perimeter_positive(figure, sides, expected_perimeter):
    f = figure(*sides)

    if isinstance(expected_perimeter, float):
        assert f.get_perimeter() == pytest.approx(expected_perimeter, EPSILON)
    else:
        assert expected_perimeter == f.get_perimeter()

@pytest.mark.negative
@pytest.mark.parametrize(("figure", "sides"), [
    (Triangle, (1, 1, 100)),
    (Rectangle,  (-3, 4)),
    (Square, (0,)),
    (Circle, (-1,))
])
def test_figure_negative(figure, sides):
    with pytest.raises(ValueError) as e_info:
        f = figure(*sides)
