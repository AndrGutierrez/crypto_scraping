from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from utils.write_csv import write_csv
 
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 
url = "https://www.binance.com/en/futures/funding-history/perpetual/1"
fund_data= []
driver.get(url)
time.sleep(2) 


# table_content=driver.find_elements(By.XPATH,"//div[@class='body svelte-15wjsvk']")
# print(table_content[0].get_attribute('innerHTML'))



page_amount=5
j=0
fund_data= []

next_button=driver.find_elements(By.XPATH,"//button[@id='next-page']")[0]
table = driver.find_elements(By.XPATH,"//tbody[@class='bn-table-tbody']")[0]
for i in range(page_amount):
    rows=table.find_elements(By.TAG_NAME,"tr")
    for row in rows[1:]:
        row_data=row.find_elements(By.TAG_NAME, 'td')
        fund = {}
        for item in row_data:
            data = item.get_attribute('innerHTML')
            print(data)
            if j==0:
                fund['Time'] = data
            elif j==2:
                fund['Funding Rate']= data
            j+=1
        j=0
        # print(fund)
        fund_data.append(fund)
    driver.execute_script("arguments[0].click();", next_button)
    time.sleep(2)

  
filename = './data/binance.csv'
write_csv(filename, fund_data)
driver.close() # closing the webdriver
