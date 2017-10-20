num=int(input("enter the number of terms"))
first=0
second=1
n=0
for i in range(0,num):
    if(i<=1):
        n=i
    else:
        n=first+second
        first=second
        second=n
    print(n)
        
