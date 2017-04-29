import pytest
from ..hw2.Commission import commission


@pytest.mark.parametrize("locks, stocks, barrels, expected",[
        ( 0, 80, 90, "Out of range value"),
        ( 70, 0, 90, "Out of range value"),
        ( 70, 80, 0, "Out of range value"),
        ( 1, 1, 1, 10),
        ( 11, 10, 10, 106.75),
        ( 70, 80, 90, 1420),
    ])
def test_c0( locks, stocks, barrels, expected):
    assert commission( locks, stocks, barrels) == expected

@pytest.mark.parametrize("locks, stocks, barrels, expected",[
    ])
def test_c1( locks, stocks, barrels, expected):
    assert commission( locks, stocks, barrels) == expected

@pytest.mark.parametrize("locks, stocks, barrels, expected",[
    ])
def test_c2( locks, stocks, barrels, expected):
    assert commission( locks, stocks, barrels) == expected

@pytest.mark.parametrize("locks, stocks, barrels, expected",[
    ])
def test_mcdc( locks, stocks, barrels, expected):
    assert commission( locks, stocks, barrels) == expected
