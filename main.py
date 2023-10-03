def display_odd_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number)

start_number = int(input('Enter start number: '))
end_number = int(input('Enter start number: '))
display_odd_numbers(start_number, end_number)