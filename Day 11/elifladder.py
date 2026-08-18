#when ever you have more than one condition you need to use this

'''budget = int(input("Enter the budget : "))
if budget >10000 :
    print("Trip")
elif budget >5000 :
    print("Resort stay")
elif budget >3000 :
    print("Movie and Dinner")
elif budget > 1000 :
    print("Cafe and Shopping")
elif budget > 500 :
    print("Street food and park visit")
else : 
    print("Stay home")

hr = int(input("Enter the time : "))

if 5<= hr <=11 :
    print("Good morning")
elif 12 <= hr <= 16 :
    print("Good Afternoon")
elif 17 <= hr <= 20 :
    print("Good Evening")
elif 21 <= hr <= 24 :
    print("Good Night")
else :
    print("MIdnigght Sleep Well")

cust_budget = int(input("Enter the budget : "))

if cust_budget > 10000 :
    print("Cloud hosting")
elif cust_budget > 5000 :
    print("Business hosting")
elif cust_budget > 2000 :
    print("Premium hosting")
else :
    print ("Single hosting")

#instagram close frnds

fa = eval(input("Follows account : "))

if fa :
    cf = eval(input("Close friend : "))
    if cf :
        print("Story visible")
    else :
        print("Not in close friends list")
else :
    print("Follow the account first")

#online gaming tournament
reg = eval(input("Registered : "))

if reg :
    fee = eval(input("Fee paid : "))
    if fee :
        print("Tournament entry confirmed")
    else : 
        print("Entry fee pending")
else : 
    print("Registration required")

#link status

ls = eval(input("Link active : "))

if ls :
    ag = eval(input("Permission granted : "))
    if ag :
        print("Access granted")
    else : 
        print("Access denied")
else :
    print ("Appropriate message")'''

data = {
    'lohitha':{'status':True,'python':90,'mysql':96,'flask':98},
    'dinesh':{'status':False,'python':80,'mysql':86,'flask':83},
    'teja':{'status':False,'python':70,'mysql':79,'flask':73},
    'kalyani':{'status':True,'python':30,'mysql':56,'flask':37},
    }

name = input("Enter the name : ")
if name in data :
    if data[name]['status'] :
        sum = data[name]['python'] + data[name]['mysql'] + data[name]['flask']
        avg = sum/3
        print(f"Hello {name}!!!")
        print(f"your average score is {avg}")
        if avg > 90 :
            print("outstanding performance")
        elif avg > 80 :
            print("very goof")
        elif avg > 70 :
            print("good, try hard")
        elif avg < 35 :
            print("Better luck next time")
        else :
            print("You failed the exam, try hard")

    else : 
       print(f"{name} did not attend the exam, bring your parents")
else :
    print ("{name} not found in the data")