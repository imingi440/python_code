# 값을 입력받아 마름모를 그리는 반복문
marumo=int(input("마름모의 크기를 입력해주세요.: "))

for a in range(marumo,1,-1):
  print("*"*a," "*(marumo-a)," "*(marumo-a),"*"*a)

for i in range(1,marumo+1):
   print("*"*i," "*(marumo-i)," "*(marumo-i),"*"*i)