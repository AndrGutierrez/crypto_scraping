from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
from bs4 import BeautifulSoup
import csv
 
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
 
url = "https://phemex.com/contract/funding-history"
fund_data= []
def load_soup():
    driver.get(url)
    time.sleep(5) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    return soup

page_amount=1
soup=load_soup()
pagination = soup.find('ul', attrs={'class' : 'pagination df fdr acc jcc'})
next = pagination.find('button', attrs={'class': 'mirror css-h4r5me'})
for i in range(page_amount):
    table = soup.find('tbody')
    rows =table.findAll('tr')
    i=0
    for row in rows:
        cols = row.findAll('td')
        fund = {}
        for col in cols:
            if col.text != 'undefined':
                if i==0:
                    fund['Time'] = col.text
                elif i==3:
                    fund['Funding Rate']=col.text
            i+=1
        fund_data.append(fund)
        i=0
    driver.execute_script("arguments[0].click();", next)
    soup = load_soup()


  
filename = 'funding_history.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Time','Symbol','Funding Interval','Funding Rate'])
    w.writeheader()
    for fund in fund_data:
        w.writerow(fund)
  
driver.close() # closing the webdriver
