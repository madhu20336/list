i=10
a=[]
while i>0:
    num=input("enter a number : ")
    a.append(num)
    
    i=i-1
print(a)
n=input("enter a number: ")
j=0
while j<len(a):
    if n in a:
        print("yes")
        break
    else:
        print("no")
        break
    