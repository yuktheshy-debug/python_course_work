'''username = input(" Enter the Username : ")
password = input("Enter the Password : ")

if username == "admin" and password == "admin123":
    print("Login successful")
else :
    print("Invalid credentials")

products = ["apple", "book", "pen"]
search = input("Enter the product : ")

if search in products:
    print(f"{search} found")
else:
    print(f"{search} not found")'''

#delivery charges
bill = int(input("Enter the bill : "))
if bill > 99:
    print("final bill", bill)
else :
    print(f"final bill + Extra charges : {bill + 30}")