# cou=["variable","data type","conversion","operator","if else","loop"]
# print(cou)
# Habits=["dancing","singing","reading books","playing"]
# print("Habits")
# companies=["tcs","bhel","relince","hexaware"]
#     print(companies)
# councile_member=[FM,Disco,T&P]
# prinT(councile_member)

#mixed_list = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
# index=0
# #length=len(mixed_list)
# while index<len(mixed_list):
#     print(mixed_list[index])
#     index+=1
#value = "shahnaaz"
# mixed_list.remove(12)
# mixed_list.pop(3)
# print(mixed_list)

# i=10
# a=[]
# while i>0:
#     num=input("enter a number : ")
#     a.append(num)
    
#     i=i-1
# print(a)
# n=input("enter a number: ")
# j=0
# while j<len(a):
#     if n in a:
#         print("yes")
#         break
#     else:
#         print("no")
#         break
#     j+=1


# i=5
# list=[]
# largest=list[0]
# while i<len(list):
#     a=int(input("enter a number"))
#     list.append(a)
#     while i>0:
#         if list[i]>largest:
#             lrgest=list[i]
#         i-=1
# print("largest number=",largest)
    
num=[66,89,99,956,8,33,90,67,876,896]
i=0
max=num[0]
while i<len(num):
    m=num[i]
    if m>max:
        max=m
    i+=1
print(max)
j=0
b=num[j]
while j<len(num):
    if num[j]<b:
        b=num[j]
    j+=1
print(b)