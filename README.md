# 데이트 마이닝: 빅데이터 기반 서울 데이트 코스 추천 알고리즘
<div align="center">
<img width="767" alt="Flowchart" src="https://user-images.githubusercontent.com/44253680/85925687-0d5d8900-b8d5-11ea-9e1c-4f13dbf9282f.png">
</div>  

## Introduction <a id="introduction"></a>
### Needs  <a id="needs"></a> 
&nbsp;&nbsp;&nbsp;&nbsp;빅데이터 기반의 추천 시스템은 오래 전부터 연구되어왔고, 유튜브, 넷플릭스, 왓챠 등 미디어 플랫폼과 인터넷 쇼핑몰에서 좋은 성능을 발휘했으나, 현재 시장에 출시된 데이트 명소를 추천해주는 애플리케이션은 수요가 높음에도 불구하고 빅데이터 기반의 추천 알고리즘을 사용하지 않고 있음을 발견했다. 따라서 본 프로젝트에서는 **머신러닝을 통해 사용자의 취향을 분석**하고 이를 통해 **데이트 코스를 추천해주는 알고리즘을 개발**한다. 이 알고리즘은 **데이트 코스를 결정하는 데에 어려움을 겪었던 커플들에게 도움**을 줄 것이며, **랜덤 데이트 코스라는 재미 요소**도 줄 수 있을 것이다.

### Goals <a id="goals"></a>
- 정성적 목표   
이 프로젝트의 **최종 결과물은 데이트 취향과 위치를 고려한 데이트 코스 추천 알고리즘**이며 데이트 코스에는 사용자의 취향에 맞춘 맛집/카페, 데이트 명소(유명 방문지, 보드게임 카페, 볼링장, 방탈출 카페 등등), 영화가 포함되어 있다. 또한 데이트를 하고자 하는 지역구를 선택한다면, 이에 대한 **코스 필터링 기능을 제공**하는 것 또한 최종 결과물에 포함되도록 한다.

- 정량적 목표   
정형화된 데이터 셋이 아닌 점과 선행 연구에 대한 오픈소스 프로젝트가 없는 관계로, 선행 연구와 비교한 정량적 목표 설정은 무리가 있다는 점을 인지하였다. 따라서 표본을 모집 후 만족도를 조사하여 **MOS 기법을 바탕으로 만족도를 조사**하는 것을 대체 방안으로 채택하였다. 테스터들은 구글 설문지를 통해 몇가지 문항들에 답변한 후, 메일로 알고리즘이 추천한 데이트 코스 결과를 받고 이후 다시 메일에 첨부된 만족도 조사에 답하게 된다. 만족도 조사는 알고리즘이 추천한 코스에 대한 만족도를 묻는 총 1개의 문항으로, 1점 '매우 불만족한다' 부터 시작하여 5점 '매우 만족한다까지'로 구분하여 응답을 받는다.

## Packages
본 프로젝트에서는 다음과 같은 패키지를 활용하였다.
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

## Table of contents
  1. [Introduction](#introduction)
     * [Needs](#needs)
     * [Goals](#goals)
  2. [Data crawling](#data_crawling)
     * [EAT](#data_crawling_eat)
     * [GO](#data_crawling_go)
     * [WATCH](#data_crawling_watch)
  3. [Data preprocessing](#data_preprocessing)
  4. [Review clustering](#review_clustering)
  5. [Modeling](#modeling)
     * [Contents Based Filtering](#cbf)
     * [Neural Collaborative Filtering](#ncf)
     * [Hybird Method](#hybrid_method)
  6. [Results](#results)
  7. [Conclusion](#conclusion)
  
## Data crawling <a id="data_crawling"></a>
데이터 크롤링은 각각 맛집/카페(이하 EAT), 데이트 명소(이하 GO), 영화(이하 WATCH)로 구분하여 카테고리별로 진행하였으며 각 카테고리별로 크롤링을 위해 이용한 플랫폼은 아래와 같다.
### Eat <a id="data_crawling_eat"></a>
<div align="center">
<img width="30%" alt="mango_plate" src="https://user-images.githubusercontent.com/44253680/85938695-82b77100-b94a-11ea-9aec-401525f01dd8.png">
<img width="31.5%" alt="dining_code" src="https://user-images.githubusercontent.com/44253680/85938715-a67ab700-b94a-11ea-9b5c-6cb9ced5d8c3.png">
</div>  

- 망고 플레이트 (장소 및 리뷰 데이터)
- 다이닝 코드  (장소 및 리뷰 데이터)


### Go <a id="data_crawling_go"></a>
<div align="center">
<img width="30%" alt="korea_tour" src="https://user-images.githubusercontent.com/44253680/85938558-56e7bb80-b949-11ea-871a-1b4869dad067.png">
<img width="32%" alt="trip_advisor" src="https://user-images.githubusercontent.com/44253680/85938510-03756d80-b949-11ea-99b5-d0bbc32711bf.png">
<img width="30%" alt="kakao_map" src="https://user-images.githubusercontent.com/44253680/85938531-230c9600-b949-11ea-82ee-b8b27d4bfffb.png">
</div>  

- 대한민국 구석구석 (장소 정보 데이터)
- TripAdvisor (대한민국 구석구석에서 수집한 장소에 대한 리뷰 데이터)
- 카카오맵 (장소 및 리뷰 데이터)

### Watch <a id="data_crawling_watch"></a>
<div align="center">
<img width="30%" alt="watcha_play" src="https://user-images.githubusercontent.com/44253680/85938601-ceb5e600-b949-11ea-9fde-3a2b65c38dd5.png">
<img width="34%" alt="naver_movie" src="https://user-images.githubusercontent.com/44253680/85938631-0886ec80-b94a-11ea-83d2-b7a688086cd3.png">
</div>  

- 왓챠 플레이 
- 네이버 영화


## Data preprocessing <a id="data_preprocessing"></a>
- **Review translation** <a id="review_translation"></a>   
기존에 수집한 한글 리뷰 데이터는 불용어처리에 시간이 많이 소요되고 또한 한글의 특수성으로 인해 형용사/느낌만을 추출하는데에 어려움을 느꼈고 결과적으로 클러스터링의 성능도 저하됨을한계점으로 파악하였다. 따라서 수집한 한글 리뷰 데이터를 pypapago 라이브러리를 사용해 영어로 변환하는 작업을 수행했다.

- **Review tokenizing** <a id="review_tokenizing"></a>   
NLTK 라이브러리를 사용하여 리뷰 문장에서 형용사들을 추출하고 불용어를 제거하는 작업을 수행한다. 이때 tokenizing한 리뷰 내의 형용사들은 이후 review clustering 단계에 인풋으로 사용된다.

## Review clustering <a id="review_clustering"></a>
Word2Vec을 사용하여 앞선 tokenizing 단계에서 추출해낸 형용사를 300차원의 벡터로 변형한 후, K-means 알고리즘을 사용해 클러스터링 작업을 수행했다. 각 카테고리별 클러스터링 결과는 아래의 링크에서 볼 수 있다.
- [EAT review word cluster](source/Eat/data/eat_cluster.csv)
- [GO review word cluster](source/Go/data/Go_adj_clustered.csv)
- [WATCH review word cluster](source/Watch/data/adj_cluster.csv)

## Modeling <a id="modeling"></a>


### Contents Based Filtering <a id="cbf"></a>

<div align="center">
<figure>
<img width="40%" alt="user_matrix" src="https://user-images.githubusercontent.com/44253680/85939334-6ff36b00-b94f-11ea-8563-4659d3bb8f1f.png"/>   
  <figcaption>user matrix example</figcaption>
<figure>
<img width="40%" alt="item_matrix" src="https://user-images.githubusercontent.com/44253680/85939365-c5c81300-b94f-11ea-8e37-0f6ca81a8a37.png">
  <figcaption>item matrix example</figcaption>
<figure>
  </div>

- **모델 설명**   
위에서 생성한 matrix를 통해 각 user row와 각 item row를 vector로 보고 두 vector의 유사도를 구하는 방식으로 CBF score를 도출했다. 여기서 vector size는 각 분야별 word cluster의 개수 이다. 유사도를 구하는 방법으로는 가장 많이 쓰이는 cosine similarity를 이용했다. 각 카테고리별 User, Item Matrix는 아래 링크된 파일을 통해 볼 수 있다.
   * EAT:  [User Matrix](source/Eat/data/normalized_user_matrix.csv) / [Item Matrix](source/Eat/data/normalized_item_matrix.csv) 
   * GO:  [User Matrix](source/Go/data/normalized_user_matrix.csv) / [Item Matrix](source/Go/data/normalized_item_matrix.csv)   
   * WATCH:  [User Matrix](source/Watch/data/normalized_user_matrix.csv) / [Item Matrix](source/Watch/data/normalized_item_matrix.csv) 

### Neural Collaborative Filtering <a id="ncf"></a>


<div align="center">
<img width="400" alt="NCF_flowchart" src="https://user-images.githubusercontent.com/44253680/85937582-cd7fbb80-b93f-11ea-8baf-52ad96c0244e.png">
</div>


- **모델 설명**   
NCF는 기존의 collaborative filtering 기법과는 달리 DNN 적용을 통해 implicit feedback을 사용하기 위함으로, 크게 ‘GMF(Generalized Matrix Factorization)’과 ‘MLP(Multi-Layer Perceptron)’파트로 나뉘어져 있다.    
본 프로젝트에서는 PreferredAI에서 개발한 corncac 패키지를 이용해 NCF 모델을 구현하였다. 모델에 들어가는 input은 [(userID, ItemID, rating), …]과 같이 유저가 각 아이템에 남긴 평점이 튜플형으로 묶여있는 값들이 들어간 리스트이며, output으로는 유저가 경험하지 않은 다른 아이템들에 대해서 추후에 해당 아이템을 소비할 가능성을 0부터 1사이의 수로 예측한 값이다.

- **FineTuning**   
<html lang="ko">
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <table>
        <tr>
          <th width="10%"></th>
          <th width="10%">batch size</th>
          <th width="10%">learning rate</th>
          <th width="10%">number of epochs</th>
          <th width="10%">number of factors</th>
        </tr>
        <tr>
          <th>EAT</th>
          <td align="center">512</td>
          <td align="center">0.0057864483</td>
          <td align="center">50</td>
          <td align="center">8</td>
        </tr>
        <tr>
          <th>GO</th>
          <td align="center">512</td>
          <td align="center">0.0022595564</td>
          <td align="center">50</td>
          <td align="center">4</td>
        </tr>
        <tr>
          <th>WATCH</th>
          <td align="center">128</td>
          <td align="center">0.0075019904</td>
          <td align="center">100</td>
          <td align="center">8</td>
        </tr>
    </table>
  </body>
</html>

NCF모델의 hyper parameter는 Random Search를 이용해 구했고, **early stopping기법 patience값을 5**로 주어 분야별 최적 파라미터를 위의 표와 같이 구하게 되었다.  
- **최종 모델 성능**   
<html lang="ko">
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <table>
        <tr>
          <th width="10%"></th>
          <th width="10%">F1@10</th>
          <th width="10%">NDCG@10</th>
          <th width="10%">Precision@10</th>
          <th width="10%">Recall@10</th>
          <th width="10%">Train(s)</th>
          <th width="10%">Test(s)</th>
        </tr>
        <tr>
          <th>EAT</th>
          <td align="center">0.0149</td>
          <td align="center">0.0313</td>
          <td align="center">0.0097</td>
          <td align="center">0.0540</td>
          <td align="center">14024.7585</td>
          <td align="center">11.2788</td>
        </tr>
        <tr>
          <th>GO</th>
          <td align="center">0.0970</td>
          <td align="center">0.2482</td>
          <td align="center">0.0556</td>
          <td align="center">0.4532</td>
          <td align="center">3795.3764</td>
          <td align="center">2.3491</td>
        </tr>
        <tr>
          <th>WATCH</th>
          <td align="center">0.0150</td>
          <td align="center">0.0283</td>
          <td align="center">0.0098</td>
          <td align="center">0.0535</td>
          <td align="center">4831.9023</td>
          <td align="center">1.0951</td>
        </tr>
    </table>
  </body>
</html>

**참고한 논문에**서는 NDCG@10가 평균적으로 약 0.43 정도였으며 **마이크로소프트가 NCF 논문을 재구성한 라이브러리 예시로 제시한 결과 값**에서는 NDCG@10가 0.198938였다는 점을 고려했을때 **GO**의 경우 논문보다는 낮고 라이브러리 예시보다는 높은 점수를, **EAT과 WATCH**는 전체적으로 모델 자체의 성능이 낮았다는 아쉬움이 남는다. 위와 같은 결과에 대한 원인으로 EAT과 WATCH에서는 **리뷰의 갯수가 적은 유저가 많기 때문인 것으로 예상**하였다. 이와 같은 한계점은 직접 플랫폼을 운영하는 서비스가 구축되어 데이터 문제가 해결된다면, 어느정도 극복할 수 있을 것이라 예상된다.

### Hybird Method <a id="hybird_method"></a>
<div align="center">
<img width="727" alt="hybrid" src="https://user-images.githubusercontent.com/44253680/85939510-18ee9580-b951-11ea-8712-e11b20ded490.png">
</div>
CBF 모델과 NCF 모델의 결과값을 결합하는 방식으로 최종 prediction score를 도출한다. 이때 최종 score는 두 모델의 score를 단순 곱하는 식으로 사용했다.   
이때 결합 방식을 산술평균, 조화평균으로도 생각해보았지만 이는 다른 한 모델이 낮게 예측한 item을 추천해주는 상황을 야기했다. 따라서 단순 곱을 통해 두 모델이 모두 높은 점수를 낸 item을 추천하도록 했다.



## Results <a id="resultes"></a>
<div align="center">
<img width="400" alt="Result" src="https://user-images.githubusercontent.com/44253680/85938055-78927400-b944-11ea-9fa5-3b33a4b7b449.png">
</div>

최종적으로는 UserID를 인풋으로 입력하면 추천할만한 데이트 코스를 두가지 추천해주는 것으로 알고리즘이 종료된다.   

- code   

``` python
def main():
    u_id = input('Enter User ID: ')
    go = Go_recommendation(u_id)
    eat = Eat_recommendation(u_id)
    watch = Watch_recommendation(u_id)
    result = Search_Recommendable_Places(eat, go, u_id)
    if len(result) == 2:
        eat_result = result[0]
        go_result = result[1]
        print(f'{u_id}님께 추천드릴 맛집은 {eat_result["district"]}에 위치한 {eat_result["name"]}입니다.')
        print(f'{u_id}님께 추천드릴 데이트 장소는 {go_result["district"]}에 위치한 {go_result["p_name"]}입니다.')

    elif len(result) == 4:
        eat_result1 = result[0]
        go_result1 = result[1]
        eat_result2 = result[2]
        go_result2 = result[3]
        print(f'{u_id}님! {eat_result1["district"]}에서의 데이트를 계획하고 계신가요?')
        print(f'{u_id}님께 추천드릴 맛집은 {eat_result1["district"]}에 위치한 {eat_result1["name"]}입니다.')
        print(f'{u_id}님께 추천드릴 데이트 장소는 {go_result1["district"]}에 위치한 {go_result1["p_name"]}입니다.')
        print(f'혹시나! {eat_result2["district"]}에서의 데이트를 계획하고 계신다면?')
        print(f'맛집으로는 {eat_result2["district"]}에 위치한 {eat_result2["name"]}와 ')
        print(f'데이트 장소로는 {go_result2["district"]}에 위치한 {go_result2["p_name"]}을(를) 추천드려요.')
        
    print(f'영화가 끌리는 데이트라면 현재 상영중인 영화 {watch}은(는) 어떠신가요?')
```


## Conclusion <a id="conclusion"></a>
&nbsp;&nbsp;&nbsp;&nbsp;이번 프로젝트에서는 서울 내의 맛집/카페, 데이트 명소, 영화를 모두 포함한 데이트 코스 추천 알고리즘을 기획하고 개발하였다. 단일 장소에 대한 추천을 넘어 각 장소들을 조합하여(필터링 등) 데이트 코스로 추천해주었다는 점에 의의가 있으며 위와 같은 결과를 도출하기 위해 어떤 추천 알고리즘을 사용해야 이 주제에서 가장 적합한 추천을 할 수 있을지에 대한 고민을 통해 다양한 추천 알고리즘의 특성 및 활용 방법을 익힐 수 있었다. 또한 최종 추천을 위해 사용되는 자연어 처리/형용사 추출, 형용사 embedding, vector clustering/clustering distance, data normalization, vector 유사도 측정에 대해서도 각각 어떤 방법론들이 있고 어떤 상황에서 사용해야 하는지 등을 찾아보면서 진행했다. 분석에 적합한 방법들에 대해 성능 평가를 동시에 진행하며 최종적인 알고리즘을 완성할 수 있었다.   
&nbsp;&nbsp;&nbsp;&nbsp;결과적으로 이번 프로젝트를 통해 추천 시스템의 A-Z를 직접 구현해봄으로써 추천 알고리즘이 어떻게 동작하는지 잘 이해할 수 있었다. 다만, 적용한 추천 알고리즘의 논문이나 내부 로직을 100% 이해하지 못했다는 아쉬움이 있으며, 더 세부적인 논문 이해를 통해 모델링을 정교화한다면 더 좋은 결과를 도출할 수도 있을 것이라 생각하였다.


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

## References
* Florian Strub 외 2인. [「Hybrid Recommender System based on Autoencoders」](https://arxiv.org/abs/1606.07659v3). 2016
* Xiangana He 외 5인. [「Neural Collaborative Filtering」](https://arxiv.org/abs/1708.05031). 2017
* Maxim Naumov 외 23인. [「Deep Learning Recommendation Model for Personalization and Recommendation Systems」](https://arxiv.org/abs/1906.00091v1). 2019

## Reports
* [Final Report](reports/%EC%BA%A1%EC%8A%A4%ED%86%A4%EB%94%94%EC%9E%90%EC%9D%B8(%EA%B2%B0%EA%B3%BC%EB%B3%B4%EA%B3%A0%EC%84%9C_Khupid_%EC%9C%A0%EC%A0%95%EC%88%98).pdf)
* [Demo video](reports/Demo.mp4)

## Contributors

* [김동혁 (경희대학교 산업경영공학과)](https://github.com/LoveDH)
* [류연주 (경희대학교 관광학과)](https://github.com/YeonjuRyu)
* [유정수 (경희대학교 산업경영공학과)](https://github.com/youjeongsue)

## Roles

<table border="0" cellpadding="0" cellspacing="0" id="sheet0" class="sheet0 gridlines">
        <col class="col0">
        <col class="col1">
        <col class="col2">
        <tbody>
          <tr class="row0">
            <td class="column0 style1 s">주차</td>
            <td class="column1 style2 s">이름</td>
            <td class="column2 style3 s">추진내용</td>
          </tr>
          <tr class="row1">
            <td class="column0 style7 s style8" rowspan="6">2주차(3월 27일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- 1차 프로젝트 제안서(3.기대효과 및 활용방안, 4. 수행방법 일부) 작성</td>
          </tr>
          <tr class="row2">
            <td class="column2 style5 s">- 맛집/카페 : 수집 가능한 플랫폼 탐색</td>
          </tr>
          <tr class="row3">
            <td class="column1 style7 s style8" rowspan="2">류연주</td>
            <td class="column2 style4 s">- 1차 프로젝트 제안서(2. 과제 목표, 4. 수행방법 일부) 작성, 최종 취합</td>
          </tr>
          <tr class="row4">
            <td class="column2 style5 s">- 데이트 명소: 수집 가능한 데이터 탐색</td>
          </tr>
          <tr class="row5">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- 1차 프로젝트 제안서(1. 과제 개요, 4. 수행방법 일부) 작성</td>
          </tr>
          <tr class="row6">
            <td class="column2 style5 s">- 전시/영화 : 수집 가능한 데이터 탐색</td>
          </tr>
          <tr class="row7">
            <td class="column0 style7 s style8" rowspan="3">3주차(4월 3일)</td>
            <td class="column1 style6 s">김동혁</td>
            <td class="column2 style5 s">- 맛집/카페 : 망고플레이트를 통해 기본 데이터 및 리뷰 수집</td>
          </tr>
          <tr class="row8">
            <td class="column1 style6 s">류연주</td>
            <td class="column2 style5 s">- 데이트 명소 : 대한민국 구석구석(장소 데이터), TripAdvisor(리뷰 데이터) 크롤링 작업 시작</td>
          </tr>
          <tr class="row9">
            <td class="column1 style6 s">유정수</td>
            <td class="column2 style5 s">- 전시/영화 : 왓챠를 통한 영화 데이터 및 리뷰 크롤링</td>
          </tr>
          <tr class="row10">
            <td class="column0 style7 s style8" rowspan="4">4주차(4월 10일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- 맛집/카페 : 망고플레이트, 다이닝코드에서 데이터 크롤링</td>
          </tr>
          <tr class="row11">
            <td class="column2 style5 s">- clustering distance에 대한 research</td>
          </tr>
          <tr class="row12">
            <td class="column1 style6 s">류연주</td>
            <td class="column2 style5 s">- 데이트 명소 : 대한민국 구석구석(장소 데이터), TripAdvisor(리뷰 데이터) 크롤링 작업 완료</td>
          </tr>
          <tr class="row13">
            <td class="column1 style6 s">유정수</td>
            <td class="column2 style5 s">- 전시/영화 : 왓챠, 네이버영화에서 데이터 크롤링</td>
          </tr>
          <tr class="row14">
            <td class="column0 style7 s style8" rowspan="4">5주차(4월 17일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- 맛집/카페 : data 부족으로 인한 추가 크롤링</td>
          </tr>
          <tr class="row15">
            <td class="column2 style5 s">- 맛집/카페 : okt 패키지를 이용한 한글 형태소 분석</td>
          </tr>
          <tr class="row16">
            <td class="column1 style6 s">류연주</td>
            <td class="column2 style5 s">- 데이트 명소 : Kakao Map 장소/리뷰 데이터 크롤링</td>
          </tr>
          <tr class="row17">
            <td class="column1 style6 s">유정수</td>
            <td class="column2 style5 s">-전시/영화 : 오픈갤러리에서 전시 데이터 크롤링, 네이버 카페에서 전시 리뷰 데이터 크롤링</td>
          </tr>
          <tr class="row18">
            <td class="column0 style7 s style8" rowspan="6">6주차(4월 24일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- 맛집/카페 : 한글 리뷰에서 형용사 추출</td>
          </tr>
          <tr class="row19">
            <td class="column2 style5 s">- 한글 기반 Fast-Text로 임베딩 연구</td>
          </tr>
          <tr class="row20">
            <td class="column1 style7 s style8" rowspan="2">류연주</td>
            <td class="column2 style4 s">- 리뷰 자연어 처리를 위한 불용어 사전 구축 (한글)</td>
          </tr>
          <tr class="row21">
            <td class="column2 style5 s">- Papago로 데이트 명소 리뷰 데이터 번역 후 tokenizing 테스트</td>
          </tr>
          <tr class="row22">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- 전시/영화 : 한글 리뷰에서 형용사 추출</td>
          </tr>
          <tr class="row23">
            <td class="column2 style5 s">- 단순 형용사 추출 방법과 리뷰를 중요 문장으로 요약 후 형용사 추출 방법에 대해 연구</td>
          </tr>
          <tr class="row24">
            <td class="column0 style7 s style8" rowspan="6">7주차(5월 1일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- word embedding에서의 CBOW와 SKIPGRAM에 대한 research</td>
          </tr>
          <tr class="row25">
            <td class="column2 style5 s">- 맛집/카페: 데이터 통합 형식으로 변형</td>
          </tr>
          <tr class="row26">
            <td class="column1 style7 s style8" rowspan="2">류연주</td>
            <td class="column2 style4 s">- 데이트 명소: Kakao Map 데이터 크롤링 완료, 리뷰 및 장소 데이터를 통합 형식으로 변형</td>
          </tr>
          <tr class="row27">
            <td class="column2 style5 s">- 리뷰 자연어 처리를 Fast-Text 기법 + Papago로 변형한 리뷰데이터로 진행</td>
          </tr>
          <tr class="row28">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- 전시/영화 : 크롤링 완료 후 데이터 통합 형식으로 변형</td>
          </tr>
          <tr class="row29">
            <td class="column2 style5 s">- 번역하지 않은 데이터를 Fast-Text 기법을 사용해 embedding</td>
          </tr>
          <tr class="row30">
            <td class="column0 style7 s style8" rowspan="8">8주차(5월 8일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- 맛집/카페: 리뷰 영어로 번역</td>
          </tr>
          <tr class="row31">
            <td class="column2 style5 s">- GMM, Affinity Propagation, Spectral 등 clustering 적용 시도</td>
          </tr>
          <tr class="row32">
            <td class="column1 style7 s style8" rowspan="3">류연주</td>
            <td class="column2 style4 s">- 리뷰 자연어 처리 Word2Vec, BERT, ELMO, GLoVe research</td>
          </tr>
          <tr class="row33">
            <td class="column2 style4 s">- 데이트 명소: Word2Vec 적용 및 Fast-text와 비교</td>
          </tr>
          <tr class="row34">
            <td class="column2 style5 s">- 데이트 명소: Kmeans, DBSCAN, GMM 클러스터링 기법 적용</td>
          </tr>
          <tr class="row35">
            <td class="column1 style7 s style8" rowspan="3">유정수</td>
            <td class="column2 style4 s">- 전시/영화: 전시 리뷰 데이터 부족으로 추가 탐색</td>
          </tr>
          <tr class="row36">
            <td class="column2 style4 s">- 전시/영화: 한글 데이터에 대해 Word2Vec, Fast-text 적용 및 비교</td>
          </tr>
          <tr class="row37">
            <td class="column2 style5 s">-embedding한 vector 클러스터링 진행(K-means, K-medoids, DBSCAN)</td>
          </tr>
          <tr class="row38">
            <td class="column0 style7 s style8" rowspan="5">9주차(5월 15일)</td>
            <td class="column1 style6 s">김동혁</td>
            <td class="column2 style5 s">- Collaborative Filtering에서 Matrix Factorization에 대한 research</td>
          </tr>
          <tr class="row39">
            <td class="column1 style7 s style8" rowspan="2">류연주</td>
            <td class="column2 style4 s">- 데이트 명소: 카카오/트립어드바이저 모든 리뷰 Papago api 사용하여 영어로 번역</td>
          </tr>
          <tr class="row40">
            <td class="column2 style5 s">- 데이트 명소: User matrix, Item matrix 생성</td>
          </tr>
          <tr class="row41">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- 전시/영화: Papago api를 사용하여 모든 리뷰 데이터 번역</td>
          </tr>
          <tr class="row42">
            <td class="column2 style5 s">- 전시/영화: User matrix, Item matrix 생성</td>
          </tr>
          <tr class="row43">
            <td class="column0 style7 s style8" rowspan="5">10주차(5월 22일)</td>
            <td class="column1 style6 s">김동혁</td>
            <td class="column2 style5 s">- Neural Collaborative Filtering 논문에 제시된 코드 연구</td>
          </tr>
          <tr class="row44">
            <td class="column1 style7 s style8" rowspan="2">류연주</td>
            <td class="column2 style4 s">- 데이트 명소: 카카오/트립어드바이저 모든 리뷰 api 사용하여 영어로 번역</td>
          </tr>
          <tr class="row45">
            <td class="column2 style5 s">- 데이트 명소: User matrix, Item matrix 생성</td>
          </tr>
          <tr class="row46">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- NCF 논문 리뷰 및 적용 방안 제시</td>
          </tr>
          <tr class="row47">
            <td class="column2 style5 s">- 영화: User matrix, Item matrix 생성</td>
          </tr>
          <tr class="row48">
            <td class="column0 style7 s style8" rowspan="6">11주차(5월 29일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- 맛집/카페 : NCF 모델 적용</td>
          </tr>
          <tr class="row49">
            <td class="column2 style5 s">- 추천시스템 성능 평가방법 research</td>
          </tr>
          <tr class="row50">
            <td class="column1 style7 s style8" rowspan="2">류연주</td>
            <td class="column2 style4 s">- NCF모델 적용 방향 수정, Hybrid method research</td>
          </tr>
          <tr class="row51">
            <td class="column2 style5 s">- 데이트 명소: NCF 모델 적용 (Microsoft 라이브러리)</td>
          </tr>
          <tr class="row52">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- Hybrid method 적용 방법 연구 및 라이브러리 탐색</td>
          </tr>
          <tr class="row53">
            <td class="column2 style5 s">- 영화: Cornac 라이브러리 내부 로직 연구 및 NCF 모델 적용</td>
          </tr>
          <tr class="row54">
            <td class="column0 style7 s style8" rowspan="6">12주차(6월 5일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- NCF를 이용한 라이브러리 검색 및 각 장단점 파악</td>
          </tr>
          <tr class="row55">
            <td class="column2 style5 s">- User Matrix * Item Matrix cosine similarity 방식 테스트</td>
          </tr>
          <tr class="row56">
            <td class="column1 style7 s style8" rowspan="2">류연주</td>
            <td class="column2 style4 s">- User Matrix * Item Matrix 단순 행렬곱 적용 방식 테스트</td>
          </tr>
          <tr class="row57">
            <td class="column2 style5 s">- Data Normalization 방식 research</td>
          </tr>
          <tr class="row58">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- 벡터의 유사도 측정 방법 research</td>
          </tr>
          <tr class="row59">
            <td class="column2 style5 s">- User Matrix * Item Matrix 단순 행렬곱 적용 방식 테스트</td>
          </tr>
          <tr class="row60">
            <td class="column0 style7 s style8" rowspan="5">13주차(6월 12일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- 프로젝트 Flow chart 생성</td>
          </tr>
          <tr class="row61">
            <td class="column2 style5 s">-  맛집/카페 : Matrix Data Normalization</td>
          </tr>
          <tr class="row62">
            <td class="column1 style7 s style8" rowspan="2">류연주</td>
            <td class="column2 style4 s">- 데이트 명소: 형용사 word-cluster 라벨링, 조사 문항에 넣을 20개 대표 형용사 선정</td>
          </tr>
          <tr class="row63">
            <td class="column2 style5 s">-  데이트 명소 : Matrix Data Normalization</td>
          </tr>
          <tr class="row64">
            <td class="column1 style6 s">유정수</td>
            <td class="column2 style5 s">- 영화: cosine similarity 방식으로 변경 후 Matrix Data Normalization</td>
          </tr>
          <tr class="row65">
            <td class="column0 style7 s style8" rowspan="8">14주차(6월 19일)</td>
            <td class="column1 style7 s style8" rowspan="3">김동혁</td>
            <td class="column2 style4 s">- 테스터들에게 보낼 설문지 중, 1) 형용사에 대해 느끼는 호감도 정도 문항 및 3) 지역구 선택 작성</td>
          </tr>
          <tr class="row66">
            <td class="column2 style4 s">- 맛집/카페 : 최종 모델 완성</td>
          </tr>
          <tr class="row67">
            <td class="column2 style5 s">- Random Search를 통한 NCF  hyper parameter tuning</td>
          </tr>
          <tr class="row68">
            <td class="column1 style7 s style8" rowspan="3">류연주</td>
            <td class="column2 style4 s">- 테스터들에게 보낼 설문지 중, 2-2) 데이트 명소 문항 작성</td>
          </tr>
          <tr class="row69">
            <td class="column2 style4 s">- 맛집/카페, 데이트 명소, 영화 데이터를 조합한 최종 알고리즘 코딩</td>
          </tr>
          <tr class="row70">
            <td class="column2 style5 s">- 지역구 필터링 코딩</td>
          </tr>
          <tr class="row71">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- 영화: 현재 상영 영화 추천을 위한 데이터 추가</td>
          </tr>
          <tr class="row72">
            <td class="column2 style5 s">- 영화: 최종 모델 완성</td>
          </tr>
          <tr class="row73">
            <td class="column0 style7 s style8" rowspan="7">15주차(6월 26일)</td>
            <td class="column1 style7 s style8" rowspan="2">김동혁</td>
            <td class="column2 style4 s">- 제작된 알고리즘을 python 파일 및 모듈로 제작</td>
          </tr>
          <tr class="row74">
            <td class="column2 style5 s">- 영상 촬영</td>
          </tr>
          <tr class="row75">
            <td class="column1 style7 s style8" rowspan="3">류연주</td>
            <td class="column2 style4 s">- 최종 만족도 조사 방식 제안</td>
          </tr>
          <tr class="row76">
            <td class="column2 style4 s">- 만족도 설문지 작성</td>
          </tr>
          <tr class="row77">
            <td class="column2 style5 s">- 최종 발표 데모 영상 시나리오 작성 및 제작</td>
          </tr>
          <tr class="row78">
            <td class="column1 style7 s style8" rowspan="2">유정수</td>
            <td class="column2 style4 s">- 최종 발표자료 준비</td>
          </tr>
          <tr class="row79">
            <td class="column2 style5 s">- 유저별 알고리즘 실행 결과 및 만족도 조사 메일 발송, 취합</td>
          </tr>
        </tbody>
    </table>
