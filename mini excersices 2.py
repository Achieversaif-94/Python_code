# Exercise 1: Function that takes a list of strings and returns only those that start with a vowel
def starts_with_vowel(words):
    vowels = 'aeiouAEIOU'
    return [w for w in words if w[0] in vowels]

print(starts_with_vowel(["apple", "banana", "orange", "grape", "umbrella"]))
# ['apple', 'orange', 'umbrella']


# Exercise 2: Dictionary of 3 products with prices, print the cheapest
products = {
    "Laptop": 55000,
    "Mouse": 799,
    "Keyboard": 2500
}
cheapest = min(products, key=products.get)
print("Cheapest:", cheapest, "at", products[cheapest])


# Exercise 3: Loop through a list of numbers and print only those divisible by 3
numbers = [3, 7, 9, 14, 18, 21, 25]
for n in numbers:
    if n % 3 == 0:
        print(n)