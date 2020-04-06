from heapq import heapify, heappop, heappush


def find_kth_largest_element(arr):
    print(arr)
    heapify(arr)
    for i in range(0, k + 1):
        heappop(arr)
    print(arr[0])


def find_kth_smallest_element(arr):
    print(arr)
    h = []
    for i in arr:
        heappush(h, -i)
    for i in range(0, k + 1):
        heappop(h)
    print(-h[0])


if __name__ == '__main__':
    k = 4
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
