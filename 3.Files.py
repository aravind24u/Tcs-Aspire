''' function.py'''
def f(a):
    p(a)
    pr(a)
    even(a)
def p(a):
     b=reversed(str(a))
     if list(b)==list(str(a)):
         print 'Palindrome'
     else:
        print 'Not a plaindrome'
def pr(a):
    b=a/2
    i=2
    f=0
    while(i<b):
        if a%i==0:
            f=1
            break
        i+=1
    if f:
        print 'Not prime'
    else :
        print 'Prime'
def even(a):
    if a%2==0:
        print'Even'
    else:
        print 'Odd'
'''Main file
import function
a=input('Enter the number : ')
function.f(a)
'''        