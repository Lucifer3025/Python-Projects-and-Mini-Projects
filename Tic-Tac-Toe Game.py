def grid():
    print("-------------------")
    print("| ",zero," | ",one," | ",two," |")
    print("-------------------")
    print("| ",three," | ",four," | ",five," |")
    print("-------------------")
    print("| ",six," | ",seven," | ",eight," |")
    print("-------------------")
zero=0;one=1;two=2;three=3;four=4;five=5;six=6;seven=7;eight=8
    
def replay():
    print("\nIf you want to replay the game choose '1' otherwise choose '0'.")
    p2=1
    while p2==1:
     try:
      choice=int(input("Enter your choice="))
      if choice!=0 and choice!=1:
         raise ValueError
     except:
        print("\nPlease enter only '1' and '0' as input!!")
     else:
         p2=0
            
    if choice==1:
        return False
    else:
        print("\nThank you for playing!!!")
        return True

def draw():
    if d1==5 and d2==4:
        return False
    
def win():
    if one==zero==two=="X" or zero==three==six=="X" or one==four==seven=="X" or\
     two==five==eight=="X" or three==four==five=="X" or six==seven==eight=="X" or\
     zero==four==eight=="X" or two==four==six=="X":
        print("\nCONGRATULATIONS!!!",A,"is the winner!!!")
        return False 
    elif one==zero==two=="O" or zero==three==six=="O" or one==four==seven=="O" or\
    two==five==eight=="O" or three==four==five=="O" or six==seven==eight=="O" or\
    zero==four==eight=="O" or two==four==six=="O":
        print("\nCONGRATULATIONS!!!",B,"is the winner!!!")
        return False
    
count=1
check=1
check2=1
t=1
p=1
p2=1
l1=[]
l2=[]
d1=0
d2=0
print("initial grid:")
grid()
while p==1:
 try:
  A=str(input("Enter the name of the player A="))
  B=str(input("Enter the name of the player B="))
 except KeyboardInterrupt:
    print("\nKey board interrupt occured.")
 else:
    p=0

print(A,"will use 'X' and",B,"will use 'O' to play!!")
while count==1:
   if t==1:
      print("\n",A,"'s turn...",sep="")
      while check==1:
              try:
                c1=int(input("Enter the number on which you want to print 'X'="))
                if c1<0 or c1>9:
                 raise ValueError
              except ValueError:
               print("Please only enter numbers and only numbers from 0 to 9 are allowed!!")
              else:
               check=0
      if t==1:
           if c1 not in l1 and c1 not in l2:  
              if c1==0:
                 zero="X"
              elif c1==1:
                 one="X"
              elif c1==2:
                 two="X"
              elif c1==3:
                 three="X"
              elif c1==4:
                 four="X"
              elif c1==5:
                 five="X"
              elif c1==6:
                 six="X"
              elif c1==7:
                 seven="X" 
              elif c1==8:
                 eight="X"
              l1.append(c1)
              check=1
              d1+=1
              t=0
              grid()
              x=win()
              y=draw()
          
              if x==False:
                 r=replay()
                 if r==False:
                     l1.clear(),l2.clear()
                     zero=0;one=1;two=2;three=3;four=4;five=5;six=6;seven=7;eight=8
                     d1=0;d2=0
                     grid()
                 else:
                   count=0
                  
              elif y==False:
               print("\nNobody won it's a draw!!!")
               r=replay()
               if r==False:
                 l1.clear(),l2.clear()
                 zero=0;one=1;two=2;three=3;four=4;five=5;six=6;seven=7;eight=8
                 d1=0;d2=0
                 grid()
               else:
                  count=0
           else:
            print("\nThis slot is already occupied, please enter another number.")
            check=1
        
     
          
   elif t==0:
         print("\n",B,"'s turn...",sep="")
         while check2==1:
             try:
               c2=int(input("Enter the number on which you want to print 'O'="))
               if c2<0 or c2>9:
                raise ValueError
             except ValueError:
              print("Please only enter numbers and only numbers from 0 to 9 are allowed!!")
             else:
              break
              
         if t==0:
             if c2 not in l1 and c2 not in l2:  
                 if c2==0:
                     zero="O"
                 elif c2==1:
                     one="O"
                 elif c2==2:
                     two="O"
                 elif c2==3:
                     three="O"
                 elif c2==4:
                     four="O"
                 elif c2==5:
                     five="O"
                 elif c2==6:
                     six="O"
                 elif c2==7:
                      seven="O" 
                 elif c2==8:
                      eight="O" 
                 l2.append(c2)
                 check2=1
                 d2+=1
                 t=1
                 grid()
                 x=win()
                 y=draw()
                 if x==False:
                     r=replay()
                     if r==False:
                         l1.clear(),l2.clear()
                         zero=0;one=1;two=2;three=3;four=4;five=5;six=6;seven=7;eight=8
                         d1=0;d2=0
                         grid()
                     else:
                      count=0
                 elif y==False:
                     print("\nNobody won it's a draw!!!")
                     r=replay()
                     l1.clear(),l2.clear()
                     zero=0;one=1;two=2;three=3;four=4;five=5;six=6;seven=7;eight=8
                     d1=0;d2=0
                     grid()
             else:
                print("\nThis slot is already occupied, please enter another number!!")
                check2=1
        
    