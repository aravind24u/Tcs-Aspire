def p(a):
    print a
a=['English,','Telegu,','hindu,','Ev.Science,','Computers.']
b=['Science,','Social Studies,','Mathematics,','Gk,','Project work.']
c= input('1.For list of subjects in first semester\n2.For list of subjects in second semester\nYour choice :')
if c==1:
    p(a)
elif c==2:
    p(b)
else:
    print 'Invalid Input' 