def reverse_word(s):

    s=s.split()
    print(s)
    newstring=""
    for  val in s:

        start=0
        end=len(val)-1
        tmp=""

        while(end>=start):

            tmp+=val[end]
            end-=1

        newstring+=tmp+" "


    return newstring

chk=reverse_word("this is my life")
print(chk)





