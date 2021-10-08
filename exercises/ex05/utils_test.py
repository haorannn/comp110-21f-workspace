"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730490705"


def test_only_evens_edge_case() -> None: 
    """Test."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_use_case1() -> None: 
    """Test."""
    xs: list[int] = [1, 2, 4, 58, 985, 211, 344]
    assert only_evens(xs) == [2, 4, 58, 344]


def test_only_evens_use_case2() -> None: 
    """Test."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_sub_edge_case() -> None: 
    """Test."""
    xs: list[int] = []
    beg_i: int = 9
    end_i: int = -1
    assert sub(xs, beg_i, end_i) == []


def test_sub_use_case1() -> None: 
    """Test."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    beg_i: int = 1
    end_i: int = 3
    assert sub(xs, beg_i, end_i) == [2, 3]


def test_sub_use_case2() -> None: 
    """Test."""
    xs: list[int] = [1, 2, 3, 4, 5]
    beg_i: int = 4
    end_i: int = 5
    assert sub(xs, beg_i, end_i) == [5]


def test_concat_edge_case() -> None: 
    """Test."""
    xs1: list[int] = []
    xs2: list[int] = []
    assert concat(xs1, xs2) == []


def test_concat_use_case1() -> None: 
    """Test."""
    xs1: list[int] = [1, 2, 3, 4, 5]
    xs2: list[int] = [6, 7, 8, 9, 10]
    assert concat(xs1, xs2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_use_case2() -> None: 
    """Test."""
    xs1: list[int] = [1]
    xs2: list[int] = [6, 7, 8, 9, 10]
    assert concat(xs1, xs2) == [1, 6, 7, 8, 9, 10]