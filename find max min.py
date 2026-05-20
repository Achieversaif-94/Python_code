inputs = ['7', '2', 'bob', '10', '4', 'done']
index = 0
largest = None
smallest = None
while True:
    user_input = inputs[index]
    index += 1

    if user_input == 'done':
        break

    try:
        number = int(user_input)
        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number
    except ValueError:
        print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)