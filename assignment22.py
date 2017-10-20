import math
class Complex(object):
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def display(self):
        if self.imaginary>0:
            print ("%.2f + %.2fi"%(self.real,self.imaginary))
        elif self.imaginary<0:
            print ("%.2f %.2fi"%(self.real,self.imaginary))
        elif self.real==0:
            print("%.2fi"%(self.imaginary))
        else :
            print(self.real)     
    def addition(self,other):
        r=float(self.real+other.real)
        i=float(self.imaginary+other.imaginary)
        result=Complex(r,i)
        result.display()
    def subtract(self,other):
        r=float(self.real-other.real)
        i=float(self.imaginary-other.imaginary)
        result=Complex(r,i)
        result.display()
    def multiply(self,other):
        r1 = self.real
        i1 = self.imaginary
        r2 = other.real
        i2 = other.imaginary
        resultR =float((r1*r2-i1*i2))
        resultI =float((r1*i2+r2*i1))
        result=Complex(resultR, resultI)
        result.display()
    def division(self,other):
        r1 = self.real
        i1 = self.imaginary
        r2 = other.real
        i2 = other.imaginary
        resultR = float(float(r1*r2+i1*i2)/float(r2*r2+i2*i2))
        resultI = float(float(r2*i1-r1*i2)/float(r2*r2+i2*i2))
        result=Complex(resultR, resultI)
        result.display()
    def mod(self):
        r=pow(self.real,2)
        i=pow(self.imaginary,2)
        print ("%.2f"%(math.sqrt(r+i)))

        
       
print("Enter the first complex number")
rpart1=float(input("Enter the real part"))
ipart1=float(input("Enter the imaginary part"))
print("Enter the second complex number")
rpart2=float(input("Enter the real part"))
ipart2=float(input("Enter the imaginary part"))
a=Complex(rpart1,ipart1)
b=Complex(rpart2,ipart2)
a.addition(b)
a.subtract(b)
a.multiply(b)
a.division(b)
a.mod()
b.mod()

