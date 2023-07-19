from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

# Configure webdriver options
options = FirefoxOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up webdriver
driver = webdriver.Firefox(options=options)
driver.get("https://divar.ir/s/tehran/car?q=%D9%BE%DA%98%D9%88%20206%20%D8%AA%DB%8C%D9%BE%202")

# Get scroll height
ads = []

last_height = driver.execute_script("return document.body.scrollHeight")
TotalTime = 0
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    if TotalTime > 4000:
        break

    last_height = new_height
    TotalTime += 1
    anchors = driver.find_elements(By.TAG_NAME, 'a')
    for anchor in anchors:
        href = anchor.get_attribute("href")
        ads.append(href)

        

driver.quit()

# Print the ads
#print(ads)
filtered_ads = [href for href in ads if "-206" in href]
print(len(filtered_ads))
for ad in filtered_ads:
    print(ad)

color_ = []
year_ = []
mileage_ = []
motor_ = []
Insurance_ = []
body_ = []
shasi_ = []
price_ = []

driver = webdriver.Chrome()
for ad in filtered_ads:

    try:
        time.sleep(3)

        driver.get(ad)
        color = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[1]/div[3]/span[2]')
        year = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[1]/div[2]/span[2]')
        mileage = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[1]/div[1]/span[2]')
        motor = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[4]/div[2]/p')
        Insurance = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[8]/div[2]/p')
        body = driver.find_element(By.XPATH ,'//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/p')
        shasi = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[9]/div[2]/p')
        price = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div[1]/div[4]/div[10]/div[2]/p')

        #mileage = driver.find_element(By.XPATH,'')
        color_.append(color.text)
        year_.append(year.text)
        mileage_.append(mileage.text)
        motor_.append(motor.text)
        Insurance_.append(Insurance.text)
        body_.append(body.text)
        shasi_.append(shasi.text)
        price_.append(price.text)
    except:
        pass

    





driver.quit()

# Save data to CSV file
data = zip(color_,year_,mileage_,motor_,Insurance_,body_,shasi_,price_)
with open('cata.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Color','Year','Mileage','motor','Insurance','Body','shasi','Price'])
    writer.writerows(data)
    csvfile.close()