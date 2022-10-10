def b_list(v):

	val = [v]

	return val



def print_b_value(n):
	
	if(n>1):
		print_b_value(n//2)

	print(n%2,end = "")


n = 8

for i in range(0,n+1):
	x = print_b_value(i)
	print("\n",end="") 
	print(b_list(x))

