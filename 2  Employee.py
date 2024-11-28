''' WAP to print Employee manegment with the help of oop's concept'''
class Company:
    # Static Variables
    company_name="TCS"
    branch="pune"
    company_code="1023466798100"
    TDS=(2/100)

    # Constructor
    def __init__(self,id,n,c,dep,po,s,mo):
        # Instance Variables
        self.emp_ID=id
        self.emp_name=n
        self.city=c
        self.department=dep
        self.post=po
        self.salary=s
        self.mobile_no=mo
    
    # Instance method
    def employee_detail(self):
        return f"""
                *** EMOPLOYEE DETAILS ***
                Emp_ID : {self.emp_ID}
                Emp_Name : {self.emp_name}
                City : {self.city}
                Moblie No. : {self.mobile_no}
                Company Name : {self.company_name}
                Branch : {self.branch}
                Company Code : {self.company_code}
                Departments : {self.department}
                Emp_Post : {self.post}
                Salary : {self.salary}  """
    
    # Class Method
    @classmethod
    def company_details(cls):
        return f"""
                *** COMPANY DETAILS ***
                Company Name : {cls.company_name}
                Company Branch : {cls.branch}
                Company Code : {cls.company_code}    """
    
    # instance Method to find employee salary
    # hra=> house ren allowance
    # pf=> provident fund'''
    def salary_detail(self,pf,hra):
        if self.salary>pf:
            self.salary=self.salary-pf
            self.salary=self.salary-hra
            self.salary=self.salary-self.TDS
            return f"""
                Rs.{pf} PF amount, Rs.{hra} HRA amount and {Company.TDS}% TDS are removed from your salary. Then Avl Balance is {self.salary} Rs.    """

    # Satic Meethod
    @staticmethod
    def Experiance(*expariance):
        sum=0
        for i in expariance:
            sum=sum+i
        return f""" Firstly Employee Work Expariance is {expariance[0:-1]} then after few years Employee Has {sum} Years work Expariance. """

e1=Company("1011","ROhit","Pune","Developer","Python Developer",100000,9689104900)
print(e1.employee_detail())
print(e1.company_details())
print(e1.salary_detail(20000,20000))
print(e1.Experiance(2,3,5))