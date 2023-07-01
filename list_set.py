while True:
 print("1.list operation")
 print("2.set operation")
 print("3.exit")

 ch=int(input("Enter choice"))

 if ch==1:
  print("====welcome in list operation====\n")
  a=list(input("Enter list").split())
  while True:
   print("1.length\n2.concat\n3.reverse\n4.sort\n5.remove\n6.append\n7.repeat\n8.sort\n9.slice\n10.clear\n0.exit\n")
   c=int(input("Enter choice"))

   if c==1:
    print(len(a))
   elif c==2:
    e=list(input("Enter another list").split())
    print(a+e)
   elif c==3:
    a.reverse()
    print(a)
   elif c==4:
    a.sort()
    print(a)
   elif c==5:
    e=input("Enter the element that u want to remove")
    a.remove(e)
    print(a)
   elif c==6:
    e=input("Enter the element that u want to append")
    a.append(e)
    print(a)
   elif c==7:
    e=int(input("Enter the times of repeatition"))
    print(e*a)
   elif c==8:
    a.sort()
    print(a)
   elif c==9:
    e=int(input("Enter start index."))
    f=int(input("enter last index."))
    print(a[e:f])
   elif c==10:
    a.clear()
    print(a)
   elif c==0:
    print("**exit**")
    break
   else:
    print("***invalid input***")
    break

 elif ch==2:
  print("====welcome in set operation====")
  a=set(input("Enter set").split())
  while True:
   print("1.length\n2.union\n3.intersection\n4.difference\n5.symmetric difference\n6.add\n7.pop\n8.contain\n9.clear\n10.delete\n0.exit\n")
   c=int(input("Enter choice"))

   if c==1:
    print(len(a))
   elif c==2:
    e=set(input("Enter another set").split())
    print(a.union(e))
   elif c==3:
    e=set(input("Enter another set").split())
    print(a.intersection(e))
   elif c==4:
    e=set(input("Enter another set").split())
    print(a.difference(e))
   elif c==5:
    e=set(input("Enter another set").split())
    print(a^e)
   elif c==6:
    e=int(input("Enter element"))
    print(a.add(e))
   elif c==7:
    
    
    print(a.pop())
   elif c==8:
    e=int(input("Enter element to check"))
    print(e in a)
   elif c==9:
    print("after clear",a.clear())
   elif c==10:
    del a
    print("deleted")
   elif c==0:
    print("**exit**")
    break
   else:
    print("***invalid input***")
    break

 elif ch==3:
  print("****exit from all operation*****")
  break

 else:
  print("****invalid input*******")
  break
