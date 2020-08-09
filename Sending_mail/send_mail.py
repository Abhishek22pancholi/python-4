import smtplib
import myTest
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
#import secret as sc

username = myTest.username
password = myTest.password
email = myTest.email
def send_mail(from_email = email, text="Email Body", subject="Hello World", to_emails=None, html=None):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From']= from_email
    msg['To']=", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html != None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part) 
      
    msg_str = msg.as_string()
    #login to smtp serverexit
    server = smtplib.SMTP(host='smtp.gmail.com', port= 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails,  msg_str)
    server.quit()
#    with smtplib.SMTP() as server:
#        server.quit()
#        pass