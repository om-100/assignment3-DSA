"""LINEAR SEARCH"""
def linear_search(lists, item):
    found = False
    index = -1
    for i in range(len(lists)):
        if lists[i] == item:
            found = True
            index = i
    if found:
        print('Found at index ' + str(index))
    else:
        print('Not Found')
lists = [1, 2, 3,4,5,6,7,8,9]
item = 4
linear_search(lists, item)