import pytest
from Triangle import triangle


@pytest.mark.parametrize("a, b, c, expected",[
        ( 0, 100, 100, "Out of range value"),
        ( 100, 0, 100, "Out of range value"),
        ( 100, 100, 0, "Out of range value"),
        ( 3, 3, 3, "Equilateral"),
        ( 10, 10, 2, "Isosceles"),
        ( 3, 4, 6, "Scalene"),
        ( 5, 5, 25, "Not a triangle"),
    ])
def test_c0( a, b, c, expected):
    assert triangle( a, b, c) == expected

@pytest.mark.parametrize("a, b, c, expected",[
    ])
def test_c1( a, b, c, expected):
    assert triangle( a, b, c) == expected

@pytest.mark.parametrize("a, b, c, expected",[
    ])
def test_c2( a, b, c, expected):
    assert triangle( a, b, c) == expected

@pytest.mark.parametrize("a, b, c, expected",[
    ])
def test_mcdc( a, b, c, expected):
    assert triangle( a, b, c) == expected
