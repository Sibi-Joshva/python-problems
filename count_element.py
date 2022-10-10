list = [1,6,2,3,5,6,4,3,3,4]
value = 3
count = 0 
if(value in list):
    for i in list:
        if(value == list[i]):
            count+=1
else:
    print("Enter valid number")

print(count)