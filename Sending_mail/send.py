import myTest
from  formating import format_msg
from  send_mail import send_mail

username = myTest.username
password = myTest.password
email = myTest.email

userEmail= []

def setUserEmail (new_userEmail):
    userEmail.append(new_userEmail)

def send (name, website, subject):
    msg= format_msg(name, website)
    send_mail(email, msg, subject, userEmail)