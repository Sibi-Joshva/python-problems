def palindrom(s1):
    s2 = s1[::-1]
    
    if(s2==s1):
        return True
    else:
        return False

s1 = "sibis"
sol = palindrom(s1)
print(sol)