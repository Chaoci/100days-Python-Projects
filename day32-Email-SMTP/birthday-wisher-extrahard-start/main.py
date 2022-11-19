##################### Extra Hard Starting Project ######################
import pandas as pd 
import datetime as dt
import random as rd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 1. Update the birthdays.csv
try:
    data_birthday = pd.read_csv('day32-Email-SMTP/birthday-wisher-extrahard-start/birthdays.csv')
except FileNotFoundError:
    with open('day32-Email-SMTP/birthday-wisher-extrahard-start/birthdays.csv','r') as data:
        data_birthday = data.readlines()

def new_letter():
    with open('day32-Email-SMTP/birthday-wisher-extrahard-start/letter_templates/letter_1.txt','r') as letter1:
        letter1_content = letter1.readlines()
    with open('day32-Email-SMTP/birthday-wisher-extrahard-start/letter_templates/letter_2.txt','r') as letter2:
        letter2_content = letter2.readlines()
    with open('day32-Email-SMTP/birthday-wisher-extrahard-start/letter_templates/letter_3.txt','r') as letter3:
        letter3_content = letter3.readlines()

    total_letter = [letter1_content, letter2_content, letter3_content]
    res = " ".join(total_letter[rd.randint(0,2)])
    res = res.replace("[NAME]", i["name"])
    return res
        
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()  #抓現在時間
# year = now.year
month = now.month #當月月份
day = now.day #當日日期
data_birthday = pd.read_csv('day32-Email-SMTP/birthday-wisher-extrahard-start/birthdays.csv')  # read data
data_birthday.iterrows() #give the data index 
birthday_dict = data_birthday.to_dict(orient="record") # good for seeing the data
for i in birthday_dict:
    if i['month'] == month and i['day']==day:
        ans = new_letter()
        
with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:    
        # Email content
        content = MIMEMultipart()  #建立MIMEMultipart物件
        content["subject"] = "Test"  #郵件標題
        content["from"] = "new.chaoci@gmail.com"  #寄件者
        #===============多個收件者===============
        recipients = ["new.chaoci@gmail.com"]
        # "a20264520@gmail.com", "elroypeng1010@gmail.com"
        content["to"] =", ".join(recipients) #收件
        content.attach(MIMEText(f"{ans}"))  #郵件內
        #Email data
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("new.chaoci@gmail.com", "phtjrynxvtwjsbdm")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("Email Send Complete!")
    except Exception as e:
        print("Error message: ", e)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




