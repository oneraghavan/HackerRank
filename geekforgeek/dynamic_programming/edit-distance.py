def edit_distance(from_string, to_string, m=None, n=None):
    m = len(from_string) - 1
    n = len(to_string) - 1
    if m == 0:
        memory[(from_string,to_string)] = n
        return n

    if n == 0:
        memory[(from_string, to_string)] = m
        return m

    if (from_string[m] == to_string[n]):
        if memory.has_key((from_string,to_string)):
            return memory[(from_string,to_string)]
        else:
            distance = edit_distance(from_string[:-1], to_string[:-1])
            memory[(from_string, to_string)] = distance
            return distance
    else:
        if memory.has_key((from_string,to_string)):
            return memory[(from_string,to_string)]
        else:
            distance = 1 + min(edit_distance(from_string, to_string[:-1]), edit_distance(from_string[:-1], to_string),
                              edit_distance(from_string[:-1], to_string[:-1]))
            memory[(from_string, to_string)] = distance
            return distance

str1 = "sunday"
str2 = "saturday"
memory = dict()
print edit_distance(str1, str2,memory)
