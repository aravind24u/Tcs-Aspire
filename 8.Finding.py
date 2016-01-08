c=input('Enter the number of elements in the list : ')
a=range(0,c)
f=0
for i in a:
    a[i]=input('Enter the value of the element number '+str(i+1)+' :')
b=input('Enter the number to be searched for : ')
for i in a:
    if i==b:
        f=1
        break
if f:
    print 'Seach element found !'
else :
    print 'Search element is not present.'