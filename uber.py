from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from datetime import datetime, timedelta
import time

# Set the start and end dates for the current month
today = datetime.now()
start_date = today.replace(day=1)
end_date = today.replace(day=1, month=(today.month % 12) + 1) - timedelta(days=1)
mes =  'feb'
# Set up the Chrome driver (you need to have Chrome and chromedriver installed)
driver = webdriver.Chrome()

# Navigate to the receipts page (assuming you are already logged in)
driver.get("https://riders.uber.com/trips/receipts")

# Wait for the receipts to load (adjust the time.sleep duration based on your internet speed)
time.sleep(5)

# Signal to continue
input("Press Enter when you are ready to continue...")
clase ="_css-iGpqSb"
# Extract receipt information as needed
continuar = True
while(continuar == True):
    receipts = driver.find_elements(By.CLASS_NAME ,value=clase)  # Adjust the class based on the actual structure
    # Use CSS selector to find all elements inside a div with the specified string
    for i in range(len(receipts)):
        receipts = driver.find_elements(By.CLASS_NAME ,value=clase)  
        receipt = receipts[i]
        #fechas= driver.find_elements(By.XPATH, value="//section[@data-baseweb='card']//p[@class='_css-dTqljZ']")
        #fecha = fechas[i]
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        fecha = WebDriverWait(driver, 1,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.XPATH,f".//*[contains(text(),'feb')]")))
       # fecha = receipt.find_elements(By.XPATH,f".//*[contains(text(),'feb')]")
        #fecha = fecha[0]
        date_text = fecha.text.strip()
        #la fecha esta en español y no tengo ganas de ver como pasarla a ingles
        #receipt_date = datetime.strptime(date_text, "%B %d %Y, %H:%M")
        print(f"Fecha: {date_text}")

        # Process each receipt as needed
        receipt.click()
        time.sleep(1)
    #    fecha= driver.find_element(By.XPATH, value="//*[@id='wrapper']/div[1]/div[1]/div[2]/div/main/div/div[2]/div[1]/div")
    #    print(f"Fecha{fecha}")        
        
        try:
            view_receipt=  driver.find_element( By.XPATH,value="//*[@id='wrapper']/div[1]/div[1]/div[2]/div/main/div/div[2]/div[5]/div[1]/button")
            view_receipt.click()
            time.sleep(1)
            boton_descarga= driver.find_element(by=By.XPATH, value="//*[@id='wrapper']/div[2]/div/div[2]/div/div/div/div/div/div/div/a")
            boton_descarga.click()  
            time.sleep(0.2)
        except:
            print(f"No hay ningun recibo{receipt}")
        driver.back()
        time.sleep(0.8)
#ask if you want to contunue
    print("Do you want to continue?")
    cont=input("y/n: ")
    if cont=="n":
        continuar=False

# Close the browser window
driver.quit()
