i=int(input("enter a number:  "))
num = i
List=[]
while i>0:
    number=int(input("enter the number of list: "))
    List.append(number)
    i-=1
print(List)
odd_number=0
even_number=0
positive_number=0
negative_number=0
zero=0
j= num - 1
while j>=0:
    if List[j]>0:
        positive_number+=1
    if List[j]<0:
        negative_number+=1
    if List[j]==0:
        zero+=1
    if List[j]%2==0:
        even_number+=1
    else:
        odd_number+=1
    j-=1
print("even: ",even_number)
print("odd: ",odd_number)
print("positive: ",positive_number)
print("negative: ",negative_number)
print("zero: ",zero)