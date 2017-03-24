def find_min_candies(ranks):
    candies = [1 for i in ranks]

    indixes = range(1, len(ranks))
    for i in indixes:
        if ranks[i] > ranks[i-1]:
            candies[i] = candies[i-1]+1

    for i in indixes[::-1][1:]:
        if ranks[i] > ranks[i+1]:
            candies[i] = max(candies[i],candies[i+1]+1)

    return sum(candies)

num_students = int(raw_input())
ranks = []

for i in range(0, num_students):
    rank = int(raw_input())
    ranks.append(rank)
print find_min_candies(ranks)

# print find_min_candies([1, 2, 2])