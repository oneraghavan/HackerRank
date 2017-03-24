def get_optimised_array(integers):
    solution = []
    solution.append([0,0])
    for num in range(0,len(integers)-1):
        sol1 = max(solution[num][0],solution[num][1]+abs(integers[num]-1))
        sol2 = max(solution[num][0]+abs(integers[num+1]-1),solution[num][1]+abs(integers[num]-integers[num+1]))
        solution.append([sol1,sol2])

    return max(solution[len(integers)-1])

print get_optimised_array([100, 2, 100, 2, 100])




