list1 = [1,2,3,4,5,6,7,8,9,10]

def rev(l):
    r = []
    for i in l:
        r.insert(0, i)
    return r

r = rev(list1)
print(r)
