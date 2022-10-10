fam1 = ["Mathi","Buvana","Sibi","Abi"]
print(fam1,"\n")

fam2 = ["Baskaran","Maheshwari","Shree","Daniel"]
print(fam2,"\n")

fam3 = ["Rajan","Santhi","Kathirraja","Isha"]
print(fam3,"\n")

fam4 = ["kamalam","vadivel"]
print(fam4,'\n')

while (0,5):
    print("Happy family !!")
    name = input('Enter the name : ').strip()#remove unwanted space in a string
    if name in fam1:
        print("YES the person {} belong to fam1".format(name))
        remove = input('would you want to remove the name ? (y/n) : ')
        if(remove == 'y'):
            fam1.remove(name)
            print(fam1,'\n')

    if name in fam2:
        print("YES the person {} belong to fam2".format(name))
        remove = input('would you want to remove the name ? (y/n) : ')
        if(remove == 'y'):
            fam2.remove(name)
            print(fam2,'\n')

    if name in fam3:
        print("YES the person {} belong to fam3".format(name))
        remove = input('would you want to remove the name ? (y/n) : ')
        if(remove == 'y'):
            fam3.remove(name)
            print(fam3,'\n')
    
    if name in fam4:
        print("YES the person {} belong to fam4".format(name))
        remove = input('would you want to remove the name ? (y/n) : ')
        if(remove == 'y'):
            fam4.remove(name)
            print(fam4,'\n')

    print("hi {}".format(name))

    join = input("In which family you want to join ? \nfam1\nfam2\nfam3\nfam4\n")
    print(join)

    if(join == '1'):
        fam1.append(name)
        print(fam1)
    
    elif(join == '2'):
        fam2.append(name)
        print(fam2)
    
    elif(join == '3'):
        fam3.append(name)
        print(fam3)
    
    elif(join == '4'):
       fam4.append(name)
       print(fam4)
    
    else:
        print('No problem ..see you later !!')


    print("\n")    

