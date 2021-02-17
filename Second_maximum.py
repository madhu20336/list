num=[55,7,48,99,100,999]
i=0
max=num[1]
while i<len(num):
    m=num[i]
    if m>max:
      max=m
    i+=1
num.remove(max)
index=0
max1=num[0]
while index<len(num):
    n=num[index]
    if n>max1:
        max1=n
    index+=1
print(max1)
