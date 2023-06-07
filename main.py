# imports
import pandas as pd
import numpy as np
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

import chromedriver_autoinstaller as chromedriver
chromedriver.install()



# ========================= INIT DRIVER ============================================
options = Options()
options.add_argument('--incognito')
options.add_argument("window-size=720,1400")

# ====== use for mac =======================

# path to chrome driver: MAC

browser = webdriver.Chrome()

ChromDriver_path = '/usr/local/Caskroom/chromedriver/101/chromedriver'
s = Service(ChromDriver_path)
driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(options=options)
driver.get("https://www.nytimes.com/games/wordle/index.html")

# get data from master sheet 
data = pd.read_excel (r'/Users/sebastianbotha/Documents/Python Projects/wordle_bot/Wordle database.xlsx')

def first_word(data_in):
    # remove words without unique 
    data_in = data_in.drop(data_in.index[data_in['Completley unique '] == 0])
    
    # sort based on selected column
    data_in.sort_values(by=['Full P'], inplace=True, ascending=False)
    #data_in.sort_values(by=['Word usage Frequency '], inplace=True, ascending=False)
    
    # Visualize the dataframe
    print(data_in.head(5))

    # selct top response 
    first_word_data = data_in.iloc[0][0]
    
    return first_word_data

def next_word(database):
    # sort based on selected column
    database.sort_values(by=['Word usage Frequency '], inplace=True, ascending=False)

    #database.reset_index(drop=True, inplace=True)
    # selct top response 
    next_word = database.iloc[0][0] 
    print("found and saved top word", next_word, "will now exclude from db")
    database.drop(index=database.index[0], axis=0, inplace=True)
    return next_word
    
def send_letter(letter):
    Close_p ='return document.querySelector("body > div > div > div > div > div.Welcome-module_buttonContainer__K4GEw > button:nth-child(3)")'
    close_b_2 = 'return document.querySelector("body > div > div > dialog > div > button")'
    path_a = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(2)')"
    path_b = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(3) > button:nth-child(6)')"
    path_c = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(3) > button:nth-child(4)')"
    path_d = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(4)')"
    path_e = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(3)')"
    path_f = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(5)')"
    path_g = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(6)')"
    path_h = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(7)')"
    path_i = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(8)')"
    path_j = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(8)')"
    path_k = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(9)')"
    path_l = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(10)')"
    path_m = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(3) > button:nth-child(8)')"
    path_n = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(3) > button:nth-child(7)')"
    path_o = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(9)')"
    path_p = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(10)')"
    path_q = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(1)')"
    path_r = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(4)')"
    path_s = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(2) > button:nth-child(3)')"
    path_t = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(5)')"
    path_u = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(7)')"
    path_v = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(3) > button:nth-child(5)')"
    path_w = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(2)')"
    path_x = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(3) > button:nth-child(3)')"
    path_y = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(1) > button:nth-child(6)')"
    path_z = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(3) > button:nth-child(2)')"
    path_enter = "return document.querySelector('#wordle-app-game > div.Keyboard-module_keyboard__uYuqf > div:nth-child(3) > button:nth-child(1)')"
    letter_path ="return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(1)')"

    if letter == "a":
        letter_path = path_a
    elif letter == "b":
        letter_path = path_b
    elif letter == "c":
        letter_path = path_c
    elif letter == "d":
        letter_path = path_d
    elif letter == "e":
        letter_path = path_e
    elif letter == "f":
        letter_path = path_f
    elif letter == "g":
        letter_path = path_g
    elif letter == "h":
        letter_path = path_h
    elif letter == "i":
        letter_path = path_i
    elif letter == "j":
        letter_path = path_j
    elif letter == "k":
        letter_path = path_k
    elif letter == "l":
        letter_path = path_l
    elif letter == "m":
        letter_path = path_m
    elif letter == "n":
        letter_path = path_n
    elif letter == "o":
        letter_path = path_o
    elif letter == "p":
        letter_path = path_p
    elif letter == "q":
        letter_path = path_q
    elif letter == "r":
        letter_path = path_r
    elif letter == "s":
        letter_path = path_s
    elif letter == "t":
        letter_path = path_t
    elif letter == "u":
        letter_path = path_u
    elif letter == "v":
        letter_path = path_v
    elif letter == "w":
        letter_path = path_w
    elif letter == "x":
        letter_path = path_x
    elif letter == "y":
        letter_path = path_y
    elif letter == "z":
        letter_path = path_z
    elif letter == "1":
        letter_path = Close_p    
    elif letter == "2":
        letter_path = path_enter  
    elif letter == "3":
        letter_path =  close_b_2
    
    button_element = driver.execute_script(letter_path)
    button_element.click()
    
def absent_letter(database, letter):
    # remove all words that contain eval letter 
    column_var =1
    
    while column_var <=5:
        # remove words without unique 
        evalue_column = "Letter {}".format(column_var)
        # print(evalue_column)
        database.drop(database.index[database[evalue_column] == letter], inplace=True)
        # returns an edited database 
        column_var = column_var + 1

def present_letter(database,letter, index):
    # remove all words that dont contain eval letter 
    
    # evalue which word contains the passed letter - True if word has the letter in it
    database['has_letter'] = np.where((database['Letter 1']== letter) | (database['Letter 2'] == letter)| (database['Letter 3'] == letter)| (database['Letter 4'] == letter)| (database['Letter 5'] == letter), True, False)
    
    # remove all rows that dont contain given letter 
    database.drop(database.index[database['has_letter'] == False], inplace=True)
    
    #REMOVE LETTER FROM SPECIIFC ROW FOR PRESENT LETTER (KNOW ITS IN WORD AND KNOW THAT ITS NOT IN THAT POSITION)
    # remove words without unique 
    evalue_column = "Letter {}".format(index)
    # print(evalue_column)
    database.drop(database.index[database[evalue_column] == letter], inplace=True)
   
def correct_letter(database, letter, index):
     # remove all words thatdont have eval letter at current index
    evalue_column = "Letter {}".format(index)
    #print(evalue_column)
    database.drop(database.index[database[evalue_column] != letter], inplace=True)

def remove_word(database):
    # next word to submit is always highest prob one so find highest prob then remove row 1 
    word_var = database.iloc[0][0] 
    print("remove word ", word_var)
    database.drop(index=database.index[0], axis=0, inplace=True)
    word_var = database.iloc[0][0] 
    print("new word top", word_var)
    
    
# =================== main =================================== 
# 1) get first word to submit
guess_counter = 1
submit_word = first_word(data)

# 2) login and ready page for inputs
#time.sleep(1)
# close button mapped to 1 
send_letter("1")

time.sleep(2)

send_letter("3")
time.sleep(2)

score_counter = 0

# 3) itterate options
while guess_counter<=6: 
    print("Guess number:", guess_counter,"of 6 possible guesses\n")
    # submit word
    print("word to submit is:", submit_word, "\n")
    for x in submit_word:
        #print(x)
        send_letter(x)
        time.sleep(2)
    # enter 
    send_letter("2")
  
    time.sleep(5)
    # evaluete options and modify DB 
    block_number = 1
    while block_number <=5:

        #check_path = "return document.querySelector('#wordle-app-game > div.Board-module_boardContainer__cKb-C > div > div:nth-child({}) > div:nth-child({}) > div')".format(guess_counter, block_number)
        check_path = "return document.querySelector('#wordle-app-game > div.Board-module_boardContainer__TBHNL > div > div:nth-child({}) > div:nth-child({}) > div')".format(guess_counter, block_number)
        
        check_ele = driver.execute_script(check_path)
        print_ele = check_ele.get_attribute('outerHTML')
        # print("letter in block is:", print_ele)
        
        # absent = letter not in word 
        # present = letter in word, wrong place 
        # correct = letter in write place
        eval_letter = submit_word[block_number-1]
   
        if "absent" in print_ele:
            # remove all words that contain eval letter 
            print("absent", eval_letter)
            absent_letter(data, eval_letter)
            
        elif "present" in print_ele: 
            # remove all words that dont contain eval letter 
            print("present", eval_letter)
            present_letter(data, eval_letter, block_number)
            
        elif "correct" in print_ele:
            # remove all words thatdont have eval letter at current index 
            print("correct", eval_letter)
            correct_letter(data, eval_letter, block_number)
            score_counter = score_counter + 1
        else:
            print("block empty")
        
       
        block_number = block_number + 1 
    
    # if full word is found 
    if score_counter == 5: 
        print("found the right word in", guess_counter, "tries and the right word is", submit_word)
        # exit loop 
        guess_counter = 7
        
    else: 
        score_counter = 0 
        # sort/index database & get highest probability word  
        submit_word = next_word(data)
        guess_counter = guess_counter +1
        time.sleep(3)

# quit chrome driver 
driver.close()
driver.quit()

exit()
