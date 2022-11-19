import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# yahoo_mail = "new.kuan@yahoo.com.tw"
# yahoo_password = "zQc(Q*5Pa'PLYzU"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()  #TLS 安全協定
#     connection.login(user= yahoo_mail, password=yahoo_password)
#     connection.sendmail(
#         from_addr=yahoo_mail, 
#         to_addrs="charlieischao@gmail.com",
#         msg="Hello"
#     )

import datetime as dt
import pandas as pd
import random as rd
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
# hour = now.hour
# min = now.minute
# second = now.second
day_of_week = now.weekday()  # 0 == Mon 1 == Tue

with open('day32-Email-SMTP/quotes.txt', "r") as data:
    quotes = data.readlines()
    
if day == 2:
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:    
            # Email content
            content = MIMEMultipart()  #建立MIMEMultipart物件
            content["subject"] = "Test"  #郵件標題
            content["from"] = "new.chaoci@gmail.com"  #寄件者
            #===============多個收件者===============
            recipients = ["new.chaocigmail.com"]
            # "a20264520@gmail.com", "elroypeng1010@gmail.com"
            content["to"] =", ".join(recipients) #收件
            content.attach(MIMEText("TEST:!!!"))  #郵件內
            #Email data
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("new.chaoci@gmail.com", "phtjrynxvtwjsbdm")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Email Send Complete!")
        except Exception as e:
            print("Error message: ", e)
