#def<함수이름>(<변수>, ... , <변수>)
#<블록>
#함수에서 만들어낸 정보를 결과로 내주려면 <블록> 에서 실행 흐름이 끝나는 부분에 다음과 같은 형식으로 return 문을 닫아두어야 한다.

#예약어 pass
#실행해도 아무 영향이 없는 명령이다, 아무일도 하지 않는 명령어

#온도 변환 함수
#화씨온도를 인수로 받아 섭씨 온도로 변환해주는 함수
#공식: c=(F-32)*5/9
def fahrenhenit2celsius(f):
  return None #Write your expression here.
#Test code
print(fahrenheit2celsius(67))           #19.44444444443
printf(round(fahrenheit2celsius(69),1)) #19.4

#9의 보수 계산 함수
#공식: 10**k-1-n
def complement_nine(n):
  return None #Write your expression here.
#test code
print(complement_nine(0)) #9
print(complement_nine(9)) #0
print(complement_nine(4)) #5
print(complement_nine(18)) #81
print(complement_nine(40)) #59
print(complement_nine(307)) #692
print(complement_nine(9142)) #857
print(complement_nine(9999)) #0
