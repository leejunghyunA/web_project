## 📊 발표주제 및 자료
### 와린이(와인 입문자)를 위한 '와인추천 서비스' 웹사이트 구현
[![발표자료 보러가기](https://user-images.githubusercontent.com/108326629/210938178-07dd3a18-aef9-4f5b-8ef6-9dedf1fbe152.png "발표자료 보러가기")](https://github.com/choi-aerim/220902_0926-Web-ML-project/blob/main/4.%20%EA%B2%B0%EA%B3%BC%20PPT%20%EB%B0%8F%20%EC%98%81%EC%83%81/B_WINEZ_%EC%99%80%EB%A6%B0%EC%9D%B4%EB%A5%BC%20%EC%9C%84%ED%95%9C%20%EC%99%80%EC%9D%B8%EC%B6%94%EC%B2%9C%EC%84%9C%EB%B9%84%EC%8A%A4%20%EC%9B%B9%EC%82%AC%EC%9D%B4%ED%8A%B8%20%EA%B5%AC%ED%98%84.pdf)<br/>
</br>
</br>
## 🌱 요약
### 기획 배경
- 와인 소비량이 코로나 이후 2배 이상 급성장, 수입 주류 시장에서 맥주를 제치고 **1위** 
  > 대형마트, 편의점 등 대부분의 **유통채널**이 와인을 들이는 것에 적극적이며 종류와 가격대가 다양, 혼술족을 겨냥해 부담 없이 마실 수 있는 **가성비 와인**이 잇따라 출시
  
  > 코로나 19 장기화로 **‘취하기 위해 마시는 술’** 에서 **‘맛있는 술’ ‘즐길 수 있는 술’** 로 주류 문화가 변화
  
 - 와인에 대한 수요 증가로 **'와린이'를 위한 정보 필요성 증가** (와린이 : 와인에 대한 배경지식이 없는 와인 입문자)
 

 ### 문제 제기
 
 ![image](https://user-images.githubusercontent.com/108326573/192915765-bc1658aa-3217-4dec-81f2-57e026003d8c.png)

 - 기존 와인 조회 서비스는 **와인 관여도가 높은 유저 중점**
  > 탄닌, 바디감, 포도종 등 와인 입문자가 활용하기 어려운 특징으로 카테고리화 하였고, 추천하는 이달의 와인도 **기존 고관여 유저 중심**으로 구성되어있음 (ex. 고품질 샤르데나 와인의 뛰어난 풍미, 스페인 토착 품종의 새로운 매력 등)
 
 - 와인 입문자가 활용하기 어려운 홈페이지 조회 기능 용어 구성 => **1차선택에 어려움을 줌**
 
 ### 최종 목표
 
 - 기존 사이트 차별화 및 개선점(P.O.D): 
 > 직접적인 특징(바디, 당도, 산도 등)을 추론할 수 있는 은유적 설문 형식(쉬운 용어로 시각화)으로 본인의 와인취향을 유추해볼 수 있는 와인을 추천하는 서비스를 제공
 
 > 카테고리를 포도종과 같은 어려운 용어로 구별하지 않고 어느음식에 먹을건지, 누구와 먹을 건지, 어떤 향이 나는 와인을 좋아하는지와 같이 일상에서 접하는 항목으로 나눠 본인이 원하는 상황과 취향에 맞게 선택할 수 있도록 구성
 
 ### 사이트 구성
 
 #### <구성 목록>
 - 나의 와인 취향 알아보기
  와린이가 선호할만한 와인타입/당도/산도/바디/도수를 추론할 수 있는 설문을 실시하여 추론된 데이터와 비슷한 군집화된 와인 리스트를 제공

- 카테고리별 와인 추천
  
  * FLAVOR (와인 맛) : 
  와인 맛에 대한 중분류를 선택할 수 있도록 제공

  * DISH (페어링 음식) : 
  크롤링한 데이터 내 페어링할 음식(소분류)에서 
  중분류 음식을 카테고리화하여 제공

  * CHARACTER (와인 특징) :
  당도, 산도, 바디감으로 와인 조회 제공

  * SITUATION(와인 마시는 상황) :
  와인타입, 당도, 산도, 도수, 음식 대분류 변수로 군집화 후
  해당 상황을 카테고리화하여 제공    

- 와인 라벨 인식, 로그인, Mypage(원하는 와인 담기)

 ### 기대 효과
 
- 기존 사이트의 **'고관여도 유저 중심 정보 조회 제공'** (와인 검색시 1차 진입 장벽) 해결

- '직관적이고 이해하기 쉬운 카테고리별 정보 조회 제공'을 통해 와인 수요가 증가하면서 역시 증가하고 있는 와린이들의 와인 입문이 보다 쉬워짐

- **와인 및 주류 시장의 성장** 도모

</br></br>
## 사용한 모듈
- 언어: <img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"/>
- 구축환경: <img src="https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white"/> 
- 활용 기술: <img src="https://img.shields.io/badge/Selenium-00660?style=flat-square&logo=Selenium&logoColor=white"/><img src="https://img.shields.io/badge/Beautifulsoup-FF0000?style=flat-square&logo=Beautifulsoup&logoColor=white"/>을 이용하여 신세계 L&B 및 VIVINO 사이트 와인 정보 크롤링
<img src="https://img.shields.io/badge/Scikit_learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=black"/> 의 K-Means를 이용하여 1.취향 추천을 위한 군집화 및 분류학습 2.상황별 추천을 위한 군집화
<img src="https://img.shields.io/badge/Pytesseract OCR-004088?style=flat-square&logo=Pytesseract OCR&logoColor=white"/> 을 이용한 이미지 내 텍스트 추출 => 추출된 단어가 있는 와인을 불러오도록 구현
- 통합 개발 환경: <img src="https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=Anaconda&logoColor=black"/> <img src="https://img.shields.io/badge/Jupyter Notebook-F37626?style=flat-square&logo=Jupyter&logoColor=black"/> <img src="https://img.shields.io/badge/Visual Studio-5C2D91?style=flat-square&logo=Visual Studio&logoColor=white"/></br>
- 웹 구현: <img src="https://img.shields.io/badge/Django-004088?style=flat-square&logo=Django&logoColor=white"/> Django생성한 데이터를 기반으로 카테고리, mypage, 와인 리스트, 와인 설명칸, log-in 구현

</br>
</br>

## 최종 구현 화면
![B_WINEZ_와린이를-위한-와인추천서비스-웹사이트-구현_구현영상_압축_ (1)](https://user-images.githubusercontent.com/108326629/210950351-b7125bf7-a436-4c20-9406-87bb330ffe92.gif)

</br>
</br>

## 👩‍👩‍👧‍👦 팀원 소개

| 팀원 | 업무 | 깃허브 주소 |
| ------ | -- | ----------- |
| 최애림 | 와인정보 크롤링, 데이터 전처리, 군집화, 이미지 내 텍스트 추출 | https://github.com/choi-aerim |
| 이정현 | 와인정보 크롤링, 데이터 전처리, 웹 구현 | https://github.com/leejunghyunA |


## 💬 아쉬운 점
와인 정보가 사이트에 자세히 게시되어있지않아 약 300개 정도의 와인으로만 군집화하여 정확한 특징을 찾기 힘들었습니다. 그래서 손군집으로 비슷한 특징으로 묶어 카테고리를 생성하였지만 새로운 와인이 추가되면 군집 내용이 달라질 수 있는 일회성의 느낌이 강해서 실전에 사용할 수 없는 부분이 아쉬웠다. 

