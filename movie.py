import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time

chromedriver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome()
url = 'https://movies.yahoo.com.tw/'
a = 0
driver.get(url)
search_input = driver.find_element_by_name("p")
search_input.send_keys("冰雪奇緣")
start_search_btn = driver.find_elements_by_xpath("//div[@id='maincontainer']/header/div[@id='kv']/div[@class='content']/div[@id='y_hous_serch']/div[@id='y_serch_l']/form[@method='get']/button[@class='serch_movie gabtn']")
sleep(2)
start_search_btn[0].click()
sleep(3)

list=[]

def test():
    global a  
    search_input = driver.find_element_by_name("p")
    search_input.clear()
    search_input.send_keys("冰雪奇緣")
    start_search_btn = driver.find_elements_by_xpath("//div[@id='maincontainer']/header/div[@id='kv']/div[@class='content']/div[@id='y_hous_serch']/div[@id='y_serch_l']/form[@method='get']/button[@class='serch_movie gabtn']")
    sleep(2)
    start_search_btn[0].click()
    sleep(3)
    movieLink = driver.find_elements_by_xpath("//div[@id='maincontainer']/main/div[@class='maincontent ga_search']/div[@id='container']/div[@id='content_l']/div[@class='release_box']/div[@class='searchpage']/ul[@class='release_list mlist']/li[1]/div[@class='release_foto']/a")
    href = movieLink[0].get_attribute('href')
    list.append(href)
    a = a+1
    # driver.get(href)

while(a!=5):
    # try:
    test()
    # except Exception as e:
    #     print(e)
    #     break

driver.close()

print(list)

