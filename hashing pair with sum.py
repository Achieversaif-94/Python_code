def pairs_with_sum(arr, target):
    seen = set()
    pairs = []
    for num in arr:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

arr = [1, 5, 3, 7, 2, 8]
target = 10
print(pairs_with_sum(arr, target))