list=[41,73,50,59,36,19]
i=0
b=list[i]
while i<len(list):
    if list[i]<b:
        b=list[i]
    i+=1
print(b)