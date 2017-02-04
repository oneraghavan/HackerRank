def max_sum(integers):
    memory = []

    def compute_max_sum(integers):
        current_integer_index = len(integers) - 1

        max_till_previous_element = memory[current_integer_index - 1][0]

        current_element = integers[-1]

        max_till_now = (max_till_previous_element + current_element, False) \
            if max_till_previous_element > 0  else (current_element, True)
        memory.append(max_till_now)

    memory.append((-2,True))

    for index in range(1,len(integers) - 1):
        compute_max_sum(integers[:index +1 ])

    return max([tup[0] for tup in memory])


print max_sum([-2, -3, 4, -1, -2, 1, 5, -3])
