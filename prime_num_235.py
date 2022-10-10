def ispossible(arr,target):
    if(target == 1):
        return True
    for i in arr:
        if(target%i == 0):
            # we cant retive the value in decimal or 
            # fractional so we can get in whole number 
            return ispossible(arr,target/i)
    return False

arr = [2,3,5]
target = 24
soln = ispossible(arr,target)
print(soln,"\n")
