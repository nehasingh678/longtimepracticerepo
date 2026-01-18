def sort_on_order(s):

    small=[0]*26
    caps=[0]*26


    for i in range(len(s)):

        vaal=ord(s[i])-ord('a')
        if vaal>=0:
            small[vaal]+=1
        else:
            vaal=abs(vaal)
            print("negative",vaal )
            caps[vaal]+=1

    newstring=''

    for i in range(26):
        smallvar=chr(97+i)*small[i]
        newstring+=smallvar
        caps1=chr(65+i)*caps[i]
        newstring+=caps1

    return newstring

chk=sort_on_order("Happy")
print(chk)








