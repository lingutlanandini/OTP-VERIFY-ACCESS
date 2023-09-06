import random
a=random.randrange(10000,99999)
user_name=input("Enter your Name: ")
print("Hello!",user_name)
print("Your OTP is",a)
otp=input("Enter OTP to Login: ")
if otp==str(a):
    print("Login Access Successuful")
else:
    print("Login Acces Failed")


