'''
This script notifies the user of price drops on his/her selected items.
Made by Zain
'''
#!importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import pandas as pd
import time
import smtplib
from email.mime.text import MIMEText

#!defining path to get files
dest_path = 'xyz:\\DarazBot\\'

#!Reading input sheet
input_sheet = pd.read_csv(dest_path+'Input.csv')

#!making a list of the URL column to iterate over
urls = input_sheet.URL.tolist()

#!making chrome headless to save memory/cpu
options = webdriver.ChromeOptions()
options.add_argument('--headless')

#!mailing function
def send_mail(url, ind):
    with smtplib.SMTP('smtp.gmail.com', 587) as email:
        #!encrypt connection
        email.starttls()
        
        #!Login
        email.login('xyz@gmail.com','xyz123')

        #!Defining body and subject
        message = MIMEText('The item ' + str(input_sheet.loc[input_sheet.index[ind], 'Item']) + ' has fallen to desired range, check ' + str(url))
        message['Subject'] = 'DARAZ.PK PRICE DROP ALERT!'

        #!sending mail (To, From, message)
        email.sendmail('xyz@gmail.com', 'xyz@gmail.com', message.as_string())

#!Iterating over URLs
for url in urls:

    #!getting threshold value for that item
    threshold = input_sheet.loc[input_sheet.index[urls.index(url)], 'Threshold']
    #my_request = urlopen(url)

    with webdriver.Chrome("xyz:\\ChromeDriver\\chromedriver.exe", chrome_options=options) as driver:    
        
        #!open url and wait 1 minute for it to fully load
        driver.get(url)
        time.sleep(60)

        #!get html from the page
        my_html = driver.page_source

        #!passing html to beautifulsoup 
        my_soup = soup(my_html, "html.parser")

    #!find <div> which contains price
    item = my_soup.find("div", class_="pdp-product-price")

    #!convert the digits to a float value (leaving the currency symbol)
    price = [float(s) for s in item.span.text.split() if s.isdigit()][0]

    #!updating current price in DataFrame
    input_sheet.loc[input_sheet.index[urls.index(url)], 'CurrentPrice'] = price

    #!Send mail if price is less than or equal to threshold
    if price <= threshold:
        send_mail(url, urls.index(url))

#!update CSV file (so it contains latest prices)
input_sheet.to_csv(dest_path+'Input.csv', index=False)

