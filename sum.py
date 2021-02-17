num=int(input("enter the number: "))
list=[]
i=1
sum=0
while i<num:
    a=int(input("enter a number"))
    list.append(a)
    sum+=a
    i+=1
print(sum)