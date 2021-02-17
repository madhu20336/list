num=[23,4,56,78,9,8,55,34,55,666,1234]
i=0
largest=num[0]
while i<len(num):
    m=num[i]
    if m>largest:
        largest=m
    i+=1
print(largest)
j=0
smallest=num[j]
while j<len(num):
    if num[j]<smallest:
        smallest=num[j]
    j+=1
print(smallest)