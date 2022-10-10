def swaplist(list,pos0,pos1):
    list[pos0], list[pos1] = list[pos1], list[pos0]
    return list

list = [1,2,3,4,5]
position0,position1 = 1,3
print(swaplist(list,position0-1,position1-1))