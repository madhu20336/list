dic={"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50}
first={}
second={}
def decending(first1):
    for j in dic:
        if dic[j]>first1:
            first[j]=dic[j]
    return(first)
for k in dic:
    decending(dic[k])
first["param"]=dic["param"]
print(first)
def ascending(first2):
    for j in dic:
        if dic[j]<first2:
            second[j]=dic[j]
    return(second)
for k in dic:
    ascending(dic[k])
second["deepak"]=dic["deepak"]
print(second)
