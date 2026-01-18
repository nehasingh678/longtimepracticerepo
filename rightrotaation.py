def rightrotation(list1,k):

    length=len(list1)-k-1
    start=0
    trck=0
    newliist=[]
    while(trck<=length):

        val=list1[start]
        list1.pop(start)
        newliist.append(val)

        #start+=1
        list1.append(val)

        trck+=1

    print(list1)

    #list1=list1+newliist
    return list1

chk=rightrotation([1,2,3,4,5],2)
print(chk)







