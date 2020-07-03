# Korea_influencer_clustering_analysis  

## 주요 내용  

* SNS가 중요한 커뮤니케이션 도구로 발전하면서, 다수의 사람들과 SNS를 통해 소통하면서 영향력을 발휘하는 소셜 인플루언서를 활용한 마케팅의 빈도가 늘고 있다. 미국 시장조사 전문 기관인 Statista가 2019년에 발표한 보고서에 따르면, 전 세계 인스타그램 인플루언서 마케팅만 56억만 달러로 2015년부터 3년간 12배까지 급증했고, 2020년에는 80억만 달러까지 늘어날 것으로 추정했다. 특히, 인플루언서 마케팅이 가장 활성화된 미국에서는 인플루언서 마케팅의 수익률이 기존의 마케팅에 비해 6.5배로 조사되었고, 미국 주간지 포브스에 따르면 미국 비즈니스 오너 중 약 40%가 소셜 미디어를 통해 상품을 판매한다. 이렇게 SNS와 인플루언서의 영향력이 확대되면서 마케팅의 흐름이 광고의 대다수를 차지하던 기존의 라디오, TV 등의 매체에서 Youtube, Facebook, Instagram 등의 SNS 매체로 이동하고 있다. 또한 한국에서도 밀레니엄세대, Z세대를 공략하기 위해 소셜 미디어 마케팅이 확산되는 추세이다. 이에 한국 시장의	소셜 시장과 인플루언서에 대한 분석이 필요함을 느꼈고, 머신러닝을 활용하여 한국 시장의 소셜 인플루언서를 분석하고자 한다.  

* 미국의 소셜 인플루언서 마케팅의 활용과 성공 사례를 살펴보고, 한국 시장에서의 영향력 있는 인플루언서는 어떻게 정의할 수 있을지, 기업의 성격별로 어떤 인플루언서 마케팅 전략을 선택해야 할지에 대한 인사이트를 얻기 위해 다양한 클러스터링 기법으로 한국 시장을 분석한다. 인플루언서의 선호도가 91.9%로 가장 높은 인스타그램을 분석 대상 플랫폼으로 잡았고, 인플루언서 마케팅이 가장 활발한 뷰티 분야를 분석하기 위해 '뷰티' 태그를 통해 데이터를 수집한다. 수집한 데이터의 대표적인 feature를 뽑아내고 여러 클러스터링 기법을 통해 인플루언서의 군집을 나눈 뒤, 군집별 특징에 따라 각 군집을 정의한다.  

* 즉, 한국 시장의 소셜 인플루언서 마케팅의 인사이트를 확보하기 위해 여러가지 클러스터링 기법으로 한국 인플루언서를 군집화하고 어떤 군집인지 정의하는 것이 이번 프로젝트의 주요 내용이다.  

## 진행 과정  
1. 웹 크롤링을 통해 뷰티 태그의 인스타그램 데이터를 수집(1000명의 뷰티 인플루언서에 대한 12 features) 

2. 데이터 전처리
3. 데이터 탐색(Data Exploration)
4. data exploration을 통해 도출한 결과를 바탕으로 파생변수 생성 및 Clustering feature 선택
5. Clustering 진행

- 알고리즘 선택 및 모델 수립  
- elbow 확인  
- evaluation(Silhouette coefficient)  
- 군집 수 조절  
- 한계 파악 및 알고리즘 재선택  
- 위 과정을 반복하며 최적 군집 도출  

6. 인플루언서 군집 정의  

## 결과
### 데이터셋
* 기본 변수(12): Account, Post, Follower, Follow, Open-account, Official-account, Image_love, Image_comment, Video-love, Video-comment, Igtv-love, Igtv-comment  
* 파생 변수(2): ER, active_rate  
### feature 선택  
1) 상품, 서비스를 최대한 많은 사람에게 노출시킬 수 있는 인플루언서  
2) 소비자와 interaction이 활발하여 소비자 그룹의 실질적인 구매력을 높일 수 있는 인플루언서


  -> 위의 두 SNS 인플루언서 마케팅 전략을 대표하는 feature(3): follower, ER, active_rate
* ER: 인플루언서의 게시물에 반응하는 follower의 비율  
  -> 구매력에 대한 신뢰도
* active_rate: 인플루언서의 게시물에 반응하는 follower 중 적극적인 잠재 소비자 비율  
  -> follower들의 잠재 구매력

### Clustering 모델 학습 및 비교
- ER, active_rate으로 clustering 진행  
1) K-means  
   - K = 3 ~ 8 결과 비교, 평균 silhouette값 및 편차 확인.  
   - K = 4 결과가 가장 적절하다고 판단.  
   ![image](https://user-images.githubusercontent.com/33457632/86476719-08d81b00-bd82-11ea-8417-20090a9841ba.png)
   ![image](https://user-images.githubusercontent.com/33457632/86476750-17263700-bd82-11ea-8cfa-1ab56b97fb0a.png)  
   - 한계점: Random initial centroid, outlier 처리 불가능, Data exploration에서 확인한 유의미한 outlier 반영하지 못함.  
   
   
2) K-medoids  
   - K = 3, 4, 5 결과 비교, K-means 클러스터 산포도와 비교.  
   - K = 3 결과가 가장 적절하다고 판단.  
   ![image](https://user-images.githubusercontent.com/33457632/86476784-2907da00-bd82-11ea-9a8b-fecee45a520b.png)  
   - K-means(K=4)와 비교.  
   ![image](https://user-images.githubusercontent.com/33457632/86476828-38872300-bd82-11ea-82f3-2c41138f0ede.png)
   ![image](https://user-images.githubusercontent.com/33457632/86476849-42a92180-bd82-11ea-9dc6-76c03a1bda3b.png)  
   - 한계점: K-means와 비교했을 때, random initial centroid 문제는 해결되었지만 outlier에 대해서는 오히려 더 적절하지 않은 cluster 생성.  
   
   
3) Hierarchical clustering  
   - 유클리드 거리, 최단연결법, 병합방식 세팅.   
   - Threshold를 20, 25, 30으로 설정해서 cluster 수를 6, 4, 3으로 정해서 확인.  
   - K = 6 결과가 가장 적절하다고 판단.  
  ![image](https://user-images.githubusercontent.com/33457632/86476869-505ea700-bd82-11ea-82f2-7ff5293885bf.png)  
   - K = 6 뿐만 아니라 K = 4, 3 모두 K-means, K-medoids에 비해 outlier에 대한 분리를 가장 잘한다. 인플루언서 데이터 셋에서 outlier는 중요한 instance이기 때문에 이를 가장 잘 반영하는 Hierarchical clustering이 세 모델 중 최적의 모델이라고 판단.  
  


### 군집 구성
- 가장 적절하다고 판단한 Hierarchical clustering의 군집 수 6개.  


  - cluster 0: ER에 비해 active_rate 월등히 높음 – 3  
  - cluster 1: ER과 active_rate 모두 월등히 높음 – 1  
  - cluster 2: ER과 active_rate 모두 낮음 – 856  
  - cluster 3: ER에 비해 active_rate 높음 – 24  
  - cluster 4: active_rate에 비해 ER 높음 – 38  
  - cluster 5: active_rate에 비해 ER 월등히 높음 – 7  

  ![image](https://user-images.githubusercontent.com/33457632/86477128-c5ca7780-bd82-11ea-8d98-3667e23e465b.png)


### 군집 정의  
- ER은 follower 대비 좋아요와 댓글 합의 비율이고, active_rate은 좋아요 대비 댓글의 비율이므로, active_rate 을 실질적인 follower들의 잠재 구매력, ER은 그 구매력에 대한 신뢰도를 나타낸다.  
- cluster의 계층을 나눠보면, 1 -> 0 -> 5 -> 3 -> 4 -> 2 로 구분된다.  


  - cluster1: follower들의 잠재 구매력과 신뢰도 모두 높은 군집  
  - cluster0: follower들의 잠재 구매력은 매우 높지만 신뢰도가 낮은 군집  
  - cluster5: follower들의 잠재 구매력은 매우 낮지만 신뢰도가 높은 군집  
  - cluster3: follower들의 잠재 구매력은 중간 정도이며 신뢰가 낮은 군집  
  - cluster4: follower들의 잠재 구매력은 매우 낮지만 신뢰도가 중간인 군집  
  - cluster2: follower들의 잠재 구매력과 신뢰도 모두 낮은 군집  
  
## 결론  

- 인플루언서의 follower들의 잠재 구매력을 대표하는 active_rate와 인플루언서의 게시물에 반응하는, 잠재 구매력에 대한 신뢰성을 나타내는 ER의 두 개의 feature로 K-means, K-medoids, 계층 군집 분석(Hierarchical Clustering)을 진행하였다. 그 중 가장 적절하다고 판단한 계층 군집 분석의 6개의 군집을 분석해본 결과, 아래와 같은 군집들로 정의할 수 있다.


- Highest benefit: follower들의 잠재 구매력과 신뢰도 모두 높은 군집  
- Low Cost High benefit: follower들의 잠재 구매력은 매우 높지만 신뢰도가 낮은 군집  
- High Interactive: follower들의 잠재 구매력은 매우 낮지만 신뢰도가 높은 군집  
- Middle benefit: follower들의 잠재 구매력은 중간 정도이며 신뢰가 낮은 군집  
- middle Interactive: follower들의 잠재 구매력은 매우 낮지만 신뢰도가 중간인 군집  
- Lowest benefit: follower들의 잠재 구매력과 신뢰도 모두 낮은 군집  


- 단순히 follower 수로 메가, 매크로, 마이크로, 나노로 구분하지 않고 마케팅 측면에서의 인사이트를 위해 각 인플루언서 팔로워의 실질적인 구매력을 바탕으로 군집을 나누고 정의를 하였다. 총 6개의 군집이 존재하고, 각 군집은 계층적으로 구성된다.

## 파일 구성  

- Influencer_crawler
  - beauty_influencer_account.csv: 뷰티 인플루언서 계정 데이터
  - beauty_basic_info.csv: 뷰티 인플루언서 기본 변수 포함 데이터
  - beauty_post_info.csv: 뷰티 인플루언서 게시물 관련 데이터
  - final_beauty_dataset.csv: basic과 post 정보 병합 데이터
  - data_merge.py: 데이터 셋 병합
  - inflencer_1000_crawler.py: 인플루언서 계정 크롤링
  - influencer_basic_crawler.py: 인플루언서 기본 변수 크롤링
  - influencer_post_crawler.py: 인플루언서 게시물 정보 크롤링
  
- Clustering
  - beauty_data_extend.csv: 최종 데이터(파생변수 포함)
  - DC_static_analysis.ipynb: 데이터 탐색 및 파생변수 도출
  - DC_K_means.ipynb: K-means 및 실루엣 지수
  - DC_K_medoids.ipynb: K-medoids
  - DC_K_Hierarchical_clustering.ipynb: Hierarchical clustering 및 군집 정의
  

## 클러스터링 알고리즘 설명 링크  

* K-means: <https://bcho.tistory.com/1203>
* K-medoids: <https://m.blog.naver.com/PostView.nhn?blogId=sw4r&logNo=221032973117&proxyReferer=https:%2F%2Fwww.google.com%2F>
* Hierarchical clustering: <https://bcho.tistory.com/1204>
