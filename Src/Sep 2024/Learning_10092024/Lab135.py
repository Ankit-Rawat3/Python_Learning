#Custom Exception

"""
Ex
bal =100
withdrawl_made =1000

"""

class CustomException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)



balance=100
withdraw=1000

if withdraw>balance:
    raise CustomException("Balance insufficient")
else:
    print("Remain Bal",balance)
