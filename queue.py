l=[]
ch="yes"
while True:
    if(ch!="yes"):
        break
    else:
        print("enter 1 for adding to the queue\n enter 2 for deleting from the queue\n enter 3 to view all elements")
        a=int(input("enter choice"))
        if(a==1):
            x=int(input("enter number to be inserted"))
            l.append(x)
            print("element added")
        elif(a==2):
            if(len(l))>0:
                x=l.pop(0)
                print("element",x,"deleted")
            else:
                print("list empty")
        elif(a==3):
            if(len(l))>0:
                for i in l:
                   print(i,end=' ')
            else:
                print("list empty")
        else:
            print("invalid choice")
    print("continue? enter yes to proceed")
    ch=input("enter here")
    
        
            
