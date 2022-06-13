import os
import math
import random
import smtplib

OTP=random.randint(999,9999)
otp ="Your verification OTP is "+ str(OTP)
sender="joker03072002@gmail.com"
password="Devendra@03"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender,password)
emailid = input("Enter your email: ")
s.sendmail(sender,emailid,otp)
a = int(input("Enter Your OTP >>: "))
# print(OTP)
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")