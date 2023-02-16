import pytest
from solution import (
    number_of_primes,
    reverse_list,
    reverse_list_inplace,
    square_root,
    square_root_using_newtons_method,
)


def square_root_baseline(n: int):
    """
    Baseline implementation using math.sqrt
    """
    return int(n**0.5)


# write tests for square_root
def test_square_root():
    assert square_root(0) == square_root_baseline(0)
    assert square_root(1) == square_root_baseline(1)
    assert square_root(4) == square_root_baseline(4)
    assert square_root(3) == square_root_baseline(3)
    assert square_root(999_999) == square_root_baseline(999_999)
    assert square_root(1_000_000) == square_root_baseline(1_000_000)
    assert square_root(1_000_001) == square_root_baseline(1_000_001)


def test_square_root_newtons_method():
    assert square_root_using_newtons_method(0) == square_root_baseline(0)
    assert square_root_using_newtons_method(1) == square_root_baseline(1)
    assert square_root_using_newtons_method(4) == square_root_baseline(4)
    assert square_root_using_newtons_method(3) == square_root_baseline(3)
    assert square_root_using_newtons_method(999_999) == square_root_baseline(999_999)
    assert square_root_using_newtons_method(1_000_000) == square_root_baseline(1_000_000)
    assert square_root_using_newtons_method(1_000_001) == square_root_baseline(1_000_001)


def test_number_of_primes():
    assert number_of_primes(0) == 0
    assert number_of_primes(1) == 0
    assert number_of_primes(2) == 1
    assert number_of_primes(3) == 2
    assert number_of_primes(4) == 2
    assert number_of_primes(5) == 3
    assert number_of_primes(7) == 4
    assert number_of_primes(11) == 5
    assert number_of_primes(10**5) == 9592
    assert number_of_primes(10**6) == 78498
    assert number_of_primes(10**7) == 664579


def test_reverse_list():
    assert reverse_list([]) == []
    assert reverse_list([1]) == [1]
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]


def test_reverse_list_inplace_check_for_integrity():
    arr = [1, 2, 3, 4]
    reverse_list_inplace(arr)
    assert arr == [4, 3, 2, 1]


def test_reverse_list_inplace():
    assert reverse_list_inplace([]) == []
    assert reverse_list_inplace([1]) == [1]
    assert reverse_list_inplace([1, 2, 3]) == [3, 2, 1]
    assert reverse_list_inplace([1, 2, 3, 4]) == [4, 3, 2, 1]
