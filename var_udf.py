def calculator(operation,*args):
    if operation==1: 
        add=0
        for i in args:
            add+= i
            #return add
            return add
    elif operation==2:
        if len(args)==0:
            return 0
        sub=args[0]
        for i in args[1]:
            sub==i
            return sub
    elif operation==3:
        mul=1
        for i in args:
            mul*=i
            return mul
    elif operation==4:
        if len(args)==0:
            return "No no. to divide"
        div=args[0]
        try:
             for i in args[1]:
              div/=i
            #else zeroDivisionerror:
        except ZeroDivisionError:
         return "Division by zero dot allowed"
         return div  
    else:
        print("enter corrent no.")
number=[]
n=int(input("enter no.of value:"))
for i in range(n):
    num=int (input("enter a no.:"))
    number.append(num)
print("Number entered:",number)
operation=int(input("Enter 1 for+2 for-,3 for *,4 for /"))                
result1=calculator(operation,*number)
print(result1)