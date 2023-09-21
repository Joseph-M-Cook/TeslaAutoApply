from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

JobApplicationLink = r"https://www.tesla.com/careers/search/job/apply/208569"

# Personal Information
firstName = ""
middleName = ""
lastName = ""
preferredName = ""
phoneNumber = ""
email = ""
LinkedIn = r""
GitHub = r""
Resume = ""  

startDate = "May 5, 2024"
# Configure Browser Options
options = webdriver.ChromeOptions()

# Set up the Chrome web driver w/ Options
driver = webdriver.Chrome(options=options)  # If chromedriver is not in PATH, use: webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the URL and Set Zoom Level to 50% (Visibilty/Monitoring)
driver.get(JobApplicationLink)
driver.execute_script("document.body.style.zoom='50%'")
time.sleep(0.2)

######################################## PAGE 1 ########################################

# Open Social Link Fields
button = driver.find_element(By.XPATH, '//*[@id="step--personal"]/div/div[9]/button')
driver.execute_script("arguments[0].click();", button)
time.sleep(.2)
driver.execute_script("arguments[0].click();", button)

# Find all input fields
input_fields = driver.find_elements(By.TAG_NAME, 'input')
final_fields = []

# Validate Input Fields
for field in input_fields:
    try:
        if field.is_displayed() and not field.get_attribute('readonly'):
            final_fields.append(field)
    except Exception as e:
        print(f"Could not input into the field. Reason: {e}")

final_fields[0].send_keys(firstName)
final_fields[1].send_keys(lastName)
final_fields[2].send_keys(middleName)
final_fields[3].send_keys(preferredName)
final_fields[4].send_keys(phoneNumber)
final_fields[5].send_keys(email)
final_fields[6].send_keys(LinkedIn)
final_fields[7].send_keys(GitHub)

# Dropdown Handler
dropdowns = driver.find_elements(By.TAG_NAME, 'select')

# Contact Phone Type
dropdown = dropdowns[0]
select = Select(dropdown)
select.select_by_visible_text('Mobile')

# Country/Region of Residence
dropdown = dropdowns[1]
select = Select(dropdown)
select.select_by_visible_text('United States')

# Profile Link Type: LinkedIn
dropdown = dropdowns[2]
select = Select(dropdown)
select.select_by_visible_text('LinkedIn')

# Profile Link Type: Portfolio (GitHub)
dropdown = dropdowns[3]
select = Select(dropdown)
select.select_by_visible_text('Portfolio')

# Filepath to Resume
final_fields[8].send_keys(Resume)
time.sleep(0.2)

# Go to the next page
button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div/div[2]/button')
driver.execute_script("arguments[0].click();", button)

######################################## PAGE 2 ########################################

# Find all input fields
input_fields = driver.find_elements(By.TAG_NAME, 'input')
final_fields = []

# Validate Input Fields
for field in input_fields:
    try:
        if field.is_displayed() and not field.get_attribute('readonly'):
            final_fields.append(field)
    except Exception as e:
        print(f"Could not input into the field. Reason: {e}")

# Go to the next page
time.sleep(1)
button = driver.find_element(By.XPATH, '//*[@id="step--job"]/fieldset/div[1]/div/div/div[1]/button')
driver.execute_script("arguments[0].click();", button)

time.sleep(0.2)
button = driver.find_element(By.XPATH, '//*[@id="step--job"]/fieldset/div[1]/div/div/div[2]/div/div[1]/button[2]')

# Select the Month
for j in range(8):
    driver.execute_script("arguments[0].click();", button)
    time.sleep(.2)

# Select the day
button = driver.find_element(By.XPATH, '//*[@id="step--job"]/fieldset/div[1]/div/div[1]/div[2]/div/div[3]/button[8]')
driver.execute_script("arguments[0].click();", button)

# Dropdown Handler
dropdowns = driver.find_elements(By.TAG_NAME, 'select')

# How many months are you available to participate in an internship?
dropdown = dropdowns[0]
select = Select(dropdown)
select.select_by_visible_text('3 months')
time.sleep(.2)

# Are you available to work full-time or part-time as part of an internship?
dropdown = dropdowns[1]
select = Select(dropdown)
select.select_by_visible_text('Full time')
time.sleep(.2)

element = driver.find_element(By.XPATH, '//label[text()="No"]')
driver.execute_script("arguments[0].click();", element)
time.sleep(.2)

# Do you need to write a thesis or report for your university as part of your internship? (No)
button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div/div[2]/button[2]')
driver.execute_script("arguments[0].click();", button)
time.sleep(1)

######################################## PAGE 3 ########################################

# Dropdown Handler
dropdowns = driver.find_elements(By.TAG_NAME, 'select')

# What is your availability or notice period?
dropdown = dropdowns[0]
select = Select(dropdown)
select.select_by_visible_text('Immediately')
time.sleep(.2)

# Obtain Radio Elements
NO_elements = driver.find_elements(By.XPATH, '//label[text()="No"]')
YES_elements = driver.find_elements(By.XPATH, '//label[text()="Yes"]')

# I authorize Tesla ... to the specific job I am applying for.
driver.execute_script("arguments[0].click();", YES_elements[0])

# Will you now or in the future require immigration sponsorship for employment with Tesla?
driver.execute_script("arguments[0].click();", NO_elements[1])

#Have you previously been employed by Tesla?
driver.execute_script("arguments[0].click();", NO_elements[2])

# Are you a former/current intern or contractor?
driver.execute_script("arguments[0].click();", NO_elements[3])

# Are you a current university student?
driver.execute_script("arguments[0].click();", YES_elements[4])

# Are you a current university student?
driver.execute_script("arguments[0].click();", YES_elements[5])

# TOS
element = driver.find_element(By.XPATH, '//label[text()="I have read and understand the statements above and accept them as conditions of employment."]')
driver.execute_script("arguments[0].click();", element)
time.sleep(.2)

# Legal Name Signature
namefield = driver.find_elements(By.NAME, 'legal.legalAcknowledgmentName')
namefield[0].send_keys(f"{firstName} {lastName}")
time.sleep(.2)

# If you are a current university student, please provide your anticipated graduation date?
element = driver.find_element(By.XPATH, '//*[@id="step--legal"]/fieldset[1]/div[7]/div/div/div[1]/button')
driver.execute_script("arguments[0].click();", element)
time.sleep(.2)
# Choose Month
for i in range(20):
    element = driver.find_element(By.XPATH, '//*[@id="step--legal"]/fieldset[1]/div[7]/div/div/div[2]/div/div[1]/button[2]')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(.2)
# Choose Day
element = driver.find_element(By.XPATH, '//*[@id="step--legal"]/fieldset[1]/div[7]/div/div/div[2]/div/div[3]/button[9]')
driver.execute_script("arguments[0].click();", element)
time.sleep(.2)

# Next Page
element = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/form/div/div[2]/button[2]')
driver.execute_script("arguments[0].click();", element)
time.sleep(1)

######################################## PAGE 4 ########################################

# Scroll to the bottom of the ToS fieldset
tos_element = driver.find_element(By.XPATH, '//*[@id="step--eeo"]/fieldset[1]/div[1]/div/div[5]')
driver.execute_script("arguments[0].scrollIntoView(true);", tos_element)
time.sleep(1)

# TOS
Label = "I acknowledge that I have read and understood Tesla's Equal Employee Opportunities."
element = driver.find_element(By.XPATH, f'//label[text()="{Label}"]')
driver.execute_script("arguments[0].click();", element)
time.sleep(0.2)

# Dropdown Handler
dropdowns = driver.find_elements(By.TAG_NAME, 'select')

# Gender
dropdown = dropdowns[0]
select = Select(dropdown)
select.select_by_visible_text('Male')
time.sleep(.2)

# Veteran Status
dropdown = dropdowns[1]
select = Select(dropdown)
select.select_by_visible_text('I am not a protected veteran')
time.sleep(.2)

# Race/Ethnicity
dropdown = dropdowns[2]
select = Select(dropdown)
select.select_by_visible_text('White')
time.sleep(.2)

# Disability
dropdown = dropdowns[3]
select = Select(dropdown)
select.select_by_visible_text("No, I don't have a disability")
time.sleep(.2)

# Legal Name Signature
namefield = driver.find_elements(By.NAME, 'eeo.eeoDisabilityStatusName')
namefield[0].send_keys(f"{firstName} {lastName}")
time.sleep(.2)

# Next Page
Label = "I acknowledge that I have read and understood Tesla's Equal Employee Opportunities."
element = driver.find_element(By.XPATH, f'//*[@id="app"]/div/div/form/div/div[2]/button[2]')
driver.execute_script("arguments[0].click();", element)
time.sleep(0.2)

######################################## PAGE 5 ########################################

time.sleep(360)
driver.quit()
