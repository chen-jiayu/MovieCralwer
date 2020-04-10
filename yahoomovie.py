import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
import os,sys

# import cv2

def seveFil():
    movie_Dic = model_list
    columns = ["電影","電影","類型","上映日期","片長","導演","演員"]
    movie_df = pd.DataFrame(movie_Dic , columns=columns)
    movie_df.to_csv("movie1.csv",encoding="utf-8-sig",index = False)

movieList=[]
errorlist=[]

f = open("movies.txt","r") 
# mw = open("movies.csv","w") 
lines = f.readlines()   
for line in lines:
    line = line[0:-1]
    movieList.append(line)
# print(movieList)

f.close()

chromedriver_path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome()
url = 'https://www.google.com.tw/'
# a = 0
model_list=[]
# movieList=['白頭山：半島浩劫','葉問 4：完結篇','野蠻遊戲：全面晉級','霹靂嬌娃','CATS']
driver.get(url)
movieLink=''
for i in range(0,len(movieList)):
    try:
        search_input = driver.find_element_by_name("q")
        sleep(1)
        search_input.send_keys(movieList[i]+" yahoo介紹"+"\n")
        sleep(3)
        a = 1
        movieLink = driver.find_elements_by_xpath("//div[@id='main']/div[@id='cnt']/div[@class='mw']/div[@id='rcnt']/div[@class='col']/div[@id='center_col']/div[@class='med']/div[2]/div/div/div/div/div['a']/div/div/div[1]/a")
        # while (a!=0):
        #     print(a) 
        #     movieh3 = driver.find_elements_by_xpath("//div[@id='main']/div[@id='cnt']/div[@class='mw']/div[@id='rcnt']/div[@class='col']/div[@id='center_col']/div[@class='med']/div[2]/div/div/div/div/div['a']/div/div/div[1]/a/h3")[0].text
        #     movieh3 = movieh3[-9:]
        #     print(movieh3)
        #     if movieh3 != 'Yahoo奇摩電影' :
        #         a = a+1
        #     if movieh3 == 'Yahoo奇摩電影' :
        #         movieLink = driver.find_elements_by_xpath("//div[@id='main']/div[@id='cnt']/div[@class='mw']/div[@id='rcnt']/div[@class='col']/div[@id='center_col']/div[@class='med']/div[2]/div/div/div/div/div['a']/div/div/div[1]/a")
        #         a = 0
        #     if a==5:
        #         break

        href = movieLink[0].get_attribute('href')
        driver.get(href)
        sleep(1)
        ch = driver.find_elements_by_xpath("//div[@id='maincontainer']/main/div[@class='maincontent ga_movie_intro']/div[@id='container']/div[@id='content_l']/div[@class='l_box _c']/div[@class='l_box_inner']/div[@class='movie_intro_info _c']/div[@class='table']/div[@class='movie_intro_info_r']/h1")[0].text
        en = driver.find_elements_by_xpath("//div[@id='maincontainer']/main/div[@class='maincontent ga_movie_intro']/div[@id='container']/div[@id='content_l']/div[@class='l_box _c']/div[@class='l_box_inner']/div[@class='movie_intro_info _c']/div[@class='table']/div[@class='movie_intro_info_r']/h3")[0].text
        date = driver.find_elements_by_xpath("//div[@id='maincontainer']/main/div[@class='maincontent ga_movie_intro']/div[@id='container']/div[@id='content_l']/div[@class='l_box _c']/div[@class='l_box_inner']/div[@class='movie_intro_info _c']/div[@class='table']/div[@class='movie_intro_info_r']/span[1]")[0].text
        time = driver.find_elements_by_xpath("//div[@id='maincontainer']/main/div[@class='maincontent ga_movie_intro']/div[@id='container']/div[@id='content_l']/div[@class='l_box _c']/div[@class='l_box_inner']/div[@class='movie_intro_info _c']/div[@class='table']/div[@class='movie_intro_info_r']/span[2]")[0].text
        director = driver.find_elements_by_xpath("//div[@id='maincontainer']/main/div[@class='maincontent ga_movie_intro']/div[@id='container']/div[@id='content_l']/div[@class='l_box _c']/div[@class='l_box_inner']/div[@class='movie_intro_info _c']/div[@class='table']/div[@class='movie_intro_info_r']/div[@class='movie_intro_list']")[0].text
        actor = driver.find_elements_by_xpath("//div[@id='maincontainer']/main/div[@class='maincontent ga_movie_intro']/div[@id='container']/div[@id='content_l']/div[@class='l_box _c']/div[@class='l_box_inner']/div[@class='movie_intro_info _c']/div[@class='table']/div[@class='movie_intro_info_r']/div[@class='movie_intro_list']")[1].text
        type = driver.find_elements_by_xpath("//div[@id='maincontainer']/main/div[@class='maincontent ga_movie_intro']/div[@id='container']/div[@id='content_l']/div[@class='l_box _c']/div[@class='l_box_inner']/div[@class='movie_intro_info _c']/div[@class='table']/div[@class='movie_intro_info_r']/div[@class='level_name_box']")[0].text
    # except ProtocolError:
    #     print('1')
    #     seveFil()
    #     driver.close()
    except Exception as e:
        seveFil()
        print(e)
        print(movieList[i])
        errorlist.append(movieList[i])
        driver.get(url)
        continue

    # print(type)
    Data = [ch,en,type,date,time,director,actor]
    # for item in Data:
    #     mw.write(item)
    # mw.write("\n")
    
    model_list.append(Data)
    driver.get('https://www.google.com.tw/')

driver.close()
seveFil()



