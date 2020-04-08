# Given an unsorted array and a number n, find if there exists a pair of elements in the array whose difference is n.
import sys


def binary_search(arr, val):
    if (len(arr) == 0):
        return None
    n = int((len(arr) - 1) / 2)
    if arr[n] == val:
        return arr[n]
    elif val > arr[n]:
        return binary_search(arr[n + 1:len(arr)], val)
    elif val < arr[n]:
        return binary_search(arr[0:n], val)
    return None


def find_pair(arr, diff: int):
    arr = sorted(arr)  # O(nlogn) heap sort
    for i in range(0, len(arr)):  # O(n)
        n = arr[i]
        delta = binary_search(arr, n + diff)  # O(log(n))
        if delta is not None:
            print("Found {}".format((n, delta)))
            # Tot Complexity O(nlogn) + O(n)*O(log(n)) = 2 O(nlogn) = O(nlogn)
            return
    print("Not Found")


if __name__ == '__main__':
    arr1 = [17, 13, 7, 5, 20, 3, 2, 50, 80]
    diff1 = 4
    find_pair(arr1, diff1)
    arr2 = [90, 70, 20, 80, 50]
    diff2 = 45
    find_pair(arr2, diff2)
