from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import io

import lxml

urls="http://www.archives.com/member/Default.aspx?_act=VitalSearchResult&lastName=Smith&state=UT&country=US&deathYear=2004&deathYearSpan=10&location=UT&activityID=9b79d578-b2a7-4665-9021-b104999cf031&RecordType=2"





##print(driver.page_source)

url= "https://www.liqahcorona.ma/fr"

options = EdgeOptions()
options.use_chromium= True
driver1 = Edge(options=options)
driver = driver1.PhantomJS(executable_path='\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get(url)
time.sleep(5) # Pause to allow you to inspect the browser.




html = driver.execute_script("return document.documentElement.outerHTML;")
innerHTML = driver.execute_script("return document.body.innerHTML")

a = ActionChains(driver)

# perform the ctrl+u pressing action

ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .send_keys("U") \
    .key_up(Keys.CONTROL) \
    .perform()



with io.open('output.html', 'a+', encoding="utf-8") as f:
    f.write(html)


import bs4    #import beautifulsoup
import re
from time import sleep

sleep(1)      #wait one second 
root=bs4.BeautifulSoup(innerHTML,"lxml") #parse HTML using beautifulsoup
viewcount=root.find_all("p",attrs={'class':'subtitle'}) 
for span in viewcount:
    print(span.string) 



"""# Opening the html file
HTMLFile = open("output.html", "r",encoding="utf-8")
  
# Reading the file
index = HTMLFile.read()
  
# Creating a BeautifulSoup object and specifying the parser
Parse = bs(index, 'lxml')

soup = BeautifulSoup(HTMLFile)

subtitles = soup.find_all("p", class_= "subtitle")
print(subtitles)
for subtitle in subtitles:
    print(subtitle)
"""


