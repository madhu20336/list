list1=[1,4,6,8,4,5,1,4,6,8,5,7,8,9,1,6,2,5,6,0,9,4,4]
new_list=[]
i=0
while i<len(list1):
    if list1[i] not in new_list:
        new_list.append(list1[i])
    i+=1
print(new_list)
