def check_vowel_consonents(string):

    input="a,e,i,o,u,A,E,I,O,U"
    vowel=0
    conso=0
    for i in range(len(string)):

        if string[i] not in  input :
            if ord(string[i])>=97 and  ord(string[i])<=122:

                conso+=1

            elif ord(string[i])>=65 and ord(string[i])<=90:
                conso+=1

        else:
            vowel+=1

    return print("conso {} vowel {}".format(conso,vowel))







chk=check_vowel_consonents("Hello")
print(chk)