#sample input is a = [1,2,3,4,5,6,7] 
#b = [1,2,3,4,5,7]
#sample o/p = 5

def find_element(a,b):
    for i in range(len(b)):
        for j in range(len(a)):
            if(b[i] == a[j]):
                continue 
            else:
                x = a.index(a)
                return x

a = [2,4,6,8,9,10,12]
b = [2,4,6,8,10,12]
sol = find_element(a,b)
print(sol)

