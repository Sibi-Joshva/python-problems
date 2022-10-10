string = input("Enter the string : ")
vowel = 0
consonent = 0
for i in string:
    if(i in ('a','e','i','o','u','A','E','I','O','U')):
        vowel+=1
    elif i.isalpha():
        consonent+=1
print("count of vowel {} \ncount of consonent {}".format(vowel,consonent))