import pytest
from NextDate import nextdate


@pytest.mark.parametrize("year, month, day, expected",[
        ( 1899, 6, 15, "Out of range value"),
        ( 2026, 6, 15, "Out of range value"),
        ( 1900, 0, 15, "Out of range value"),
        ( 1900, 13, 15, "Out of range value"),
        ( 2000, 6, 15, "2000/6/16"),
        ( 1960, 6, 15, "1960/6/16"),
        ( 1900, 6, 0, "Out of range value"),
        ( 1900, 6, 32, "Out of range value"),
        ( 1900, 2, 30, "Invalid date"),
        ( 1900, 4, 31, "Invalid date"),
        ( 1900, 12, 31, "1901/1/1"),
        ( 1900, 1, 31, "1900/2/1"),
    ])
def test_c0( year, month, day, expected):
    assert nextdate( year, month, day) == expected

@pytest.mark.parametrize("year, month, day, expected",[
    ])
def test_c1( year, month, day, expected):
    assert nextdate( year, month, day) == expected

@pytest.mark.parametrize("year, month, day, expected",[
    ])
def test_c2( year, month, day, expected):
    assert nextdate( year, month, day) == expected

@pytest.mark.parametrize("year, month, day, expected",[
    ])
def test_mcdc( year, month, day, expected):
    assert nextdate( year, month, day) == expected
