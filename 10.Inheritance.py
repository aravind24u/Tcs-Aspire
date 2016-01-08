class base(object):
    def __init__(self):
        self.__age=0
    def a(self,b):
        self.age=b
        print self.age
class child(base):
    def __init__(self,c):
        super(child,self).__init__()
        super(child,self).a(c)
e=input('Enter the Age')
d=child(e)