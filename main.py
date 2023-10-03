def draw_line(symbol, length, direction):
    if direction == 'horizontal':
        line = symbol * length
        print(line)
    elif direction == 'vertical':
        for _ in range(length):
            print(symbol)
    else:
        print('Invalid direction')

symbol = input('Enter a symbol: ')
length = int(input('Enter line length: '))
direction = input('Enter direction (horizontal or vertical): ')

draw_line(symbol, length, direction)
