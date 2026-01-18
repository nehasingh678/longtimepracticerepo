def intersection(list1,list2):

    dict2={}
    newlist=[]

    for val in list2:

        dict2[val]=1


    for i in list1:
        if i not in dict2.keys():
            pass

        else:

            newlist.append(i)


    return newlist

chk=intersection(list1 = [1, 2, 4, 5, 3, 6],
list2 = [3, 4, 7, 8, 9, 0])

print(chk)

