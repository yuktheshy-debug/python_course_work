#another child class for the redbus driver
#take details using cons
#user needs to see booked 
#protect the driver details from user


class Redbus:
    bus = {i: "Available" for i in range(1,11)}

    def displayseats(self):
        print("------------xyz------------")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])

    def booking(self,seatno):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i] == 'Available':
                Redbus.bus[i] = 'Booked'
                print(f"Seat - {seatno} booked successfully")
                break
        else:
            print(f"The seat {seatno} you selected is already bookked")



class driver(Redbus):
    def __init__(self,name,age,phoneno):
        self.name = name
        self.age = age
        self.phoneno = phoneno

    def driver_details(self):
        print("Driver is assigned to the bus")


class Users(Redbus):
    def __init__(self,name,email,phoneno):
        self.name = name
        self.email = email
        self.phoneno = phoneno
        print(f"Hello {self.name}, Welcome to the Redbus")

lohitha = Users('lohitha','lohitha@12gmail.com','1234567890')
lohitha.displayseats()
lohitha.booking(7)
lohitha.displayseats()
lohitha.booking(7)







