# 데이트 마이닝: 빅데이터 기반 서울 데이트 코스 추천 알고리즘
<div align="center">
<img width="767" alt="Flowchart" src="https://user-images.githubusercontent.com/44253680/85925687-0d5d8900-b8d5-11ea-9e1c-4f13dbf9282f.png">
</div>  

## Introduction <a id="introduction"></a>
#### Needs  <a id="needs"></a> 

#### Goals <a id="goals"></a>
- 정성적 목표   
&nbsp;&nbsp;&nbsp;&nbsp;이 프로젝트의 최종 결과물은 데이트 취향과 위치를 고려한 데이트 코스 추천 알고리즘이며 데이트 코스에는 사용자의 취향에 맞춘 맛집/카페, 데이트 명소(유명 방문지, 보드게임 카페, 볼링장, 방탈출 카페 등등), 영화가 포함되어 있다. 또한 데이트를 하고자 하는 지역구를 선택한다면, 이에 대한 코스 필터링 기능을 제공하는 것 또한 최종 결과물에 포함되도록 한다. 기존의 목표는 웹앱 제작까지 포함이였으나, 시간상의 관계로 구글 폼으로 대체하여 유저로 하여금 웹앱에서 데이트 코스 추천을 처음 받을때의 경험을 똑같이 할 수 있도록 문항들을 구성하도록 한다.
- 정량적 목표   
&nbsp;&nbsp;&nbsp;&nbsp;정형화된 데이터 셋이 아닌 점과 선행 연구에 대한 오픈소스 프로젝트가 없는 관계로, 선행 연구와 비교한 정량적 목표 설정은 무리가 있다는 점을 인지하였다. 따라서 표본을 모집 후 만족도를 조사하여 MOS 기법을 바탕으로 만족도를 조사하는 것을 대체 방안으로 채택하였다. 테스터들은 구글 설문지를 통해 요구되는 몇가지 문항들에 답변한 이후, 메일로 알고리즘이 추천한 데이트 코스 결과를 받고 이후 다시 메일에 첨부된 만족도 조사에 답하게 된다.  만족도 조사는 알고리즘이 추천한 코스에 대한 만족도를 묻는 총 1 문항으로, 1점 매우 불만족한다 부터 시작하여 5점은 매우 만족한다까지로 척도를 제시해 30명 내외의 표본을 대상으로 실시하였다. 이를 통해 최종적으로 평점 3.79점(5점 만점)을 받았다.


## Table of contents
  1. [Introduction](#introduction)
     * [Needs](#needs)
     * [Goals](#goals)
  2. [Data crawling](#data_crawling)
     * [EAT](#data_crawling_eat)
     * [GO](#data_crawling_go)
     * [WATCH](#data_crawling_watch)
  3. [Data preprocessing](#data_preprocessing)
     * [Review translation](#review_translation)
     * [Review tokenizing](#review_tokenizing)
  4. [Review clustering](#review_clustering)
  5. [Modeling](#modeling)
     * [Contents Based Filtering](#cbf)
     * [Neural Collaborative Filtering](#ncf)
  6. [Result](#result)
  7. [Conclusion](#conclusion)
  
## Data crawling
#### Eat
#### Go
#### Watch

## Data preprocessing
#### Review translation
#### Review tokenizing

## Review clustering

## Modeling
#### Contents Based Filtering
#### Neural Collaborative Filtering

## Results
* Main code, table, graph, comparison, ...
* Web link

``` C++
void Example(int x, int y) {
   ...  
   ... // comment
   ...
}
```

## Conclusion
* Summary, contribution, ...


## Project Schedule
| Contents | March | April |  May  | June  |
|----------|-------|-------|-------|-------|
|  1. 데이터 수집  |       | :heavy_check_mark:      |       |       |
|  2. 데이터 형식 통합  |       |   :heavy_check_mark:    |       |       |
|  3. 리뷰 데이터 자연어 처리  |       |       |   :heavy_check_mark:    |       |
|  4. 장소별 형용사 데이터 셋 생성  |       |       |  :heavy_check_mark:     |       |
|  5. 유저별 형용사 데이터 셋 생성  |       |       |  :heavy_check_mark:     |       |
|  6. Contents Based Filtering(User, Item based)  |       |       |   :heavy_check_mark:    |       |
|  7. Neural Collaborative Filtering  |       |       |    :heavy_check_mark:   |       |
|  8. 1차 최종 알고리즘 모델링  |       |       |  :heavy_check_mark:     |       |
|  9. 최종 알고리즘 모델링  |       |       |       |   :heavy_check_mark:    |
|  10. 테스트용 구글 폼 제작  |       |       |       |  :heavy_check_mark:     |
|  11. 표본을 대상으로 만족도 조사 시행  |       |       |       |  :heavy_check_mark:     |

## Packages
* [tensorflow(1.15.2)](https://github.com/tensorflow/docs/tree/r1.5/site/en/api_docs)
* [scikit-learn(0.22.1)](https://pypi.org/project/scikit-learn/0.22.1/)
* [cornac(1.6.1)](https://pypi.org/project/cornac/)
* [pypapago](https://github.com/Beomi/pypapago)
* [nltk(3.4.5)](https://pypi.org/project/nltk/3.4.5/)
* [gensim(3.8.3)](https://pypi.org/project/gensim/3.8.3/)
* [pandas (1.0.1)](https://pypi.org/project/pandas/1.0.1/)
* [beautifulsoup(4.8.2)](https://pypi.org/project/beautifulsoup4/4.8.2/)
* [selenium(3.141.0)](https://pypi.org/project/selenium/3.141.0/)
* [numpy(1.18.1)](https://pypi.org/project/numpy/1.18.1/)



## Reports
* Upload or link (e.g. Google Drive files with share setting)
* Midterm: [Report](Reports/Midterm.pdf)
* Final: [Report](Reports/Final.pdf), [Demo video](Reports/Demo.mp4)

### Contributors

* [김동혁 (경희대학교 산업경영공학과)](https://github.com/LoveDH)
* [류연주 (경희대학교 관광학과)](https://github.com/YeonjuRyu)
* [유정수 (경희대학교 산업경영공학과)](https://github.com/youjeongsue)

