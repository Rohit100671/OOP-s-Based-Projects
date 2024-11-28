'''WAP to print bank software with help of oop's concept'''
class Bank:
    # Satic or Class Variables
    bank_name="State Bank Of India"
    ifsc="sbin13456"
    branch="Karve Nagar,Pune"

    def __init__(self,n,city,an,b):
        # Instance Variables
        self.name=n
        self.city=city
        self.acc_no=an
        self.bal=b

    # Instance Method
    def c_detail(self):
        return f"""
        - Account Holder Details -
        Holder Name : {self.name}
        Holder City : {self.city} 
        Bank Name : {self.bank_name}
        IFC Code : {self.ifsc}
        Bank Branch : {self.branch}
        Account Number : {self.acc_no}
        Balance : {self.bal}     """
    
    # Class Methods 
    @classmethod
    def bank_detail(cls):
        return f"""
            - Bank detail -
            Bank Name : {cls.bank_name}       
            IFSC Code : {cls.ifsc}    
            Branch : {cls.branch}   """   

    # Instance Method Deposit Amount
    def deposit(self,amount):
        self.bal=self.bal+amount
        return f""" SBI Rs.{amount} is Credited to your Ac. XXXXXX{self.acc_no[-4::1]}. Avl Balance is {self.bal} """ 
    # Instance Method For Withrawl Amount
    def withdrawl(self,amount):
        if self.bal>=amount:
            self.bal=self.bal-amount
            return f""" SBI Rs.{amount} is Debited to your Ac. XXXXXX{self.acc_no[-4::1]}. Avl Balance is {self.bal} """ 
        else:
            return "Insufficient Amount Entered..."

    # Static Method To check Interest 
    @staticmethod
    def simple_interest(p,r,t):
        si=(p*r*t)/100
        return f"""Simple Interes is {si}"""


c1=(Bank("Rohit","Nagpur","12345678911",100000))
print(c1.c_detail())
print(c1.bank_detail())
print(c1.withdrawl(50000))
print(c1.simple_interest(100000,8,2))