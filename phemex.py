from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.write_csv import write_csv
import time
 
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 
url = "https://phemex.com/contract/funding-history"
fund_data= []
driver.get(url)
time.sleep(2) 


# table_content=driver.find_elements(By.XPATH,"//div[@class='body svelte-15wjsvk']")
# print(table_content[0].get_attribute('innerHTML'))



page_amount=10
j=0
fund_data= []

next_button=driver.find_elements(By.XPATH,"//li[@class='next svelte-3tqfek']")[0]
table = driver.find_elements(By.XPATH,"//div[@class='body svelte-15wjsvk']")[0]
for i in range(page_amount):
    rows=table.find_elements(By.CLASS_NAME,"tr")
    print(j)
    for row in rows:
        content=row.find_elements(By.TAG_NAME, 'div')
        fund = {}
        # print(content)
        for span_tag in content:
            data = span_tag.find_elements(By.TAG_NAME, 'span')[0].get_attribute('innerHTML')
            if j==0:
                fund['Time'] = data
            elif j==3:
                fund['Funding Rate']= data
            j+=1
        j=0
        # print(fund)
        fund_data.append(fund)
    driver.execute_script("arguments[0].click();", next_button)
    time.sleep(2)

  
filename = './data/phemex.csv'
write_csv(filename, fund_data)
  
driver.close() # closing the webdriver
