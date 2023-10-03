def sum_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

start_num = int(input("Enter start number: "))
end_num = int(input("Enter end number: "))

result = sum_range(start_num, end_num)
print(f"Sum of numbers {result}")
