x=input("enter the x value:")
y=input("enter the y value:")
while 1:
    c=input('1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5.Quit\n\nYour Choice :')
    if c==1:
        print x+y
    elif c==2:
        print x-y
    elif c==3:
        print x*y
    elif c==4:
        print x/y
    elif c==5:
        break
    else :
        print'Invalid Input'