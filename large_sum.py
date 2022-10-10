def large_sum(arr,len):
    n = int(input("enter the value : "))
    count = 0
    if(n<=len):
        for i in range(0,n):
            count+=arr[i]
        return count            
            

def sort(arr,len):
    for i in range(0,len):
        for j in range(0,i+1):
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp       
    return arr
          

arr = [7,1,4,9,4,5,0]
len = len(arr)
print("------before sort------")
print(arr)
print("\n------After sort------")
sorted_arr = sort(arr,len)
print(sorted_arr)

sol = large_sum(sorted_arr,len)
print(sol)