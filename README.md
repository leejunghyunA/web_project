# 와인추천솔루션

## 1. 기획 배경
- 와인 소비량이 코로나 이후 2배 이상 급성장, 수입 주류 시장에서 맥주를 제치고 **1위** 
  > 대형마트, 편의점 등 대부분의 **유통채널**이 와인을 들이는 것에 적극적이며 종류와 가격대가 다양, 혼술족을 겨냥해 부담 없이 마실 수 있는 **가성비 와인**이 잇따라 출시
  
  > 코로나 19 장기화로 **‘취하기 위해 마시는 술’** 에서 **‘맛있는 술’ ‘즐길 수 있는 술’** 로 주류 문화가 변화
  
 - 와인에 대한 수요 증가로 **'와린이'를 위한 정보 필요성 증가** (와린이 : 와인에 대한 배경지식이 없는 와인 입문자)
 
 ## 2. 문제 제기
 
 ![image](https://user-images.githubusercontent.com/108326573/192915765-bc1658aa-3217-4dec-81f2-57e026003d8c.png)

 - 기존 와인 조회 서비스는 **와인 관여도가 높은 유저 중점**
  > 탄닌, 바디감, 포도종 등 와인 입문자가 활용하기 어려운 특징으로 카테고리화 하였고, 추천하는 이달의 와인도 **기존 고관여 유저 중심**으로 구성되어있음 (ex. 고품질 샤르데나 와인의 뛰어난 풍미, 스페인 토착 품종의 새로운 매력 등)
 
 - 와인 입문자가 활용하기 어려운 홈페이지 조회 기능 용어 구성 => **1차선택에 어려움을 줌**
 
 ## 3. 목표
 
 - 기존 사이트 차별화 및 개선점(P.O.D): 
 > 직접적인 특징(바디, 당도, 산도 등)을 추론할 수 있는 은유적 설문 형식(쉬운 용어로 시각화)으로 본인의 와인취향을 유추해볼 수 있는 와인을 추천하는 서비스를 제공
 
 > 카테고리를 포도종과 같은 어려운 용어로 구별하지 않고 어느음식에 먹을건지, 누구와 먹을 건지, 어떤 향이 나는 와인을 좋아하는지와 같이 일상에서 접하는 항목으로 나눠 본인이 원하는 상황과 취향에 맞게 선택할 수 있도록 구성
 
 ## 4. 사이트 구성
 
 ### <구성목록>
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

 ## 5. 기대 효과
 
- 기존 사이트의 **'고관여도 유저 중심 정보 조회 제공'** (와인 검색시 1차 진입 장벽) 해결

- '직관적이고 이해하기 쉬운 카테고리별 정보 조회 제공'을 통해 와인 수요가 증가하면서 역시 증가하고 있는 와린이들의 와인 입문이 보다 쉬워짐

- **와인 및 주류 시장의 성장** 도모

## 6. 사이트 구성 방법 및 활용 언어

|                | 활용언어 & 사용방법             |
|----------------|-------------------------------|
|와인 정보 크롤링 |**selenium 과 beautifulsoup** 을 이용하여 신세계 L&B와인 정보 크롤링(이후 전처리 작업)|
|Collection 라이브러리 Okt 활용|차가운 육류요리, 붉은육류요리 등 형용사와 같이 설명되어있는 음식 정보에서  빈도수를 확인하여 빈도수가 높은 단어를 기준으로 **중분류 키워드 추출**|
|scikit.learn|1.취향 추천을 위한 **군집화 및 분류학습** 2.상황별 추천을 위한 **군집화**|
|Tesseract OCR|이미지에서 텍스트를 추출하여 인식된 텍스트와 숫자로만 이루어진 단어가 출력되도록 코드 생성 => 추출 된 단어가 있는 와인을 불러오도록 구현|
|Django|생성한 데이터를 기반으로 카테고리, mypage, 와인 리스트, 와인 설명칸, log-in 구현|

## 7. 최종 구현 화면
https://github.com/leejunghyunA/my_dj/blob/main/%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%83%9D%EC%84%B1%EA%B3%BC%EC%A0%95/%EC%B5%9C%EC%A2%85_output/B_WINEZ_%EC%99%80%EB%A6%B0%EC%9D%B4%2C%20%EC%9D%B4%EB%A6%AC%EC%99%80%EB%A6%B0%EC%9D%B4_%EA%B5%AC%ED%98%84%EC%98%81%EC%83%81.mp4

## 아쉬운 점
와인 정보가 사이트에 자세히 게시되어있지않아 약 300개 정도의 와인으로만 군집화하여 정확한 특징을 찾기 힘들었습니다. 그래서 손군집으로 비슷한 특징으로 묶어 카테고리를 생성하였지만 새로운 와인이 추가되면 군집 내용이 달라질 수 있는 일회성의 느낌이 강해서 실전에 사용할 수 없는 부분이 아쉬웠다. 
### 자세한 진행사항
https://github.com/leejunghyunA/my_dj/blob/main/%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%83%9D%EC%84%B1%EA%B3%BC%EC%A0%95/%EC%B5%9C%EC%A2%85_output/B_WINEZ_%EC%99%80%EB%A6%B0%EC%9D%B4%2C%20%EC%9D%B4%EB%A6%AC%EC%99%80%EB%A6%B0%EC%9D%B4.pdf

- produce by 최애림, 이정현A
