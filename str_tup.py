while True:
 print("1.string operation")
 print("2.tuple operation")
 print("3.exit")

 ch=int(input("Enter choice"))

 if ch==1:
  print("====welcome in string operation====\n")
  a=input("Enter string")
  while True:
   print("1.length\n2.uppercase\n3.lowercase\n4.reverse\n5.find\n6.count\n7.swapcase\n8.concatenation\n9.split\n10.title\n0.exit\n")
   c=int(input("Enter choice"))

   if c==1:
    print(len(a))
   elif c==2:
    print(a.upper())
   elif c==3:
    print(a.lower())
   elif c==4:
    print(a[::-1])
   elif c==5:
    e=input("Enter the element that u want to find")
    print(a.find(e))
   elif c==6:
    e=input("Enter the element that u want to count")
    print(a.count(e))
   elif c==7:
    print(a.swapcase())
   elif c==8:
    e=input("Enter another string")
    print(a+e)
   elif c==9:
    e=input("Enter the element from where u want to split")
    print(a.split(e))
   elif c==10:
    print(a.title())
   elif c==0:
    print("**exit**")
    break
   else:
    print("***invalid input***")
    break

 elif ch==2:
  print("====welcome in tuple operation====")
  a=tuple(input("Enter tuple").split())
  while True:
   print("1.length\n2.nested tuple\n3.type\n4.reverse\n5.find by index no.\n6.conversion\n7.slice\n8.concatenation\n9.maximum\n10.minimum\n0.exit\n")
   c=int(input("Enter choice"))

   if c==1:
    print(len(a))
   elif c==2:
    e=tuple(input("Enter another tuple").split())
    print((a,)+(e))
   elif c==3:
    print(type(a))
   elif c==4:
    print(a[::-1])
   elif c==5:
    e=int(input("Enter the index no."))
    print(a[e])
   elif c==6:
    l=list(a)
    print(l)
   elif c==7:
    e=int(input("Enter index no. from where u want to slice"))
    f=int(input("Enter index no. till where u want to slice"))
    print(a[e:f])
   elif c==8:
    e=tuple(input("Enter another tuple").split())
    print(a+e)
   elif c==9:
    print(max(a))
   elif c==10:
    print(min(a))
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


