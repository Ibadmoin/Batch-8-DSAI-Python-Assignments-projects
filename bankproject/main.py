
# defining a function to create a new account 
def create_account(accounts, name, initialBalance):

    if name in accounts:
        return f"Account with name '{name}' alread exists."
    accounts[name] = {
        'balance': initialBalance,
        'transactions': []
    }
    with open(f"{name}.txt",'w') as f:
        f.write(f"Account Name: {name}\nInitial Balance: {initialBalance}\n")
    return f"Account with name '{name}' created successfully."



# Deposit function to add money to the account

def deposit(accounts,name,amount):
    # here i am typecasting the amount type if possible: via error handling.
    try:
        amount = float(amount)
    except ValueError:
        return f"Invalid input. Amount must be a numeric value."            

    if name not in accounts:
        return f"Account with name '{name}' does not exist."
    if amount <= 0:
        return f"Deposit amount must be greater than zero."
    accounts[name]['balance'] += amount
    transaction = f"Deposited: {amount}. new Balance: {accounts[name]['balance']}"
    accounts[name]['transactions'].append(transaction)
    save_transaction(name,transaction)
    return f"Deposited {amount} into account '{name}' successfully.\n New Balance: {accounts[name]['balance']}"


# Withdrawal function to withdraw money from account
def withdraw(accounts,name,amount):
    # here i am typecasting the amount type if possible: via error handling.
    try:
        amount = float(amount)
    except ValueError:
        return f"Invalid input. Amount must be a numeric value."            


    if name not in accounts:
        return f"Account with name '{name}' does not exist."
    if amount <= 0:
        return f"Withdrawal amount must be greater than zero."
    
    if accounts[name]['balance'] < amount:
        return f"Insufficient balance in account '{name}'."
    
    accounts[name]['balance'] -= amount
    transaction = f"Withdrawal: {amount}. new Balance: {accounts[name]['balance']}"
    accounts[name]['transactions'].append(transaction)
    save_transaction(name,transaction)
    return f"Withdraw {amount} from account '{name}' successfully. \n Remaining balance: {accounts[name]['balance']}"



# function to check the current balance in users account

def check_balance(accounts,name):

    if name not in accounts:
        return f"Account with name '{name}' does not exist."
    
    return f"Current balance in account named '{name}' is: {accounts[name]['balance']}"



# a function  print_statement to print the account statement

def print_statement(accounts,name):
    if name not in accounts:
        return f"Account with name '{name}' does not exist."
    if not accounts[name]['transactions']:
        return f"No transactions in account '{name}'."
    statement= f"\t---Transaction statement for account name: '{name}'----\n"
    statement += "\n".join(accounts[name]['transactions'])
    return statement


# here i am creating a function to permenentaly save the transaction records
def save_transaction(name,transaction):
    with open(f"{name}.txt","a") as f:
        f.write(transaction + "\n")




if __name__ == "__main__":
    # Dictionary to store accounts
    accounts = {}

    # trying to create same name accounts 
    print(create_account(accounts,"jhon",500))
    # ------------------------
    print(create_account(accounts,"jhon",500))

    #  deposite money in account
    # negative money
    print(deposit(accounts,"jhon",-1500))
    # positive money
    print(deposit(accounts,"jhon","1500"))
    

    # Checking the current balance:
    print(check_balance(accounts,"jhon"))

    # widthdrawing with invalid account name
    print(withdraw(accounts,"ali",1000))

    # withdraw with valid account name
    print(withdraw(accounts,"jhon",1000))

    # print transaction statements:
    print(print_statement(accounts,"jhon"))
