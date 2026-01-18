import math


def checkprime(num):

    newlist=[]


    for val in num:

        if val in  num:



                val1=math.sqrt(val)
                val1=math.ceil(val1)
                print("vl1 val",val1,val)
                start=3
                end=val1
                track=0
                while(start<=end):
                    print("***",start,val,track)
                    rem=start%val
                    print("rem",rem)

                    if val%2!=0 and val%start!=0:

                        track=1
                    else:
                        track=0

                    if track==0:
                        break
                    start+=1
                if track == 1:
                    newlist.append(val)

    return newlist

chk=checkprime([3,6,7,8,9,10,11])
print(chk)














