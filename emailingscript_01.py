#Author: James Ellerbee
#Date: 10/30/18
#Purpose: This script is responsible for sending emails based on a given input

from os.path import basename
from smtplib import SMTP
#email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
#pie library in order to detect changes in pins

user = ''
pass_w = ''
file_path = "./test.jpg"
testing_email = "coreystewart149@gmail.com"

def login(s):
    """Starts encryption and uses credentials to logon to the smtp server."""
    s.starttls()
    s.login(user, pass_w)

def test_mail(s):
    """Used in testing SMTP.sendmail()""" 
    s.sendmail(user, testing_email, "helloworld")
    
    
def custom_mail(s, str_msg = None):
    """Used in sending custom messages"""
    if str_msg == None:
        str_msg = input("enter a custom message: ")                                               
    s.sendmail(user, testing_email, str_msg)
    
def test_emailAttachments(s):
    """Method used in teasting adding attachments to a message using MIMEMultipart and MIMEApplication"""
    msg = MIMEMultipart()       # create a message
    msg['From'] = user
    msg['To'] = testing_email
    msg['Subject'] = "This is a test"
    #code responsible for opening file and constructing a MIMEApplication
    with open(file_path, "rb") as fil:
            part = MIMEApplication( 
                fil.read(),
                Name=basename(file_path)
            )#create MIMEApplication object
    #attach "content" to the message and then send it
    part["Content-Disposition"] = 'attachment; filename = "%s"' % basename(file_path)
    msg.attach(part)

    s.send_message(msg)

def main():
    s = SMTP(host = 'smtp.gmail.com',port = 587)
    login(s)
    ### Finish set up ###
    #test_mail(s)
    #custom_mail(s)
    #test_emailAttachments(s)
    s.close()
    
main()
print("done")
