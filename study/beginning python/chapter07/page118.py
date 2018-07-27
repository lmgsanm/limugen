#!/usr/bin/env python3
__Author__ = "limugen"

class person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print("Hello,this is %s greet to you",self.name)

a = person()
b = person()

a.setName("lee")
b.setName("limugen")

print(a.greet())
print(b.greet())

