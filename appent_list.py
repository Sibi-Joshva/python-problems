list = [1,2,3,4,5]
val = [10]#value should be given in []
index = 2

def insert_list(x,val,index):
    y = x[:index] + val + x[index:]
    #from x 0 to given index travel
    #add the given value
    #from the current index it goes to end
    return y
    
F_list = insert_list(list,val,index)
print(F_list)