def check_pair(s):
    dict1={}
    newlist=[]
    for val in s:
        if val not in dict1.keys():
            dict1[val]=1

    for i in range(len(s)):
        x=s[i]-6
        if s[i] in dict1.keys() and x in dict1.keys():
            tmp=(s[i],x)
            newlist.append(tmp)


    return newlist

chk=check_pair([1, 5, 7, -1, 5])
print(chk)






