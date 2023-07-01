from magic1 import*

ob1=ope()
ob2=ope()

ob1.accept()
ob2.accept()

while True:
 print("1.Addition")
 print("2.Subtraction")
 print("3.Multiplication")
 print("4.FloorDivision")
 print("5.greater than")
 print("0.Exit")

 ch=int(input("Enter your choice"))

 if ch==1:
  ob1+ob2

 elif ch==2:
  ob1-ob2
 
 elif ch==3:
  ob1*ob2

 elif ch==4:
  ob1//ob2

 elif ch==5:
  ob1>ob2 

 elif ch==0:
  break

 else:
  break
