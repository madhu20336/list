numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
length=len (numbers)
count=0
less_than20=0
more_than40=0
while count<length:
    num=numbers[count]
    if num<20:
        less_than20+=1
    else:
        more_than40+=1
    count+=1
print("num less than 20 :"+str(less_than20))
print("num more than 40 :"+str(more_than40))