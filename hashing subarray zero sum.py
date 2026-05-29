def has_zero_sum_subarray(arr):
    seen = set()
    seen.add(0)
    total = 0
    for num in arr:
        total += num
        if total in seen:
            return True
        seen.add(total)
    return False

print(has_zero_sum_subarray([3, 4, -7, 1, 2]))
print(has_zero_sum_subarray([1, 2, 3]))