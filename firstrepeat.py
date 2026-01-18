import sys

def find_first_repeat(string):
    dict1={}

    for i in range(len(string)):
        if string[i] not in dict1.keys():
            dict1[string[i]]=[1]

        else:

            dict1[string[i]][0]+=1
            dict1[string[i]].append(i)

    minimum=sys.maxsize

    for j in range(len(string)):
        val=string[j]

        if dict1[val][0]>1 and minimum == sys.maxsize:
            minimum=string[j]
            key=dict1[val]
        elif  dict1[val][0] >1 and minimum > dict1[val][1]:
            minimum=dict1[val][1]
            key=val

    return key


chk=find_first_repeat([10, 5, 3, 4, 3, 5, 6])
print(chk)





