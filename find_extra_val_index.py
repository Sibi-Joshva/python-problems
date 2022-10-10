def check_value(a,b,n):
    for i in range(0,n):
        if(a[i] != b[i]):
            return i
    
    return n

a = [2,4,6,8,9,10,12]
b = [2,4,6,8,10,12]

lenght  = len(b)

index = check_value(a,b,lenght)
print(index)