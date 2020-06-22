import requests
import pandas as pd
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm.notebook import tqdm

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=ko_KR')

base_url='https://movie.naver.com'
current='https://movie.naver.com/movie/running/current.nhn'
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.implicitly_wait(3)

driver.get(current)

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

url_list=soup.select('ul.lst_detail_t1 dt a')

#영화 목록
df_movie=pd.DataFrame(columns=['name','url'])
for i in range(len(url_list)):
    temp=pd.Series([url_list[i].text, base_url+url_list[i].get('href')], index=df_movie.columns)
    df_movie=df_movie.append(temp,ignore_index=True)

#영화 별 리뷰
df_movie_review=pd.DataFrame(columns=['mid','user','rate','review'])
for key in tqdm(range(len(df_movie))):
    try:
        iframe_page='https://movie.naver.com/movie/bi/mi/point.nhn?code='+str(df_movie.iloc[key,1][df_movie.iloc[key,1].find('=')+1:])
        driver.get(iframe_page)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        review_page=base_url+soup.select('iframe.ifr')[0].get('src')
        driver.get(review_page)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        paging=soup.select('div.paging a')
        page_list=[base_url+paging[i].get('href') for i in range(len(paging)-1)]

        #리뷰에 paging 있음, paging 별 리뷰 10개씩 있음
        for _page in page_list:
            driver.get(_page)
            page = driver.page_source
            soup = BeautifulSoup(page, 'html.parser')

            temp_df=pd.DataFrame(columns=['mid','user','rate','review'])
            for i in range(len(soup.select('div.star_score em'))):
                #user, rate 정보
                rate=soup.select('div.star_score em')[i].text
                user=soup.select('div.score_reple dl span')[i].text

                temp_series=pd.Series([key,user,rate,None], index=df_movie_review.columns)
                temp_df=temp_df.append(temp_series, ignore_index=True)

            #review는 복잡해서 따로 가져옴
            span_list=soup.select('div.score_reple p span')
            review_list=[]
            for span in span_list:
                try:
                    if '_filtered' in span.get('id'):
                        review_list.append(span)
                except:
                    pass

            reviews=[]
            for review in review_list:
                try:
                    #긴 리뷰
                    reviews.append(review.a.get('data-src'))
                except:
                    #짧은 리뷰
                    reviews.append(review.text.replace('\n','').replace('\t',''))

            temp_df['review']=reviews
            df_movie_review=df_movie_review.append(temp_df)
    except:
        print(key)
        
df_movie.to_csv('current_movie.csv')
df_movie_review.to_csv('current_movie_review.csv')