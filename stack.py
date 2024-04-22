l=[]
ch="yes"
while True:
    if(ch!="yes"):
        break
    else:
        print("enter 1 for adding to the stack\n enter 2 for deleting from the stack\n enter 3 to view all elements")
        a=int(input("enter choice"))
        if(a==1):
            x=int(input("enter number to be inserted"))
            l.append(x)
            print("element added")
        elif(a==2):
            if(len(l))>0:
                n=len(l)
                x=l.pop(n-1)
                print("element",x,"deleted")
            else:
                print("list empty")
        elif(a==3):
            if(len(l))>0:
                for i in range(-1,-n-1,-1):
                   print(l[i],end=' ')
            else:
                print("list empty")
        else:
            print("invalid choice")
    print("continue? enter yes to proceed")
    ch=input("enter here")
    
        
            
