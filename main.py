def prod_range(num1, num2):
    if num1 < num2:
        lower = num1
        upper = num2
    else:
        lower = num2
        upper = num1

    product = 1

    for number in range(lower, upper + 1):
        product *= number

    return product

num1 = int(input('Enter number: '))
num2 = int(input('Enter number: '))

result = prod_range(num1, num2)

print(f"Product of numbers between {num1} and {num2} is {result}.")
