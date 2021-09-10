from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
import requests
import pandas as pd
PATH = "H:\\Uni )\\chromedriver.exe"
driver=webdriver.Chrome(PATH)
url="https://itdashboard.gov/"
driver.get(url)
page_source=driver.page_source
link=driver.find_element_by_link_text('DIVE IN')
link.click()
doc=BeautifulSoup(page_source,'html.parser')
soup1=doc.find_all('div',{'id':'agency-tiles-2-container'})
#######
'soup1 contains the body where every department and its money is mentioned'
#######
'if you want to see just print the below statement by removing the string'
'print(soup1)'
#############
'now lets scrape through it to take what we want...'
#########
name_and_money=(soup1[0].find_all('span'))
#print(name_and_money)
#######
' our desired data lies in the above command'
name=[]
money=[]
for i in soup1[0].find_all('span',{'class':'h4 w200'}):
    name.append(i.text)
for i in soup1[0].find_all('span',{'class':'h1 w900'}):
    money.append(i.text)
data1=zip(name,money)
data=dict(data1)
'Time to convert it to excel file'
df=pd.DataFrame(list(zip(name,money)))
df.columns=['Agency Name','Agency Spendings']
'Now export it'
df.to_excel('Agencies.xlsx')
#####################
'Task 2..........'

link2=driver.find_element_by_link_text('view')
link2.click()
time.sleep(30)
'selecting All in dropdown'
drpdown=Select(driver.find_element_by_name('investments-table-object_length'))
drpdown.select_by_visible_text('All')
time.sleep(20)
doc2a=driver.page_source
doc2=BeautifulSoup(doc2a,'html.parser')

##print(doc2)
soup2=doc2.find('div',{'id':'investments-table-container'})
print(soup2)
####
'Now lets fetch table contents'
'UII'
UII=[]
for i in soup2.find_all('td',{'class':'left sorting_2'}):
    UII.append(i.text)
'Bureau=[]'
Bureau=[]
for i in soup2.find_all('td',{'class':'left select-filter'}):
	Bureau.append(i.text)
'Inv_title=[]'
Inv_title=[]
for i in soup2.find_all('td',{'class':'left'}):
	Inv_title.append(i.text)
Total_Spend=[]
for i in soup2.find_all('td',{'class':'right'}):
	Total_Spend.append(i.text)
                         

                         
CIO_Rat=[]
for i in soup2.find_all('td',{'class':'center'}):
	CIO_Rat.append(i.text)
############
'Noticed that the class of Bureau and Type are the same '
'also CIO Rating and No of proj have same class'
'We will separate them by even and and odd combination as all the odd entries'
'are from one category and the even are from other'
bureau=[]
cio=[]
                         
type1=[]
No_of_proj=[]
for count, i in enumerate(Bureau):
    if count % 2 != 1:
        bureau.append(i)
    else:
        type1.append(i)                         

for count, i in enumerate(CIO_Rat):
    if count % 2 != 1:
        cio.append(i)
    else:
        No_of_proj.append(i)
'Cleaning Investment title'
for i in UII:
	for j in Inv_title:
		if i==j:
			Inv_title.remove(j)
for i in bureau:
	for j in Inv_title:
		if i==j:
			Inv_title.remove(j)

for i in type1:
	for j in Inv_title:
		if i==j:
			Inv_title.remove(j)
data23=pd.DataFrame()
data23['UII']=UII
data23['Bureau']=bureau
data23['Investment Title']=Inv_title
data23['Total FY2021 Spending ($M)']=Total_Spend
data23['CIO Rating']=cio
data23['# of Projects']=No_of_proj

data23.to_excel('Individual Investments.xlsx')

# now downling Business cases
'''
!!! Importtant for a single business case downloading we are using below code
other wise for multiple business caeses use the bottom most code after uncommenting
and comment the below code
'''
##bus=soup2.find('td',{'class':'left sorting_2'})
##p=driver.find_element_by_link_text(bus.text)
##p.click()
##time.sleep(20)
##p=driver.find_element_by_link_text('Download Business Case PDF')
##p.click()
##time.sleep(10)
##driver.back()
##driver.back()
links=[]
for a in soup2.find_all('a',href=True):
    links.append(a['href'])

for i in links:

    up=url+i
    driver.get(up)
    time.sleep(20)
    p=driver.find_element_by_link_text('Download Business Case PDF')
    p.click()
    time.sleep(10)
    
##for i in soup2.find_all('td',{'class':'left sorting_2'}):
##    
##    p=driver.find_element_by_link_text(i.text)
##    p.click()
##    time.sleep(20)
##    p=driver.find_element_by_link_text('Download Business Case PDF')
##    p.click()
##    
##    time.sleep(10)
##    u="https://itdashboard.gov/drupal/summary/005"
##    driver.get(u)
##    time.sleep(20)
##    dropdown=Select(driver.find_element_by_name('investments-table-object_length'))
##    dropdown.select_by_visible_text('All')
##    time.sleep(10)
    
    


##link2=WebDriverWait(driver,500).until(
##EC.element_to_be_clickable((By.XPATH,'//a[@href="'+'https://itdashboard.gov/drupal/summary/005'+'"]')))
##link2.click()

    
    
                                       


