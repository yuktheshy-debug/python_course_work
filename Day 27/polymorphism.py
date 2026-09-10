#same method diff actions

#method overloading - same name different parameters
#method overriding - Redefining a parent class method in the child class with the same name and parameters.
#operator overloading

#example for overriding

class Hotstar:
    def __init__(self,name):
        print(f'Welcome to the hotstar, {name}---------')
    def auth(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard")
    def searchbar(self):
        print("You can see the search bar")
    def history(self):
        print("You can see the history")
    def playcontrolls(self):
        print("You can see the play controlls")
    def ads(self):
        print("ads will be run")
    def quality(self):
        print("You have limited quality")
    def devices(self):
        print("Single device login")
    def access(self):
        print("Limited access")
    def download(self):
        print("You can't download")

class Premiumhotstar(Hotstar):
    def __init__(self,name):
        print(f'Welcome to the premium hotstar, {name}')
    def ads(self):
        print("ads will not run")
    def quality(self):
        print("You have high quality")
    def devices(self):
        print("Multiple devices login")
    def access(self):
        print("unlimited access")
    def download(self):
        print("You can download")

yukthesh = Hotstar('yukthesh')
yukthesh.auth()
yukthesh.dashboard()
yukthesh.searchbar()
yukthesh.history()
yukthesh.playcontrolls()
yukthesh.ads()
yukthesh.quality()
yukthesh.devices()
yukthesh.access()
yukthesh.download()


ssr = Premiumhotstar('ssr')
ssr.auth()
ssr.dashboard()
ssr.searchbar()
ssr.history()
ssr.playcontrolls()
ssr.ads()
ssr.quality()
ssr.devices()
ssr.access()
ssr.download()

