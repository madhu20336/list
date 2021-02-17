List=input("enter a name: ")
index=0
N=-1
while index < len(List) :
    M=List[index]
    A=List[N]
    if M==A:
        N=N-1
        K=List
    else:
        print("it is not palindrome")
        break
    index+=1
    print(K,"it is palindrome")
    break
     
      

