import numpy as np
l1=list(np.arange(1,51))
print(type(l1))
l2=[]
count=1 
width=3
def print_seat():
 for x in range(len(l1)):
  print("%*s" % (width,l1[x]),end="  ")
  if (x+1)%10==0:
    print()
  
while count==1:
  if count==1:
   print_seat()
   x=int(input("\nEnter the seat number you want to book="))
  if x<=len(l1)+1:
   if x not in l2:
      print("Seat no.",x,"is booked successfully!!\n")
      l2.append(x)
      l1[x-1]="BK"
      print_seat()
    
      print("\n\nPress 1 to continue booking and 0 to exit.")

      e=int(input("\nEnter your choice="))
      if e==1:
       count=1
      else:
       count=0
       print("\nThank you for visiting!!!")
       print("Your booked seats are seat no.= ",end="")
       for i in range(0,len(l2)):
         print(l2[i],end=" ")
   else:
     print("This seat is already booked choose another!!")
     

     print("\nPress 1 to continue booking and 0 to exit.")
     e=int(input("Enter your choice="))
     if e==1:
      count=1
     else:
      count=0
      print("\nThank you for visiting!!!")
  else:
    print("\nSeat nunmbers are only available from 1 to ",len(l1),"."," Try again!!",sep="")