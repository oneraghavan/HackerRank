def find_num_candies(digits):
    sub_strings = []
    sub_strings.append(digits[0])
    last_added_count = 1
    for i in range(1, len(digits)):
        current_digits = digits[i]
        last_added_digits = sub_strings[-last_added_count:]
        new_digits = [current_digits]
        for digit in last_added_digits:
            new_digits.append(str(digit) + str(current_digits))
        last_added_count = len(new_digits)
        sub_strings = sub_strings + new_digits
    print sub_strings
    return sum([int(i) for i in sub_strings])


def get_digits(numbers):
    digits = []
    while numbers:
        digit = numbers % 10
        digits.append(digit)
        numbers //= 10
    return digits

# numbers = raw_input()
numbers = 5312
digits = get_digits(numbers)
print find_num_candies(digits[::-1])