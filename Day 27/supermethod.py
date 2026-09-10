#SUPER METHOD
'''
class whatsappv1():
    def status(self):
        print("You can upload the status")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()  #to get the both child class and parent class attributes we use super method
        print("You add music and you can react")

a = whatsappv1()
a.status()

b = whatsappv2()
b.status()
'''
#CLASS METHOD

#whenever we have multiple inheritance we need to use this class method

class whatsappv1():
    def status(self):
        print("You can upload the status")

class whatsappv2():
    def status(self):  
        print("You add music and you can react")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)    #to get the both child class and parent class attributes we used here CLASS method(when we have 3 means one parent and two childs)
        whatsappv2.status(self)
        print("You can add to the platform")

a = whatsappv3()
a.status()

