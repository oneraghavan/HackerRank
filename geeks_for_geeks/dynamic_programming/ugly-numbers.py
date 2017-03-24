def get_ugly_number(n):
    ugly_numbers = [1]
    not_reached = True
    counter_for2 = 0
    counter_for3 = 0
    counter_for5 = 0
    while not_reached :

        next_num2 = 2 * ugly_numbers[counter_for2]
        next_num3 = 3 * ugly_numbers[counter_for3]
        next_num5 = 5 * ugly_numbers[counter_for5]

        next_ugly_number = min(next_num2,next_num3,next_num5)

        ugly_numbers.append(next_ugly_number)
        if(len(ugly_numbers) == n + 1):
            not_reached = False

        if(next_ugly_number == next_num2):
            counter_for2 = counter_for2 + 1
        if(next_ugly_number == next_num3):
            counter_for3 = counter_for3 + 1
        if(next_ugly_number == next_num5):
            counter_for5 = counter_for5 + 1

    print ugly_numbers
    return ugly_numbers[n-1]

print get_ugly_number(150)