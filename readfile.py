a=open('C:/Users/Ajay_2/Desktop/Workspace/Python/asd.txt','r')
b=a.readlines()
j=0
c=['','','','','','','','','']
print b
d=input('Enter your chioce\n1.All Subject Names\n2.subject details\nYour Chioce :')
if d==1:
    j=0
    for i in b:
        for k in i:
            if k!=' ':
                c[j]=c[j]+k
            if k==' ':
                break
        print c[j]
        j+=1
if d==2:
    print('Enter the subject ')
    j=0
    for i in b:
        for k in i:
            if k!=' ':
                c[j]=c[j]+k
            if k==' ':
                break
    
        j+=1
    j=0
    for i in c:
        while c[j]!='':
            print str(j)+'. for '+c[j]
            j+=1    
    choice=input('Enter your choice :')
    print b[choice]