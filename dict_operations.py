d={}

class Employee:
 def input(self):
  self.name=input("Enter name")
  self.add=input("Enter address")
  self.pan=input("Enter pan")
  self.basic=int(input("Enter basic salary"))
  self.deduct=int(input("Enter deductions"))
  self.hra=1.25*self.basic
  self.da=0.25*self.basic
  self.gross=self.basic+self.hra+self.da
  self.net=self.gross-self.deduct
  
  self.update()


 def update(self):
  d.update({self.name:{"name":self.name,
                      "address":self.add,
                      "pan":self.pan,
                      "basic_sal":self.basic,
                      "deductins":self.deduct,
                      "hra":self.hra,
                      "da":self.da,
                      "gross":self.gross,
                      "net":self.net 
                    }})

 def search(self,name):
  
  flag=0
  for key in d:
   if key==name:
    print("employee found")
    for i in d[key]:
     print(i,d[key][i])
     flag=1

  if flag==0:
   print("employee not found")


 def printtemp(self):
  for key in d:
   print(key,d[key])


class employee1(Employee):
 em=Employee()
 while True:
  print("1.add employee\n2.print employee\n3.search employee\n0.exit\n")
  ch=int(input("Enter choice"))

  if ch==1:
   em.input()

  elif ch==2:
   em.printtemp()

  elif ch==3:
   n=input("Enter name of employee that u want to search")
   em.search(n)
  
  elif ch==0:
   print("**exit**")
   break

  else:
   print("**invalid input**")
   break
