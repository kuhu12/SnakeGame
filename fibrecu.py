def fib(n):
    if(n<=1):
        return n
    else:
        return(fib(n-1)+fib(n-2))

num=int(input("enter the no.of terms"))
if(num<=0):
    print("enter a positive number")
else:
    for i in range(0,num):
        print(fib(i))
        
