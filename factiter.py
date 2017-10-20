def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial of %d is %d"%(num,fact));
numb=int(input("Enter the number to evaluate n!"))
factorial(numb)
