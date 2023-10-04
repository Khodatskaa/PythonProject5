def find_min_of_five(a, b, c, d, e):
    min_value = min(a, b, c, d, e)
    return min_value

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
num4 = int(input('Enter fourth number: '))
num5 = int(input('Enter fifth number: '))

result = find_min_of_five(num1, num2, num3, num4, num5)
print(f"The minimal number is {result}")