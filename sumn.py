def sum(n):
    if (n==0):
        return 0

    else:
        return n+sum(n-1)
num=int(input("enter the number"))
print("the sum of %d numbers is %d"%(num,sum(num)))
