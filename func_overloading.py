class Student:
 def show(self,name=None,age=None,college=None):
  if(name==None and age==None and college==None):
   print("No data given")
  
  elif (age==None and college==None):
   self.name=name
   print("Studen name is ",self.name)
  
  elif (college==None):
   self.name=name
   self.age=age
   print("Student name is ",self.name,"and age is",self.age)

  else:
   self.name=name
   self.age=age
   self.college=college
   print("Student name :",self.name,"age:",self.age,"college:",self.college)

s=Student()

while True:
 print("1.One argument\n2.Two argument\n3.Three argument\n4.No argument\n0.Exit\n")
 ch=int(input("Enter your choice"))

 if ch==1:
  s.show("john")

 elif ch==2:
  s.show("john",22)

 elif ch==3:
  s.show("john",22,"RVCE")
 
 elif ch==4:
  s.show()

 elif ch==0:
  print("****Exit****")
  break

 else:
  print("****Invalid Input*****")
  break

