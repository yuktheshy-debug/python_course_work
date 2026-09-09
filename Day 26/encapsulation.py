#binding data into single unit is called encapsulation

'''
pub -> inclass,child,outside
pri -> inclass
pro -> inclass,child,outside(not recommended)
'''

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword
    
    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

yukthesh = Instagram('yukthesh','1234')

print(yukthesh.username)
print(yukthesh.getpassword())
print(yukthesh.accesspost)

yukthesh.username = 'yukthesh_123'
print(yukthesh.username)

yukthesh.setpassword('yukthesh@123')
print(yukthesh.getpassword())

yukthesh.accesspost = 'python'
yukthesh.accesspost = 'java'
yukthesh.accesspost = 'mysql'

print(yukthesh.accesspost)