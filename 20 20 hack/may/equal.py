array = [2,2,3,7]
steps = 0

def normalize(list):
    minitem , maxitem = min(list) , max(list)
    list.remove(maxitem)
    if maxitem - minitem >= 5 :
        list = [num + 5 for num in list]
    elif maxitem - minitem >= 2:
        list = [num + 5 for num in list]
    elif maxitem - minitem >= 1:
        list = [num + 5 for num in list]
    list.append(maxitem)

while(min(array) < max(array)):
    steps = steps + 1
    normalize(array)

print steps