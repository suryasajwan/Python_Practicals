class Employee:
    apply_raise = 1.5

    def __init__(self):
        self.first = input("Enter the First name")
        self.empid = input("Enter the Emp ID")
        self.pay = int(input("Enter the Salary"))

    def display(self):
        print("first name:", self.first)
        print("last name:", self.last)
        print("empid=", self.empid)
        print("pay=", self.pay)

    def pay_raise(self):
        self.pay = int(self.pay) * self.apply_raise


class Developer(Employee):
    apply_raise = 2.5

    def __init__(self):
        self.first = input("Enter the First name")
        self.last=input("Enter last")
        self.empid = input("Enter the Emp ID")
        self.pay = int(input("Enter the Salary"))



    def pay_raise(self):
        self.pay = int(self.pay) * self.apply_raise


class Manager(Employee):
    apply_raise = 3.5

    def pay_raise(self):
        self.pay = int(self.pay) * self.apply_raise


e1 = Developer()
e2 = Manager()
e1.pay_raise()
e2.pay_raise()
e1.display()
e2.display()
