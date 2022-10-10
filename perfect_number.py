num = int(input())
sum = 1
for x in range(2,num):
    if(num%x==0):
        sum += x
if(sum == num):
    print("%d is a perfect number"%num)
else:
    print("%d is not a perfect number"%num)
