import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
import os,sys

def seveFil():
    movie_Dic = model_list
    columns = ["電影","電影","日期","內容","導演","演員","類型","片長"]
    movie_df = pd.DataFrame(movie_Dic , columns=columns)
    movie_df.to_csv("movie2.csv",encoding="utf-8-sig",index = False)

movieList=[]
errorlist=[]

f = open("movies.txt","r") 
lines = f.readlines()   
for line in lines:
    line = line[0:-1]
    movieList.append(line)
f.close()

driver = webdriver.Chrome()
url = 'https://www.google.com.tw/'
# a = 0
model_list=[]
driver.get(url)
movieLink=''
for i in range(0,len(movieList)):
    try:
        search_input = driver.find_element_by_name("q")
        sleep(1)
        search_input.send_keys(movieList[i]+" 威秀"+"\n")
        sleep(3)
        a = 1
        movieLink = driver.find_elements_by_xpath("//div[@id='main']/div[@id='cnt']/div[@class='mw']/div[@id='rcnt']/div[@class='col']/div[@id='center_col']/div[@class='med']/div[2]/div/div/div/div/div['a']/div/div/div[1]/a")

        href = movieLink[0].get_attribute('href')
        driver.get(href)
        sleep(1)
        ch = driver.find_elements_by_xpath("//article[@class='article']/section[@class='movieDetail']/div[@class='movieMain']/section[@class='movieInfo']/div[@class='titleArea']/h1")[0].text
        en = driver.find_elements_by_xpath("//article[@class='article']/section[@class='movieDetail']/div[@class='movieMain']/section[@class='movieInfo']/div[@class='titleArea']/h2")[0].text
        date = driver.find_elements_by_xpath("//article[@class='article']/section[@class='movieDetail']/div[@class='movieMain']/section[@class='movieInfo']/div[@class='titleArea']/time")[0].text
        str =''
        content = driver.find_elements_by_xpath("//div[@class='movieStory']/article[@class='article']/div[@class='bbsArticle']")[0].text
        time = driver.find_elements_by_xpath("//article[@class='article']/section[@class='movieDetail']/div[@class='movieMain']/section[@class='movieInfo']/div[@class='infoArea']/table/tbody/tr[4]/td[2]")[0].text
        director = driver.find_elements_by_xpath("//article[@class='article']/section[@class='movieDetail']/div[@class='movieMain']/section[@class='movieInfo']/div[@class='infoArea']/table/tbody/tr[1]/td[2]")[0].text
        actor = driver.find_elements_by_xpath("//article[@class='article']/section[@class='movieDetail']/div[@class='movieMain']/section[@class='movieInfo']/div[@class='infoArea']/table/tbody/tr[2]/td[2]")[0].text
        type = driver.find_elements_by_xpath("//article[@class='article']/section[@class='movieDetail']/div[@class='movieMain']/section[@class='movieInfo']/div[@class='infoArea']/table/tbody/tr[3]/td[2]")[0].text
    # except ProtocolError:
    #     print('1')
    #     seveFil()
    #     driver.close()
    except Exception as e:
        seveFil()
        print(e)
        print(movieList[i])
        errorlist.append(movieList[i])
        # driver.get(url)
        continue

    # print(type)
    Data = [ch,en,date,str,str,str,str,str]
    # for item in Data:
    #     mw.write(item)
    # mw.write("\n")
    
    model_list.append(Data)
    driver.get('https://www.google.com.tw/')

driver.close()
seveFil()



