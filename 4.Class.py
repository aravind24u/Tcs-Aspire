class student :
    name=0
    no=0
    a=range(0,6)  
    def __init__(self):
        self.name=raw_input('Enter the name : ')
        self.no=input('Enter the Roll no : ')
        for i in  range(1,6):
            self.a[i]=float(input('Enter your mark in subject - '+`i`+' : '))        

    def calc(self):
        self.total=0
        self.avg=0
        for i in range(1,6):
            self.total+=self.a[i]
        self.avg= self.total/5
    def display(self):
        print '\n\nYour Name : '+self.name
        print 'Your Roll No : ',self.no
        print 'Total marks obatined : ',self.total
        print 'Average marks scored : ',self.avg 
b=student()
b.calc()
b.display()