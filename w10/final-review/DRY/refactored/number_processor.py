def process_numbers(numbers, operation):
    return [operation(num) for num in numbers]


numbers = [1, 2, 3, 4, 5]

squared_numbers = process_numbers(numbers, lambda x: x**2)
doubled_numbers = process_numbers(numbers, lambda x: x * 2)

print("Squared numbers:", squared_numbers)
print("Doubled numbers:", doubled_numbers)
