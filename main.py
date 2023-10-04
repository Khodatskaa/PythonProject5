def count_digits(number):
    num_str = str(number)
    digit_count = len(num_str)
    return digit_count

num = int(input('Enter number: '))
digit_count = count_digits(num)
print(f"The number of digits is {digit_count}.")
