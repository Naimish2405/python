Name=input("Enter your name :")
m1=int(input("Enter a marks 1:"))
m2=int(input("Enter a marks 2:"))
m3=int(input("Enter a marks3:"))
total=m1+m2+m3
if m1 >=28 and m2 >=28 and m3>=28:
    result="pass"
    per=total/2.1
    if per>=70:
        grade="A"
    elif per>=60:
        grade="B"
    elif per>=50:
        grade="C"
    elif per>=40:
        grade="D"
    else:
        grade="E"
else:
    result="Fail"
    per="***"
    grade="F"
print("Name:",Name)
print("total :",total)       
print("result :",result)        
print("percentage :",per)        
print(" grade :",grade)        