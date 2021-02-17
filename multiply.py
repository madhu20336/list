num=int(input("enter the number: "))
list=[]
i=0
multi=1
while i<num:
    a=int(input("enter a number: "))
    list.append(a)
    multi*=a
    i+=1
print(multi)