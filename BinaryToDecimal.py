List=[1,0,0,1,1,0,1,1]
index=0
A=0
sum=0
length=len(List)-1
while index<len(List):
    M=List[length]
    A=(2**index)*M
    length-=1
    index+=1
    sum+=A
print(sum)
