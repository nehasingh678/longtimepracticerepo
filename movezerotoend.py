def movezero(list1):


    for i in range(len(list1)):

        if list1[i] == 0:
            list1.pop(i)
            list1.append(0)

    return list1

chk=movezero([5,0,9,0,6,0,0])
print(chk)

