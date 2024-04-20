s=input("enter a string")
a=""
n=len(s)
for i in range(n):
    if(i==0):
        a=a+chr((ord(s[i])-32))
    elif(i==(n-1)):
        a=a+chr((ord(s[i])-32))
    elif(s[i+1]==" "):
        a=a+chr((ord(s[i])-32))
    elif(s[i-1]==" "):
        a=a+chr((ord(s[i])-32))
    else:
        a=a+s[i]
print(a)
    
