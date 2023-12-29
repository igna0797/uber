from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from datetime import datetime, timedelta
import time

# Set the start and end dates for the current month
today = datetime.now()
start_date = today.replace(day=1)
end_date = today.replace(day=1, month=(today.month % 12) + 1) - timedelta(days=1)

# Set up the Chrome driver (you need to have Chrome and chromedriver installed)
driver = webdriver.Chrome()

# Navigate to the receipts page (assuming you are already logged in)
driver.get("https://riders.uber.com/trips/receipts")

# Wait for the receipts to load (adjust the time.sleep duration based on your internet speed)
time.sleep(5)

# Signal to continue
input("Press Enter when you are ready to continue...")
clase ="_css-gtxWCh"
# Extract receipt information as needed
receipts = driver.find_elements(By.CLASS_NAME ,value=clase)  # Adjust the class based on the actual structure
continuar = True
while(continuar == True):
    for i in range(len(receipts)):

        fechas= driver.find_elements(By.XPATH, value="//*[@id='wrapper']/div[1]/div[1]/div[2]/div/main/div/div[2]/section[1]/div/div/div[1]/p[2]")
        fecha = fechas[i]
        date_text = fecha.text.strip()
        #la fecha esta en español y no tengo ganas de ver como pasarla a ingles
        #receipt_date = datetime.strptime(date_text, "%B %d %Y, %H:%M")
        print(f"Fecha: {date_text}")
        if date_text.find('diciembre') != -1:
            receipts = driver.find_elements(By.CLASS_NAME ,value=clase)  # Adjust the class based on the actual structure
            # Process each receipt as needed
            receipt = receipts[i]
            receipt.click()
            time.sleep(1)
    #        fecha= driver.find_element(By.XPATH, value="//*[@id='wrapper']/div[1]/div[1]/div[2]/div/main/div/div[2]/div[1]/div")
    #        print(f"Fecha{fecha}")        
            try:
                view_receipt=  driver.find_element( By.XPATH,value="//*[@id='wrapper']/div[1]/div[1]/div[2]/div/main/div/div[2]/div[5]/div[1]/button")
                view_receipt.click()
                time.sleep(1)
                boton_descarga= driver.find_element(by=By.XPATH, value="//*[@id='wrapper']/div[2]/div/div[2]/div/div/div/div/div/div/div/a")
                boton_descarga.click()  
                time.sleep(0.2)
            except:
                print(f"No hay ningun recibo{receipt}")
                continue  
            driver.back()
            time.sleep(0.8)
#ask if you want to contunue
    print("Do you want to continue?")
    cont=input("y/n")
    if cont=="n":
        continuar=False

# Close the browser window
driver.quit()
