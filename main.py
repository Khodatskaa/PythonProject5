def display_square(side_length, fill_char, is_filled):
    if is_filled:
        for _ in range(side_length):
            print(fill_char * side_length)
    else:
        print(fill_char * side_length)

        for _ in range(side_length - 2):
            print(fill_char + " " * (side_length - 2) + fill_char)

        print(fill_char * side_length)

side_length = int(input('Enter number: '))
fill_char = input('Enter symbol: ')
is_filled = input('Choose true or false: ')

is_filled = is_filled.lower() == 'true'

display_square(side_length, fill_char, is_filled)
