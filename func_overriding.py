class employee:
 apply_raise=2
 def __init__(self):
  self.first=input("Enter first name")
  self.last=input("Enter last name")
  self.empid=input("Enter empid")
  self.pay=int(input("enter salary"))

 def display(self):
  print("first:",self.first)
  print("last:",self.last)
  print("empid:",self.empid)
  print("pay:",self.pay)

 def pay_raise(self):
  self.pay=self.pay*self.apply_raise


class Developer(employee):
 apply_raise=3

 def pay_raise(self):
  self.pay=self.pay*self.apply_raise


class Manager(employee):
 apply_raise=4

 def pay_raise(self):
  self.pay=self.pay*self.apply_raise


e1=Developer()
e2=Manager()

e1.pay_raise()
e2.pay_raise()

e1.display()
e2.display()

