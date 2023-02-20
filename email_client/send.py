"""
Module sends the mail as a helper for the node spawn process
"""

# path module
from pathlib import Path

# SMTP server essentials
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Configuration section
import sys
import os
import re
from constants.variables import MAIL_ID,MAIL_PASSWORD,SMTP_HOST,SMTP_PORT,APPNAME
# import dotenv

def send_mail(client:str,to:str,otp:str):
  try:
    FROM_MAIL = MAIL_ID
    TO_MAIL = to
    OTP=otp
    COMPANY_NAME = APPNAME

    # Create the HTML file
    HTML = ""
    STYLESHEET = ""

    with open(os.path.join(Path.cwd(), "email_client/custom", "style.css"), "r", encoding="utf-8") as template:
        STYLESHEET = template.readlines()

    with open(os.path.join(Path.cwd(), "email_client/custom", "index.html"), "r", encoding="utf-8") as template:
        for LINE in template:
            REGEX = r"({.*})"

            # Checking the presence of the style element
            if ("{style}" in re.findall(REGEX, LINE)):
                LINE += "\n<style>\n"
                LINE += "".join(STYLESHEET)
                LINE += "\n</style>\n"

            # Check the presence of the company name
            if ("{COMPANY_NAME}" in re.findall(REGEX, LINE)):
                splitLINE = LINE.split()
                for element in splitLINE:
                    if(re.match(REGEX, element)):
                        # print(splitLINE.index(element))
                        splitLINE[splitLINE.index(element)] = COMPANY_NAME
                LINE = " ".join(splitLINE)

            # Checking the presence of the OTP
            if ("{OTP}" in re.findall(REGEX, LINE)):
                splitLINE = LINE.split()
                for element in splitLINE:
                    if(re.match(REGEX, element)):
                        splitLINE[splitLINE.index(element)] = OTP
                LINE = " ".join(splitLINE)

            HTML = HTML + LINE if(HTML != "") else LINE


    message = MIMEMultipart('alternative')
    message['Subject'] = f"Login OTP for {COMPANY_NAME} is {OTP}"
    converted = MIMEText(HTML, 'HTML')
    message.attach(converted)

    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)

    server.starttls()
    try:
        server.login(MAIL_ID, MAIL_PASSWORD)
        server.sendmail(FROM_MAIL, [TO_MAIL], message.as_string())
        server.quit()
        print("PYTHON SERVER :: success sent mail")
    except Exception as error:
        print(error)
        print("PYTHON SERVER :: Server error -> Mailing section")
    finally:
        sys.exit(0)
  except Exception as error:
      print(error)
      print("Server error cannot send mail : section main")
