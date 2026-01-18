def nonrepeat(s):
    dict1={}
    for i in range(len(s)):

        if s[i] not in dict1.keys():

            dict1[s[i]]=[i,1]

        else:
            dict1[s[i]][1]+=1


    min=-1
    for key in dict1.keys():

        if min==-1 and dict1[key][1]==1 :
            min=dict1[key][0]
            item=key

        elif min>dict1[key][0]:
            min = dict1[key][0]
            item = key

    return min

x=nonrepeat("leetcodelltcod")
print(x)





