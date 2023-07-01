while True:
 print("1.Value Error")
 print("2.File Not Found Error")
 print("3.Type Error")
 print("4.IO Error")
 print("5.Name Error")
 print("0.Exit")
 ch=int(input("Enter your choice"))

 if ch==1:
  try: 
   f=open("f1.txt","g")
   print("successful")

  except ValueError:
   print("\nValue Error\n")

 elif ch==2:
   try:
    f=open("f2.txt","r")
    print("successful")

   except FileNotFoundError:
    print("\nFile Not Found Error\n")

 elif ch==3:
   try:
    f=open("f1.txt","r","w")
    print("successful")
  
   except TypeError:
    print("\nType Error\n")

 elif ch==4:
   try:
    f=open("f1.txt","r")
    f.write("hello")
    print("successful")

   except IOError:
    print("\n IO Error\n")

 
 elif ch==5:
   try:
    f=opens("f1.txt","r")
    print("successuful")

   except NameError:
    print("\nName Error\n")  

 elif ch==0:
  print("**exit**")
  break

 else:
  print("**invalid input**")
  break
