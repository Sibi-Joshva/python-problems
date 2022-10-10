def sort(list):
    for i in list:
        for j in range(i+1,len(list)):
            if(list[i]==list[i+1]):
                print(list[i],list[j])

def merge(l1,l2):
    list = l1 + l2
    return list

l1 = [1,2,4]
l2 = [1,3,4]

merge_list = merge(l1,l2)
sort_list = sort(merge_list)

print(merge_list)
#print(sort_list)