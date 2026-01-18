def find_missing_numberr(list1):

    sumoflist1=sum(list1)
    start=1
    total_sum=0
    while(start<=list1[len(list1)-1]):
        total_sum+=start
        start+=1


    difff=total_sum-sumoflist1
    print(total_sum,sumoflist1)
    return difff


chk=find_missing_numberr([1, 2, 4, 5, 6])
print(chk)


