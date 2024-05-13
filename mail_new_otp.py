import random
import smtplib
from email.message import EmailMessage

otp = ""
for i in range(4):
    otp += str(random.randint(0, 9))
print("The Otp Generated is:", otp)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_mail = 'vishalshankar105@gmail.com'
server.login(from_mail, 'begr qnnc ofcp yggj')
mail_list = []
mail_inp = int(input("Enter the number of user you want to sent the mail:"))
for i in range(mail_inp):
    to_mail = input("Enter your Email: ")
    mail_list.append(to_mail)
print(mail_list)
msg = EmailMessage()
msg['Subject'] = "OTP Verification......."
msg['From'] = from_mail
msg['To'] = ','.join(mail_list)
msg.set_content("Your otp is: " + otp)

server.send_message(msg)
print("Email Sent Sucessfully..........")
input_otp = input("Enter OTP: ")
if input_otp == otp:
    print("OTP Verified......")
else:
    print("Invalid OTP.......")
