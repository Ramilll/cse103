def square_root(n: int) -> int:
    """
    Algorithm for solving Square root by having only multiplication at your disposal
    """
    assert n >= 0, "Square root of negative number is not defined"
    l, r = 0, n
    while l <= r:
        # integer division using bits (faster than using //)
        mid = (l + r) >> 1
        if mid * mid <= n < (mid + 1) * (mid + 1):
            return mid
        elif n < mid * mid:
            r = mid - 1
        else:
            l = mid + 1
    return l


def square_root_using_newtons_method(n: int) -> int:
    """
    Algorithm using Newton's method for finding zeros of real functions
    """
    z = n
    while z * z > n:
        z = (z + n // z) // 2
    return z


def number_of_primes(n: int) -> int:
    """
    This function computes the number of primes less than or equal to n
    """
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, square_root(n) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return sum(is_prime)


def reverse_list(arr: list) -> list:
    """
    This function reverses a list by creating a new one
    """
    n = len(arr)
    new_arr = [0] * n
    for i in range(len(arr)):
        new_arr[i] = arr[n - 1 - i]
    return new_arr


def reverse_list_inplace(arr: list) -> list:
    """
    This function reverses a list in place
    """
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr


def rotate_the_list_inplace(arr: list, k: int) -> list:
    """
    This function rotates the list by k steps
    """
    n = len(arr)
    k = k % n
    reverse_list_inplace(arr)
    reverse_list_inplace(arr[:k])
    reverse_list_inplace(arr[k:])
    return arr
