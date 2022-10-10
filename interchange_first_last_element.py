from hashlib import new
from tkinter import NE


def swaplist(New_list):
    size = len(New_list)

    temp = New_list[0]
    New_list[0]=New_list[size-1]
    New_list[size-1]=temp

    return New_list
    
list = [1,2,3,4,5,6,7,8,9,10]
print(swaplist(list))