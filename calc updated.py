print(" ____________________________________________________________________________________________________ \n Let's say , \n 1 means add \n 2 means subtract \n 3 means multiply \n 4 means divide \n 5 means exponent")
def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply (x,y):
    return x*y
def divide (x,y):
    return  x / y
def exponent (x,y):
    return x**y
l={1:add,2:subtract,3:multiply,4:divide,5:exponent}
while(1):
      print(" \nEnter your first number please")
      x= float(input())
      print("enter your second number")
      y = float(input())
      print("enter your operator")
      c= int(input())
      d= l[c](x,y)
      print("your answer is ", d)



