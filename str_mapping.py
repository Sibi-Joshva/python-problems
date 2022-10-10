def strcheck(s1,s2):
    if(len(s1)!=len(s2)):
        return False
    hs ={}
    for i in range(len(s1)):
        try:
            if(hs[s1[i]] != s2[i]):
                return False
        except KeyError:
            hs[s1[i]]=s2[i]
    return True

s1 = input("")
s2 = input("")
sol = strcheck(s1,s2)
print(sol)



