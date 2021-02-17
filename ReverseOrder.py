i=0
list1=[]
while i<10:
    a=input("enter a number: ")
    list1.append(a)
    i+=1
print(list1)
list2=[]
j=len(list1)-1
print(j)1
while j>=0:
    list2.append(list1[j])
    j-=1
print(list2)