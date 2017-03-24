def find_update_operations_max_element(min_element, max_element, operations, not_equaled, memory):
    difference = max_element - min_element
    if memory.has_key(difference):
        operations = memory[difference]
        return min_element, min_element, operations, False
    if (difference > 4):
        steps = difference / 5
        operations = operations + steps
        max_element = max_element - (steps * 5)
        return find_update_operations_max_element(min_element, max_element, operations, True, memory)
    elif (difference > 1):
        steps = difference / 2
        operations = operations + steps
        max_element = max_element - (steps * 2)
        return find_update_operations_max_element(min_element, max_element, operations, True, memory)
    elif (difference > 0):
        operations = operations + 1
        max_element = max_element - 1
        return operations, max_element, True
    else:
        return operations, max_element, False


def update_operations(difference, memory):
    if memory.has_key(difference):
        operations = memory[difference]
        return operations

    steps = (difference / 5) + ((difference % 5) / 2) + ((difference % 5) % 2)
    memory[difference] = steps
    return steps

def find_min_operation_to_equalize(candy_counts, memory):
    operations = 0
    candy_counts.sort()
    for indix in range(2, len(candy_counts) + 1):
        current_list = candy_counts[:indix]
        min_element = min(current_list)
        max_element = current_list[-1]

        operations = operations + update_operations(max_element-min_element,memory)
        # while not_equaled:
        #     operations, max_element, not_equaled = find_update_operations_max_element(min_element, max_element,
        #                                                                               operations, not_equaled, memory)

        candy_counts[indix - 1] = min_element

    return operations


num_testcases = int(raw_input())

for i in range(1,num_testcases+1):
    raw_input()
    memory = dict()
    candy_counts = [int(i) for i in raw_input().strip().split()]
    print find_min_operation_to_equalize(candy_counts,memory)

# memory = dict()
# print find_min_operation_to_equalize(
#     [53, 361, 188, 665, 786, 898, 447, 562, 272, 123, 229, 629, 670, 848, 994, 54, 822, 46, 208, 17, 449, 302, 466, 832,
#      931, 778, 156, 39, 31, 777, 749, 436, 138, 289, 453, 276, 539, 901, 839, 811, 24, 420, 440, 46, 269, 786, 101, 443,
#      832, 661, 460, 281, 964, 278, 465, 247, 408, 622, 638, 440, 751, 739, 876, 889, 380, 330, 517, 919, 583, 356, 83,
#      959, 129, 875, 5, 750, 662, 106, 193, 494, 120, 653, 128, 84, 283, 593, 683, 44, 567, 321, 484, 318, 412, 712, 559,
#      792, 394, 77, 711, 977, 785, 146, 936, 914, 22, 942, 664, 36, 400, 857], memory)
