#Magic number

#check is sum of all digit equal to 1


def magic(num):
    sum=0
    while(num>0):
        sum=sum+(num%10)
        num=int(num/10)
    print(sum)
    if(len(str(sum))>1):
        magic(sum)
    if(sum==1):
        print("Its a magic number")



magic(173)

