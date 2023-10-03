def find_max_of_four(a, b, c, d):
    max_value = max(a, b, c, d)
    return max_value

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
num4 = int(input('Enter fourth number: '))

result = find_max_of_four(num1, num2, num3, num4)
print(f"The maximal number is {result}")
