''' EXAMPLES OF ARITHMETIC OPERATOR
for checking remainder in dividing of two numbers use - %
for exponential use - **
for  flooring in division use - //
EXAMPLE OF ASSIGNMENT OPERATOR
X += 5   ( adds 5 to the value of x )
x /= 5   ( divides 5 to the value of x)
EXAMPLES OF COMPARISON OPERATOR
 i == 5 (checks whetehr i = 5 or not )
i!= 5 ( checks whether i is not equal to 5 or it is )
i >= 5 (checks whether i is greater than 5 or not )
EXAMPLES OF LOGICAL OPERATOR
BASICS  [TRUE AND TRUE - TRUE , TRUE AND FALSE - FALSE , TRUE OR FALSE - TRUE, TRUE OR TRUE - TRUE]
is , is not ( identity operator )
EXAMPLES OF MEMBERSHIP OPERATOR
L=[12, 21 ,52 , 69 ,37,32]
PRINT ( 324 in L) , OUTPUT - TRUE
EXAMPLES OF BITWISE OPERATOR
'''
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



