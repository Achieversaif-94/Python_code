# Exercise 1: Function that returns only even numbers from a list
def get_evens(numbers):
    return [n for n in numbers if n % 2 == 0]

print(get_evens([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]


# Exercise 2: Dictionary of 3 students with marks, print the topper
students = {
    "Alice": 88,
    "Bob": 95,
    "Charlie": 76
}
topper = max(students, key=students.get)
print("Topper:", topper, "with", students[topper], "marks")


# Exercise 3: Print only words longer than 4 characters
words = ["hi", "hello", "world", "cat", "python", "sky"]
for word in words:
    if len(word) > 4:
        print(word)