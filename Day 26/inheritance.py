#aqurirng data from parent class to child class
#main goal is REUSE the code


#EXAMPLE fpr single inheritance
'''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24 hrs")

lohitha = whatsappv1()
lohitha.message()

yukthesh = whatsappv2()
yukthesh.status()
yukthesh.message()
'''
'''
#example for multilevel inheritance

class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24 hrs")

class whatsappv3(whatsappv2):
    def groups(self):
        print("You can create a group and talk with multiple people at the same time")

class whatsappv4():
    def community(self):
        print("You can create a community")

class whatsappv5(whatsappv4,whatsappv3,whatsappv2):
    def channels(self):
        print("You can post reggurarly")


lohitha = whatsappv1()
lohitha.message()

yukthesh = whatsappv2()
yukthesh.status()
yukthesh.message()

ssr = whatsappv3()
ssr.groups()
ssr.status()
ssr.message()

k = whatsappv4()
k.community()

yuk = whatsappv5()
yuk.channels()
yuk.community()
yuk.groups()
yuk.status()
yuk.message()
'''

#hierarichal : one parent and many childs

class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24 hrs")

class whatsappv3(whatsappv1):
    def groups(self):
        print("You can create a group and talk with multiple people at the same time")

class whatsappv4(whatsappv1):
    def community(self):
        print("You can create a community")

lohitha = whatsappv1()
lohitha.message()

yukthesh = whatsappv2()
yukthesh.status()
yukthesh.message()

ssr = whatsappv3()
ssr.groups()
ssr.message()

k = whatsappv4()
k.community()
k.message()