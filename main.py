def is_palindrome(number):
    num_str = str(number)

    return num_str == num_str[::-1]

num = int(input('Enter number: '))

if is_palindrome(num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")