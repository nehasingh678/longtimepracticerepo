def check_divisor(num):


    num1=num//2
    new_list=[]
    rem=0
    num2=2
    total=0
    while(num2<=num1):
        if num%num2==0:
            new_list.append(num2)
            print("newlist",new_list)
        num2+=1
        print("num2",num2)

    total=sum(new_list)+1

    return total

chk=check_divisor(28)
print("*******",chk)














































