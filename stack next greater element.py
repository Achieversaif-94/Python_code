def next_greater(arr):
    result = [-1] * len(arr)
    stack = []
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)
    return result

arr = [4, 5, 2, 10, 8]
print(next_greater(arr))