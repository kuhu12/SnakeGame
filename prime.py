n=int(input("Enter the number to check whether it is prime or not"))
c=0
for i in range(1,n+1):
    if(n%i==0):
        c+=1

if(c==2):
    print("prime")
else:
    print("not prime")




