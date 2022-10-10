string = input("enter the string ")

result =""
for i in string:
    if(i!=' '): #if the given char is not a blank space we store in result
        result+=i
print(result)