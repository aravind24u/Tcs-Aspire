a=raw_input('Enter the the First name : ')
b=raw_input('Enter the the Second name : ')
a=''.join(set(a))
b=''.join(set(b))
for i in range(0,len(a)-1):
    for j in range(0,len(b)-1):
        if a[i]==b[j]:
            print a[i]
        