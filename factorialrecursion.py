def ffactrecurrsion(number):

    if number == 1:
        return 1

    return number*ffactrecurrsion((number-1))



chk=ffactrecurrsion(5)
print(chk)
