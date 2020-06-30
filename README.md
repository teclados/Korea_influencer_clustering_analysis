# Korea_influencer_clustering_analysis  

## 주요 내용  

* SNS가 중요한 커뮤니케이션 도구로 발전하면서, 다수의 사람들과 SNS를 통해 소통하면서 영향력을 발휘하는 소셜 인플루언서를 활용한 마케팅의 빈도가 늘고 있다. 미국 시장조사 전문 기관인 Statista가 2019년에 발표한 보고서에 따르면, 전 세계 인스타그램 인플루언서 마케팅만 56억만 달러로 2015년부터 3년간 12배까지 급증했고, 2020년에는 80억만 달러까지 늘어날 것으로 추정했다. 특히, 인플루언서 마케팅이 가장 활성화된 미국에서는 인플루언서 마케팅의 수익률이 기존의 마케팅에 비해 6.5배로 조사되었고, 미국 주간지 포브스에 따르면 미국 비즈니스 오너 중 약 40%가 소셜 미디어를 통해 상품을 판매한다. 이렇게 SNS와 인플루언서의 영향력이 확대되면서 마케팅의 흐름이 광고의 대다수를 차지하던 기존의 라디오, TV 등의 매체에서 Youtube, Facebook, Instagram 등의 SNS 매체로 이동하고 있다. 또한 한국에서도 밀레니엄세대, Z세대를 공략하기 위해 소셜 미디어 마케팅이 확산되는 추세이다. 따라서 한국 시장의	소셜 시장과 인플루언서에 대한 분석이 필요함을 느꼈고, 머신러닝을 활용하여 한국 시장의 소셜 인플루언서를 분석하였다.  

* 미국의 소셜 인플루언서 마케팅의 활용과 성공 사례를 살펴보고, 한국 시장에서의 영향력 있는 인플루언서는 어떻게 정의할 수 있을지, 기업의 성격별로 어떤 인플루언서 마케팅 전략을 선택해야 할지에 대한 인사이트를 얻기 위해 다양한 클러스터링 기법으로 한국 시장을 분석하였다. 인플루언서의 선호도가 91.9%로 가장 높은 인스타그램을 분석 대상 플랫폼으로 잡았고, 인플루언서 마케팅이 가장 활발한 뷰티 분야를 분석하기 위해 '뷰티' 태그를 통해 데이터를 수집하였다. 수집한 데이터의 대표적인 feature를 뽑아내고 여러 클러스터링 기법을 통해 인플루언서의 군집을 나눈 뒤, 군집별 특징에 따라 각 군집을 정의하였다.  

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
  
## 결론
| 순번 | 내용 | 3월 | 4월 | 5월 | 6월 |
|---|:---:|:---:|:---:|:---:|:---:|
| `1` | 연구 기획 | O | O | | |
| `2` | 데이터 수집 |  | O | O | |
| `3` | 데이터 정제 및 feature 선택 | | O | O | |
| `4` | 모델 학습 |  | | O | O |
| `5` | 데이터 시각화| | | O | O |
| `6` | 인사이트 도출| | | | O |

## 파일 구성
