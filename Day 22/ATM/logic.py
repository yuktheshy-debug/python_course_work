data = {
    123456 : {"name" : "yukthesh","pin" : 1234, "balance" : 5000,"history":[]},
    123456 : {"name" : "yuk","pin" : 1234, "balance" : 5000,"history":[]},
    123456 : {"name" : "ssr","pin" : 1234, "balance" : 5000,"history":[]},
    123456 : {"name" : "shreya","pin" : 1234, "balance" : 5000,"history":[]},
}

def login(): 
    global acc_num 
    acc_num = int(input("Enter the account number: ")) 
    pin = int(input("Enter the pin: ")) 
    if acc_num["pin"] == pin: 
        print(f"acc_num['name]['pin']['balance]") 
    else: 
        print("Invlid loggin")

def menu(): 
    print(f"Welcome to the ATM, {data[acc_num]['name']}") 
    print('[C]heck balance') 
    print('[D]eposit') 
    print('[W]ithdraw') 
    print('[V]iew transaction') 
    print('[E]xit')

def checkbalance(): 
    print(f'Hello {data[acc_num]["name"]},') 
    print("Current Balance:",data[acc_num]["balance"],end='\n\n')

def deposit(): 
    amount = int(input("Enter the amount to deposit: ")) 
    data[acc_num]["balamce"]+=amount 
    data[acc_num]["history"].append(f"{amount} is deposited") 
    print(f"{amount} is deposited successfully") 
    checkbalance()

def withdraw(): 
    amount = int(input("Enter the amount to withdraw : ")) 
    if data[acc_num]["balance"]>=amount: 
        data[acc_num]["balance"]-=amount 
        data[acc_num]["history"].append(f"{amount} is withdrawed") 
        print(f"{amount} is withdrawed successfully") 
        checkbalance()
    else: 
        print("Insufficient Balance")

def viewtransaction(): 
    if data[acc_num]["history"]: 
        print("======== Transaction History======") 
        for i in data[acc_num]["history"]: print(i) 
        else: 
            print("=========== End of the History ========") 
    else: 
        print("NO Transaction History")


    
