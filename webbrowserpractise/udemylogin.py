from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the chromedriver executable
chromedriver_path = "C:\Users\vslpv\AppData\Local\Programs\Python\Python311\Lib\site-packages\selenium\webdriver\common\driver"

# Initialize the Chrome browser
driver = webdriver.Chrome(chromedriver_path)

# Open the Udemy website
driver.get("https://www.udemy.com")

# Find and click the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Log in')]"))
)
login_button.click()

# Find the username and password input fields and enter the credentials
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email--1"))
)
username_field.send_keys("your_username")

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_password"))
)
password_field.send_keys("your_password")

# Find and click the login button
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log In')]"))
)
login_button.click()

# Close the browser
driver.quit()