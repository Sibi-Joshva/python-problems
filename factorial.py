# 5! factorial is 5*4*3*2*1 = 120

n = int(input("Enter the number : "))
result = 1
for i in range(1,n+1):
    result*=i
print("{} is a factorial of {}".format(result,n))