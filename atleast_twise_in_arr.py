def check_arr(arr,n):
    arr.sort()
    for i in range(0,n-1):
        if(arr[i] == arr[i+1]):
            return True
        return False
        

arr = [3,4,5,3,6,]
l = len(arr)

print(check_arr(arr,l))