from re import I
from tokenize import Number


print ("hello")
print("i am groot")
Number = int(input("enter the number of multiplication: "))
count = 1
print("the multilpication of", Number)
while count <=10:
  Number = Number * 1
 
  print(Number, 'x',count,'=', Number*count)
  count += 1