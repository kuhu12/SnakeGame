def menu():
    print("\nMenu\nSelect '+' for addition\nSelect '-' for subtraction\nSelect '*' for multiplication\nSelect '/' for division\n");
def add(a,b):
    c=a+b;
    print("The sum of ",a,"and ",b,"is ",c);
def subtract(a,b):
    c=a-b;
    print("The difference of ",a,"and ",b,"is ",c);
def multiply(a,b):
    c=a*b;
    print("The product of ",a,"and ",b,"is ",c);
def divison(a,b):
    c=b/a;
    print("The divison of ",a,"and ",b,"is ",c);

restart=input("Enter y or Y to start the calculator");
menu()
while restart in('y','Y'):
    choice=input("Enter menu choice");
    a=float(input("Enter the first number"));
    b=float(input("Enter the second number"));
    if choice=="+":
        add(a,b)
    elif choice=="-":
        subtract(a,b)
    elif choice=="*":
        multiply(a,b)
    elif choice=="/":
        divide(a,b)
    else:
        print("Enter the right menu choice");
    restart=input("Enter y or Y to restart the calculator");
           
       

