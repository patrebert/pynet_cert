#!/bin/env python
def func3():
    print "world.py func3"

class MyClass:

    def __init__(self,arg1, arg2, arg3):
        print "MyClass __init__"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def hello(self):
        print "hello"
        print "  %s %s %s" %(self.arg1, self.arg2, self.arg3)

    def not_hello(self):
        print "not_hello"
        print "  %s %s %s" %(self.arg1, self.arg2, self.arg3)

class MyChildClass(MyClass):

    def __init__(self,var1,var2,var3):
        print "MyChildClass __init__"
        MyClass.__init__(self, var1, var2, var3)

    def  hello(self):
        print "This is the overridden 'hello' method of MyChildClass speaking"
        print "  %s %s %s" %(self.arg3, self.arg2, self.arg1)

def testclass():
    hell = MyClass('1', '2', '3')
    hell.hello()
    hell.not_hello()
 
def main():
    func3()
    hell = MyClass('1','2','3')
    hell.hello()
    hell.not_hello()
    print "CREATE MyChildClass object"
    hell2 = MyChildClass('1','2','3')
    hell2.hello()

if __name__ == '__main__':
    main()
