# Korea_influencer_clustering_analysis  

## 과제명  
머신러닝을 활용한 한국시장의 소셜 인플루언서 분석
 
## 주요 내용
* SNS가 중요한 커뮤니케이션 도구로 발전하면서, 다수의 사람들과 SNS를 통해 소통하면서 영향력을 발휘하는 소셜 인플루언서를 활용한 마케팅의 빈도가 늘고 있다. 특히, 인플루언서 마케팅이 가장 활성화된 미국에서는 인플루언서 마케팅의 수익률이 기존의 마케팅에 비해 6.5배로 조사되었고, 미국 주간지 포브스에 따르면 미국 비즈니스 오너 중 약 40%가 소셜 미디어를 통해 상품을 판매한다. 이렇게 SNS와 인플루언서의 영향력이 확대되면서, 한국에서도 밀레니엄세대, Z세대를 공략하기 위해 소셜 미디어 마케팅이 확산되는 추세이다. 아직은 분석이 부족한 한국 시장의 소셜 인플루언서에 대한 분석이 필요함을 느꼈고, 미국과 비교하여 한국에서의 영향력있는 인플루언서를 어떻게 정의하고, 그룹이 나뉘는지를 분석하고자 하였다. 

* 인플루언서의 선호도가 91.9%로 가장 높은 인스타그램을 분석 대상 플랫폼으로 잡았고, 뷰티, 패션 등 인플루언서 마케팅이 가장 활발한 분야의 태그를 통해 데이터를 수집할 예정이다. 수집한 데이터를 통해 한국의 인플루언서를 Clustering하고 평가하여, 각 그룹에 대한 정의와 인사이트를 찾고자 한다.

## 과제 목표
* 데이터 셋은 뷰티, 패션 분야의 인스타그램 데이터를 사용할 예정이고, 도출된 cluster의 타당성은 silouette 계수가 0.6 이상이 정량적인 목표치이다. 각 그룹을 시각화하고 특징을 파악하여, 최종적으로 한국 소셜 인플루언서 마케팅에 대한 인사이트를 도출하는 것이 목표이다. 따라서 최종 결과물의 형태는 데이터를 분석한 논리적, 시각적 자료가 될 것이다.

## 과제 수행 계획
* 개요
K-means, DBSCAN의 거리 기반, 밀도 기반 클러스터링을 진행한 뒤, 군집의 타당성에 따라 (군집 내 분산, 군집 간 분산) 추가적인 여러 clustering 기법을 수행할 예정이다. 데이터 분석을 위해 pandas, sklearn, numpy, matplotlib 등의 라이브러리를 사용할 것이고, 해당 분석은 모두 python으로 진행되며, PyCharm, Idle, Jupyter notebook을 사용한다. 만약 추가적으로 딥러닝 기법인 SOM을 수행한다면 K-means, DBSCAN의 군집타당성 지표가 정량적인 목표에 부합하지 않거나, feature selection을 진행하는데 dimension 축소의 근거가 부족할 때 수행할 예정이다.

  
## 추진 일정
| 순번 | 내용 | 3월 | 4월 | 5월 | 6월 |
|---|:---:|:---:|:---:|:---:|:---:|
| `1` | 연구 기획 | O | O | | |
| `2` | 데이터 수집 |  | O | O | |
| `3` | 데이터 정제 및 feature 선택 | | O | O | |
| `4` | 모델 학습 |  | | O | O |
| `5` | 데이터 시각화| | | O | O |
| `6` | 인사이트 도출| | | | O |
