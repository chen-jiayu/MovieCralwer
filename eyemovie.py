import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from time import sleep
import time
import os,sys

def seveFil():
    movie_Dic = model_list
    columns = ["電影","片長","上映日期","IMDb 分數","IMDb 評分人數","類型","電影劇情","影片年份","出品國","出品","發行商","語言","導演","編劇","演員"]
    movie_df = pd.DataFrame(movie_Dic , columns=columns)
    movie_df.to_csv("movie2.csv",encoding="utf-8-sig",index = False)

def savelink():
    movie_Dic = link_list
    columns = ["1","2"]
    movie_df = pd.DataFrame(movie_Dic , columns=columns)
    movie_df.to_csv("link1.csv",encoding="utf-8-sig",index = False)

def change(number):
    alist = []
    if number >= 11:
        alist = [4,5,6,7,8]
    if number == 10:
        alist = [3,4,5,6,7]
    if number == 9:
        alist = [2,3,4,5,6]
    return alist

# def judge(number):
#     if number<=0
#         return ' '
#     else
        
movieList=[]
errorlist=[]

f = open("error.txt","r") 
# mw = open("link.txt","w") 
lines = f.readlines()   
for line in lines:
    # line = line[0:-1]
    movieList.append(line)
# print(movieList)

f.close()

driver = webdriver.Chrome()
url = 'http://www.atmovies.com.tw/home/movie/'
# a = 0
model_list=[]
link_list=[]
driver.get(url)
movieLink=''
for i in range(0,len(movieList)):
    print(i)
    try:
        # driver.find_element_by_name("search_term").clear()
        # search_input = driver.find_element_by_name("search_term")
        # sleep(1)
        # search_input.send_keys(movieList[i]+"\n")
        # sleep(1)
        # a = 1
        # movieLink = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[2]/div[@class='12u']/section[@class='box blog']/div/div/div[@class='9u 12u(mobile)']/div[@class='content content-left']/blockquote/header/a")
        # if len(movieLink)<=0:
        #     movieLink = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[2]/div[@class='12u']/section[@class='box blog']/div/div/div[@class='9u 12u(mobile)']/div[@class='content content-left']/blockquote/ol/li/a")

        # coount = 0
        # # href =''
        # href = movieLink[0].get_attribute('href')
        # while(len(movieLink) <= 0) :
        #     movieLink = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[2]/div[@class='12u']/section[@class='box blog']/div/div/div[@class='9u 12u(mobile)']/div[@class='content content-left']/blockquote/ol/li/a")
        #     if coount == 5:
        #         break
        #     coount = coount+1
        # sleep(1)
        # href = movieLink[0].get_attribute('href')
        # path =href.split("/")[-2]
        # print(href)
        # path1 = 'http://app2.atmovies.com.tw/film/cast/'+path+'/'
        # data = [href,path1]
        # link_list.append(data)
        href = movieList[i]
        path =href.split("/")[-2]
        path1 = 'http://app2.atmovies.com.tw/film/cast/'+path+'/'
        driver.get(movieList[i])
        name=''
        time=''
        date=''
        content =''
        date =' '
        IMDB =''
        name = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/cfprocessingdirective[@pageencoding='utf-8']/div[@class='filmTitle']")
        if len(name)<=0:
            name = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/div[@class='filmTitle']")[0].text
            time = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/div[@id='filmTagBlock']/span[2]/ul[@class='runtime']/li[1]")[0].text
            date1 = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/div[@id='filmTagBlock']/span[2]/ul[@class='runtime']/li[2]")[0].text
            # if len(date1)<=0:
            #     date =' '
            # else:
            #     date = date1[0].text
            content = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/div[@style='width:90%;font-size: 1.1em;']")[0].text
            sleep(0.5)
            all = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/div[@id='filmCastDataBlock']/ul[2]/li")
            allist = change(len(all))
            IMDb = driver.find_elements_by_xpath("//li/a[contains(text(),'IMDb')]")
            if len(IMDb)>0:
                IMDB = IMDb[0].get_attribute('href')
            IMDB = IMDb[0].get_attribute('href')
            year = all[allist[0]].text
            country = all[allist[1]].text
            company = all[allist[2]].text
            publish = all[allist[3]].text
            language = all[allist[4]].text
            # driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/div[@id='filmCastDataBlock']/ul[2]/li['an5']")[0].text
        else:
            name = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/cfprocessingdirective[@pageencoding='utf-8']/div[@class='filmTitle']")[0].text
            time = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/cfprocessingdirective[@pageencoding='utf-8']/div[@id='filmTagBlock']/span[2]/ul[@class='runtime']/li[1]")[0].text
            date1 = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/cfprocessingdirective[@pageencoding='utf-8']/div[@id='filmTagBlock']/span[2]/ul[@class='runtime']/li[2]")[0].text
            # if len(date1)<=0:
            #     date =' '
            # else:
            #     date = date1[0].text            
            content = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/cfprocessingdirective[@pageencoding='utf-8']/div[@style='width:90%;font-size: 1.1em;']")[0].text
            sleep(0.5)
            all = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/cfprocessingdirective[@pageencoding='utf-8']/div[@id='filmCastDataBlock']/ul[2]/li")
            allist = change(len(all))
            IMDb = driver.find_elements_by_xpath("//li/a[contains(text(),'IMDb')]")
            if len(IMDb)>0:
                IMDB = IMDb[0].get_attribute('href')
            year = all[allist[0]].text
            country = all[allist[1]].text
            company = all[allist[2]].text
            publish = all[allist[3]].text
            language = all[allist[4]].text
        # hhref = 'http://app2.atmovies.com.tw/film/cast/'
        # sleep(2)
        # i = i+1
        # print(i)
        sleep(1)
        driver.get(path1)
        director = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/ul/ul[1]")
        writer = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/ul/ul[2]")
        actor = driver.find_elements_by_xpath("//div[@id='page-wrapper']/div[@id='main-wrapper']/div[@id='main']/div[@class='row']/div[1]/div[@class='content content-left']/ul/ul[3]/li/a")
        actor1=''
        director1=''
        writer1=''
        if len(director)>0:
            for each in director:
                director1 = director1 + (each.text + ',')
        if len(writer)>0:
            for each in writer:
                writer1 = writer1 + (each.text + ',')
        if len(actor)>0:
            for each in actor:
                actor1 = actor1 + (each.text + ',')
        data=[name,time,date1,content,year,country,company,publish,language,director,writer,actor1]
        model_list.append(data)

        score  =''
        number =''
        type1 = ''
        sleep(2)
        if len(IMDB)>0:
            driver.get(IMDB)
            score = driver.find_elements_by_xpath("//span[contains(@itemprop , 'ratingValue')]")[0].text
            number = driver.find_elements_by_xpath("//span[contains(@itemprop , 'ratingCount')]")[0].text
            type = driver.find_elements_by_xpath("//div[contains(@class , 'subtext')]/a")
            for each in type:
                if ' ' not in each.text:
                    type1 = type1 + (each.text + ' ')
            print(type1)
        data=[name,time,date,score,number,type1,content,year,country,company,publish,language,director1,writer1,actor1]
        model_list.append(data)


    except Exception as e:
        # seveFil()
        print(e)
        print(movieList[i])
        # errorlist.append(movieList[i])
        # driver.get('http://www.atmovies.com.tw/home/movie/')
        continue
    
    sleep(1)
    # driver.get('http://www.atmovies.com.tw/home/movie/')
seveFil()

driver.close()
seveFil()



