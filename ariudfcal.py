def calculator (*args):
    if c=='1':
        return(a+b)
    elif c=='2':
      return(a-b)
    elif c=='3':
         return(a*b)
    elif c=='4':
         return(a/b)
    else:
        return(print("enter corrent no:"))
a=int(input("enter first no:"))
b=int(input("enter second no:"))
c=input("enter 1 for add,2 for sub,3 for multi,4 for div:")
print(calculator(a,b,c))
        
    