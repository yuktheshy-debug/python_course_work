class Flipkart:
    discount = 30
    @classmethod#decorator
    def updateddiscount(cls):#class method
        cls.discount = 40
        print("Updated discount",cls.discount)

    def info(self,name,phoneno,address):#instant method
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print("Welcome to flipkart",self.name)
        print("Your phoneno is: ",self.phoneno)
        print("City is ",self.address)

    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% discount is going on,grab the products")


lohitha = Flipkart()
lohitha.info("Lohitha",9983664830,"Hyd")
lohitha.updateddiscount()
lohitha.banner()
usharani = Flipkart()
usharani.info("usharani",9983664830,"bnr")
usharani.updateddiscount()
usharani.banner()
mounasri = Flipkart()
mounasri.info("mounasri",9983664830,"ch")
mounasri.updateddiscount()
mounasri.banner()