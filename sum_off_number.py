def sum_of_number(num):
    total_sum=0

    while(num):

        quot=num//10
        rem=num%10
        num=quot
        total_sum+=rem

    return total_sum


chk=sum_of_number(12334)
print(chk)

