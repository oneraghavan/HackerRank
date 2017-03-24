N = int(raw_input())

right_heap = []
left_heap = []
total_item = 0
iseven = 1
middle_value = None
median = None

import heapq


def remove_item(heap, item):
    heap.remove(item)


def add_item(heap, item):
    heapq.heappush(heap, item)


def pop_and_re_add(heap):
    item = heapq.heappop(heap)
    heapq.heappush(heap, item)
    return item


def normalize_right_left():

    left_length = len(left_heap)
    right_length = len(right_heap)
    if abs(left_length - right_length) > 1:
        if left_length > right_heap:
            while len(left_heap) - len(right_heap) > 1:
                heapq.heappush(right_heap, heapq.heappop(left_heap))
        else:
            while len(right_heap) - len(left_heap) > 1:
                heapq.heappush(left_heap, -1 * heapq.heappop(right_heap))


def find_median():
    left_length = len(left_heap)
    right_length = len(right_heap)
    if left_length > right_length:
        return -1 * pop_and_re_add(left_heap)
    elif right_length > left_length:
        return pop_and_re_add(right_heap)
    else:
        if left_length == 0 and right_length == 0:
            return None
        pop_and_re_add(left_heap)
        left_poped = -1 * pop_and_re_add(left_heap)
        right_poped = pop_and_re_add(right_heap)
        new_median = float(float(left_poped+right_poped)/2)
        if new_median == int(new_median):
            new_median = int(new_median)
        return new_median

# def print_as_variable(text):
#     outputtext = str(text) + "\n"


for i in range(0, N):
    tmp = raw_input()
    operation, item = [xx for xx in tmp.split(' ')]
    item = int(item)
    if operation == 'r':
        if median is None:
            print "Wrong!"
        else:
            if item > median:
                if item in right_heap:
                    remove_item(right_heap, item)
                    normalize_right_left()
                    median = find_median()
                    if median is None:
                        print "Wrong!"
                    else:
                        print median
                else:
                    print "Wrong!"
            else:
                if -1 * item in left_heap:
                    remove_item(left_heap, -1 * item)
                    normalize_right_left()
                    median = find_median()
                    if median is None:
                        print "Wrong!"
                    else:
                        print median
                else:
                    print "Wrong!"
    else:
        if median is None:
            add_item(left_heap, -1 * item)
            normalize_right_left()
            median = find_median()
            if median is None:
                print "Wrong!"
            else:
                print median
        else:
            if item > median:
                add_item(right_heap, item)
            else:
                add_item(left_heap, -1 * item)
            normalize_right_left()
            median = find_median()
            if median is None:
                print "Wrong!"
            else:
                print median



