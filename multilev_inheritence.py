d={}
class student:
 def __init__(self):
  self.name=input("Enter name")
  self.age=int(input("Enter age"))
  self.usn=input("Enter usn")

 def display(self):
  print("name:",self.name)
  print("age:",self.age)
  print("usn:",self.usn)

class deriv1(student):
 def __init__(self):
  student.__init__(self) 
  self.sub=[]
  self.total=0
  for i in range(1,6):
   n=int(input("Enter marks in subject"))
   self.sub.append(n)
   self.total+=n
  self.per=((self.total/250)*100)

 def display(self):
   student.display(self)
   for i in range(5):
    print("Marks in sub are:-",self.sub[i])
   print("percentage:",self.per)


class deriv2(deriv1):
 def __init__(self):
  deriv1.__init__(self)
  d.update({self.name:{"name":self.name,
                       "age:":self.age,
                       "usn:":self.usn,
                       "marks:":self.sub,
                       "total:":self.total,
                       "percentage:":self.per }})


def printtemp():
	print(d)
	for key in d:
		print(key,d[key])

while True:
 print("1.add\n2.display\n0.exit\n")

 ch=int(input("Enter choice"))
 if ch==1:
  e=deriv2()
  e.display()

 elif ch==2:
  printtemp()

 elif ch==0:
  print("**exit**")
  break

 else:
  print("**invalid input**")
  break



                         
 

