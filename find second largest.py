inputs = ['3', '9', 'abc', '7', '1', '9', 'done']
index = 0
largest = None
second = None

while True:
    user_input = inputs[index]
    index += 1

    if user_input == 'done':
        break

    try:
        number = int(user_input)
        if largest is None or number > largest:
            second = largest
            largest = number
        elif second is None or (number > second and number != largest):
            second = number
    except ValueError:
        print("Invalid input")

print("Largest is", largest)
print("Second largest is", second)