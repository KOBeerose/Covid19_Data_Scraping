import time
import string
from datetime import datetime, timedelta
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import Select


import requests
from bs4 import BeautifulSoup



# !!!!! this script is meant to work on https://www.liqahcorona.ma/fr website but you can make changes use it with another one !!!! 






"""# this function gets the user info and save them in variables
def get_info(filename): 
    elem_list=["url","email","firstname","lastname","password","card","zip","cvv","exp"]   # list of expressions preceding the user info
    with open(filename, 'r') as read_obj: 
            for line in read_obj:
                for elem in elem_list:  # Get the value after an expression occurrence
                    if elem in line:
                        globals()[elem] = line.partition(elem+": ")[2].translate({ord(c): None for c in string.whitespace})   # save the value in a variable named according to the expression preceding it

"""

# this function will add new lines the top of a file
def add_at_top(filename, lines): 
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(lines.rstrip('\r\n') + '\n' + content + '\n')



# configuration and direction to the website URL 

url= "https://www.liqahcorona.ma/fr"

options = EdgeOptions()
options.use_chromium= True
driver = Edge(options=options)
driver.get(url)
time.sleep(5)
htmlSource = driver.page_source
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print (html)


"""my_url="https://avi.im/stuff/js-or-no-js.html"
response = requests.get(my_url)
soup = BeautifulSoup(response.text,'html.parser')
print(soup.find(id="intro-text"))
"""
print("done")

"""# entering user's email and clicking the register button
fmail = driver.find_element_by_name("account_signup[email]")
fmail.send_keys(u_mail)

outside = driver.find_element_by_name("button")
outside.click()


# entering user's info and clicking the submit button
fname = driver.find_element_by_id("account_signup_first_name")
fname.send_keys(u_fname)

lname = driver.find_element_by_id("account_signup_last_name")
lname.send_keys(u_lname)

password = driver.find_element_by_id("account_signup_password")
password.send_keys(u_password)

card = driver.find_element_by_id("credit_card_number")
card.send_keys(u_card)

zp = driver.find_element_by_id("account_signup_postal_code")
zp.send_keys(u_zp)

cvv = driver.find_element_by_id("credit_card_cvv")
cvv.send_keys(u_cvv)

l1= driver.find_element_by_xpath("//fieldset[@id='consent-info']")
driver.execute_script("arguments[0].scrollIntoView(true);", l1)
time.sleep(0.4)

driver.find_element_by_xpath("//label[@class='form-label' and @for='account_signup_tos_consent']/span[@class='form-label-required']").click()
driver.find_element_by_xpath("//p[@class='radio-checkbox-note']").click()

sel1 = Select(driver.find_element_by_xpath("//select[@name='credit_card_month']"))
sel1.select_by_index(u_card_month)

sel2 = Select(driver.find_element_by_xpath("//select[@name='credit_card_year']"))
sel2.select_by_index(u_card_year)

l2= driver.find_element_by_xpath("//div[@class='form-footer']")
driver.execute_script("arguments[0].scrollIntoView(true);", l2)
time.sleep(0.4)

outside = driver.find_element_by_name("commit")
outside.click()

# wait for the page to refresh and add the account to the file Account if the sign_up process was successful
time.sleep(2)
if (driver.current_url=="https://teamtreehouse.com/welcome"):
    add_at_top("Accounts.txt", "from " + sdate + " to " + edate + "\nemail: " + u_mail + "\npassword: " + u_password + "\n \n")"""