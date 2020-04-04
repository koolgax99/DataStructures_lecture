class CreditCard:
    def __init__(self,customer,bank, card_number,balance):
        self.customer_name = customer
        self.bank_name = bank
        self.balance = balance
        self.credit_card_number = card_number

    def get_customer(self):
        return self.customer_name
    def get_bank(self):
        return self.bank_name
    def get_creditcard(self):
        return self.credit_card_number
    def get_balance(self):
        return self.balance
    def recharge(self):
        self.balance = 20000 + int(self.balance)
        return self.balance

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Raj','HDFC Bank','53710345 1245 2764',45000))
    wallet.append(CreditCard( 'Shyam' , 'ANZ Bank' ,' 3485 0399 3395 1954' , 35000))
    wallet.append(CreditCard( 'Mohan' , 'ICICI Bank' , '5391 0375 9387 5309' , 50000))

    for c in range(3):
        print( 'Customer=' , wallet[c].get_customer())
        print( 'Bank =' , wallet[c].get_bank())
        print('creditcard=',wallet[c].get_creditcard())
        print('balance=',wallet[c].get_balance())
        wallet[c].recharge()
        print("balance after recharge= ",wallet[c].get_balance() )
