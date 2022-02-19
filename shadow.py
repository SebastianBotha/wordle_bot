# imports
from tokenize import String
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


# Key Paths 

def send_letter(letter):
    Close_p = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-modal').shadowRoot.querySelector('div > div > div > game-icon').shadowRoot.querySelector('svg')"
    path_a = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(2)')"
    path_b = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(6)')"
    path_c = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(4)')"
    path_d = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(4)')"
    path_e = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(3)')"
    path_f = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(5)')"
    path_g = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(6)')"
    path_h = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(7)')"
    path_i = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(8)')"
    path_j = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(8)')"
    path_k = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(9)')"
    path_l = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(10)')"
    path_m = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(8)')"
    path_n = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(7)')"
    path_o = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(9)')"
    path_p = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(10)')"
    path_q = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(1)')"
    path_r = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(4)')"
    path_s = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(2) > button:nth-child(3)')"
    path_t = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(5)')"
    path_u = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(7)')"
    path_v = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(5)')"
    path_w = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(2)')"
    path_x = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(3)')"
    path_y = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(1) > button:nth-child(6)')"
    path_z = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(2)')"
    path_enter = "return document.querySelector('body > game-app').shadowRoot.querySelector('#game > game-keyboard').shadowRoot.querySelector('#keyboard > div:nth-child(3) > button:nth-child(1)')"
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
    
    button_element = driver.execute_script(letter_path)
    button_element.click()
    
options = Options()
options.add_argument('--incognito')
options.add_argument("window-size=720,1400")

ChromDriver_path = '/usr/local/Caskroom/chromedriver/97.0.4692.71/chromedriver'
s = Service(ChromDriver_path)
driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(options=options)


driver.get("https://www.nytimes.com/games/wordle/index.html")

time.sleep(2)

# close button mapped to 1 
send_letter("1")

time.sleep(2)
send_letter("h")
send_letter("i")
send_letter("v")
send_letter("e")
send_letter("s")
send_letter("2")

time.sleep(5)

