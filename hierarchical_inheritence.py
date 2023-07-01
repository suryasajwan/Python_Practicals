class student:
 def __init__(self):
  self.name=input("Enter name")
  self.usn=input("Enter usn")
  self.age=input("Enter age")
 
 def display(self):
  print("name:",self.name)
  print("usn:",self.usn)
  print("age:",self.age)

class ugstudent(student):
 def __init__(self):
  student.__init__(self)

  self.stipened=int(input("Enter stipended"))
  self.fees=int(input("Enter fees"))
  self.sem=int(input("Enter semester"))

 def display(self):
  student.display(self)
  
  print("semester:",self.sem)
  print("fees:",self.fees)
  print("stipened:",self.stipened)


class pgstudent(student):
 def __init__(self):
  student.__init__(self)

  self.stipened=int(input("Enter stipended"))
  self.fees=int(input("Enter fees"))
  self.sem=int(input("Enter semester"))

 def display(self):
  student.display(self)
  
  print("semester:",self.sem)
  print("fees:",self.fees)
  print("stipened:",self.stipened)

  
while True:
 print("1.ug\n2.pg\n0.exit\n")
 ch=int(input("Enter choice"))
 
 if ch==1:
   ug=ugstudent()
   ug.display()

 elif ch==2:
  pg=pgstudent()
  pg.display()

 elif ch==0:
  print("**exit**")
  break

 else:
  print("**invalid input**")
  break
