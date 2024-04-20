s=input("enter a string")
a=""
n=len(s)
for i in range(n):
    if(i==0):
        a=a+s[i].upper()
    elif(i==(n-1)):
        a=a+s[i].upper()
    elif(s[i+1]==" "):
        a=a+s[i].upper()
    elif(s[i-1]==" "):
        a=a+s[i].upper()
    else:
        a=a+s[i]
print(a)
    
