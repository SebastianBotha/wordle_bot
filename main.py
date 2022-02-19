# imports
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import traceback

# ========================= INIT DRIVER ============================================
#https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi

options = Options()
options.add_argument('--incognito')
options.add_argument("window-size=720,1400")

# ====== use for mac =====

# path to chrome driver: MACBOOK 

ChromDriver_path = '/usr/local/Caskroom/chromedriver/97.0.4692.71/chromedriver'
s = Service(ChromDriver_path)
driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(options=options)

# get data from master sheet 
# data = pd.read_excel (r'/Users/sebastianbotha/Documents/Python Projects/wordle_bot/Wordle database.xlsx')

def first_word(data_in):
    # remove words without unique 
    data_in = data_in.drop(data_in.index[data_in['Completley unique '] == 0])
    
    # sort based on selected column
    data_in.sort_values(by=['Full P'], inplace=True, ascending=False)
    
    # Visualize the dataframe
    # print(data_in.head(5))

    # selct top response 
    first_word_data = data_in.iloc[0][0]
    
    return first_word_data

def login():
    driver.get("https://www.nytimes.com/games/wordle/index.html")
    print("Click now\n")
    SmartClick("//HTML/BODY/GAME-APP")
    
def SmartClick(PATH):
    try:
        #print("wait to click")
        wait=WebDriverWait(driver,30)
        wait.until(EC.element_to_be_clickable((By.XPATH, PATH)))
        #print("found so now click")
        driver.find_element(By.XPATH, PATH).click()
        
    except:
        print("couldint find to click ")
# =================== main =================================== 
# get first word to submit
# First_word_print = first_word(data)

login()
# submit first word

# get submission results 


# print(First_word_print)


# print(" old data/main\n")
# print(data.head(20))

exit()
