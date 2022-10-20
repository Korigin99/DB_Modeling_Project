import  csv
import random

""" f = open('info.csv','r')
rdr = csv.reader(f)

for line in rdr:
  print(line)

f.close() """

# 회원 번호는 PK


# 교통 사고 당사자 정보
""" fn = ['김','박','이','황','정','최','유','성','육','장','곽','한','노','조']
mn = ['지우','민준','서윤','서준','서연','민서','하윤','도윤','시우','서현','연우',
      '주원','예준','지민','지호','하은','지원','서진','지후','지안','하준','윤서','지유',
      '채원','준서','준우','채은','수정','주호','선우']
sex = ['남','여']
interest = ['개발자 도구', '교육', '그래픽 및 디자인', '뉴스', '도서', '사진 및 비디오', '소셜 네트워킹', '스포츠', '게임', '쇼핑']


f = open('taInfo.csv', 'a', newline='')
wr = csv.writer(f)

for i in range(100):
  fnRan = random.choice(fn)
  mnRan = random.choice(mn)
  sexRan = random.choice(sex)
  yearRan = random.randrange(1980,2005)
  monthRan = random.randrange(1,13)
  dateRan = random.randrange(1,32)
  interestRan = random.choice(interest)
  name = fn[fnRan] + mn[mnRan]
  dateBirth = str(yearRan)+"."+str(monthRan)+"."+str(dateRan)
  wr.writerow([i+1,name,sex[sexRan],dateBirth, interest[interestRan]])

f.close()
 """
# 대전시 교통사고 정보

f = open('교통사고정보3.csv', 'a', newline='')
wr = csv.writer(f)
# 사고 종류
n1 = ['음주운전','과속','신호위반','중앙선 침범']

# 부상/ 사망 정도
n2 = ['부상','부상','부상','부상','부상','부상','부상','부상','부상','사망']

#이름
fn = ['김','박','이','황','정','최','유','성','육','장','곽','한','노','조']
mn = ['지우','민준','서윤','서준','서연','민서','하윤','도윤','시우','서현','연우',
      '주원','예준','지민','지호','하은','지원','서진','지후','지안','하준','윤서','지유',
      '채원','준서','준우','채은','수정','주호','선우']

# 성별
sex = ['남','여']

# 면허 유무
driverSLicense = ['유', '유','유', '유','유', '유','유', '유','유','무']

# 음주 여부
drinking = ['무','무','무','무','무','무','무','무','무','유']

acloc =['동구 신인동', '동구 효동', '동구 용운동', '동구 삼성동', '동구 자양동',
'중구 대흥동', '중구 대사동', '중구 오류동', '중구 목동', '중구 은행선화동',
'서구 둔상동', '서구 갈마동', '서구 도마동', '서구 월평동', '서구 만년동',
'유성구 진잠동', '유성구 노은동', '유성구 전민동', '유성구 신성동', '유성구 관평동',
'대덕구 송촌동', '대덕구 석봉동', '대덕구 회덕동', '대덕구 오정동', '대덕구 법동']

num = ['A','B','C','D','Z','F','G','H','I','J','K','L']

sameNum = []
sameLoc = []
sameKind = []
sameDate = []
addr = ''
x = 0

c = 0
for i in range(1000):
  fnRan = random.choice(fn)
  mnRan = random.choice(mn)
  sexRan = random.choice(sex)
  yearRan = random.randrange(1960,2003)
  monthRan = random.randrange(1,13)
  dateRan = random.randrange(1,32)
  speed = random.randrange(90, 140)
  name = fnRan + mnRan
  adMonth = random.randrange(1,13)
  adDate = random.randrange(1,32)
  dateBirth = str(yearRan)+"."+str(monthRan)+"."+str(dateRan)
  accidentDate = "2022"+"."+str(adMonth) +"."+ str(adDate)
  nn = "2022" + num[adMonth-1] + str(random.randrange(1,100))
  dl = random.choice(driverSLicense)
  # dk = random.choice(drinking)
  accidentKind = random.choice(n1) #사고 종류
  asd = random.choice(n2) # 부상
  loc = random.choice(acloc)
  if(accidentKind == '음주운전'):
    dk = '유'
  else:
    dk = '무'

  if (speed>=130):
    asd = '사망'

  sameLoc.append(loc) 
  sameNum.append(nn)
  sameKind.append(accidentKind)
  sameDate.append(accidentDate)
  
  for j, snum in enumerate(sameNum):
    if nn in snum:
      loc = sameLoc[j]
      accidentKind = sameKind[j]
      accidentDate = sameDate[j]
      break
    
  wr.writerow([i+1, name, sexRan, dateBirth, '유','유', dk, asd, accidentKind, accidentDate, speed, loc, nn])

""" with open("교통사고정보1.csv", 'a') as f:
  f.truncate(0) """

