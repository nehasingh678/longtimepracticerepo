def remove_all_vowel(s):
    newstring=""
    vowelst='a,e,i,o,u'
    #s=s.split()

    for i in range(len(s)):
        if s[i] not in vowelst:

            newstring+=s[i]

    return newstring


chk=remove_all_vowel("this is my world")
print(chk)



