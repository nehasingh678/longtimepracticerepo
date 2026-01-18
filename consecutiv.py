def check_conse(num):

    num=sorted(num)
    print(num)
    staarrt=0
    track=0
    comp_num=0

    for i in range(len(num)-1):

        if num[i]+1 == num[i+1]:
            print("nummmm",num[i])
            staarrt+=1
            print("ttt",staarrt)
        elif num[i]+1 !=num[i+1]:

            if comp_num < staarrt:
                comp_num
                comp_num=staarrt+1
            staarrt=0



    if staarrt ==0 and comp_num ==0:
        return  1
    elif staarrt !=0 and comp_num < staarrt:
        comp_num=0
        comp_num+=staarrt+1
        return comp_num

chk=check_conse([100,2,3,8,9,0,1,2,3,100,101,102,103,104])
print(chk)





















