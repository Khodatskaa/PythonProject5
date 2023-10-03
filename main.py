def is_lucky_number(number):
    if len(str(number)) != 6:
        return False

    first_half = number // 1000
    second_half = number % 1000

    sum_first_half = sum(int(digit) for digit in str(first_half))
    sum_second_half = sum(int(digit) for digit in str(second_half))

    return sum_first_half == sum_second_half

number = int(input("Enter your number: "))

if is_lucky_number(number):
    print(f"{number} is a lucky number.")
else:
    print(f"{number} is not a lucky number.")
