import random
from typing import List


def binary_search(arr: List[int], value: int, left=None, right=None) -> int:
    """Returns the index of the value element in arr, otherwise -1

    Args:
        arr (List[int]): sorted list of integers
        value (int): integers to be found
        left (int): left index (rec. boundary)
        right (int): right index (rec. boundary)

    Returns:
        int: index of the element
    """
    if left == None or right == None:
        left, right = 0, len(arr) - 1
    assert left <= right
    if left == right:
        if arr[left] == value:
            return left
        return -1

    # left < right here
    mid = (left + right) // 2
    if arr[mid] == value:
        return mid

    if arr[mid] > value:
        return binary_search(arr, value, left, mid - 1)
    else:
        return binary_search(arr, value, mid + 1, right)


def merge(arr1: list, arr2: list) -> list:
    """Merges two sorted lists"""
    result = [0] * (len(arr1) + len(arr2))
    l1, l2 = 0, 0

    while l1 < len(arr1) and l2 < len(arr2):
        if arr1[l1] <= arr2[l2]:
            result[l1 + l2] = arr1[l1]
            l1 += 1
        else:
            result[l1 + l2] = arr2[l2]
            l2 += 1

    # used one of the arrays already
    if l1 == len(arr1):
        while l2 < len(arr2):
            result[l1 + l2] = arr2[l2]
            l2 += 1

    if l2 == len(arr2):
        while l1 < len(arr1):
            result[l1 + l2] = arr1[l1]
            l1 += 1

    return result


def merge_sort(arr: list) -> list:
    """Sorts the list using merge sort algorithm"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def quick_sort(arr: list) -> list:
    """Sorts the list using quick sort algorithm (not in place))"""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less, equal, bigger = [], [], []
    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            bigger.append(element)

    return quick_sort(less) + equal + quick_sort(bigger)


def counting_sort(arr: List[int]) -> list:
    """Sorts the list using counting sort algorithm"""
    if len(arr) <= 1:
        return arr

    max_value = max(arr)
    counts = [0] * (max_value + 1)
    for element in arr:
        counts[element] += 1

    result = []
    for i in range(len(counts)):
        result.extend([i] * counts[i])

    return result


def radix_sort(arr: list[int]) -> list:
    """Sorts the list using radix sort algorithm"""
    if len(arr) <= 1:
        return arr

    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counts = [0] * 10
        for element in arr:
            counts[element // exp % 10] += 1

        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

        result = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            result[counts[arr[i] // exp % 10] - 1] = arr[i]
            counts[arr[i] // exp % 10] -= 1

        arr = result
        exp *= 10

    return arr
