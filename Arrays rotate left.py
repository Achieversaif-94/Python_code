def rotate_left(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]

arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_left(arr, k))