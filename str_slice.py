#slicing a given input

from xmlrpc.client import boolean


mail = input("Enter yout mailID :")
print(mail)

print('\n')
name = mail[:mail.index('@'):]
print('name of the email user is : ',name)
#sanathkumar@gmail.com

host = mail[mail.index('@')+1:mail.index(".")]
print('host of mail user is : ',host)

#string format
output = "username is {} and the host name is {}"
print(output.format(name,host))

#format()

#list  =  set of element it may str,char,int,boolean,float
#tuple = 

#var_name = [ list ]
#var_name = ( tuple )
#var_name = { dict }

a = b+c
b = 10
c =10

x = y+z
y = "hai"
z = "welcome"

x= haiwelcome single action in different ways



# hai all welcome to this meet
#arr [] = {1,2,3,4,5,6,7,8,9,10}

#str operations
#concat - join the strings hi + all = hiall
#str cpy - 
#str rev abc -cba
#str slice - seprate
#str len - find the lenth of the char or str


x = "sanath"
print (x[:3])