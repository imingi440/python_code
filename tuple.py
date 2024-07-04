# 튜플 생성
my_tuple=(1,2,3)
print(my_tuple)

# 튜플 값 가져오기 (인덱싱)
print(my_tuple[1])
print(my_tuple[-1])

# 튜플은 괄호 없이도 생성이 가능하다
my_tuple=1,2,3
print(my_tuple)

# 튜플 슬라이싱
my_tuple=(1,2,3)
print(my_tuple[1:3])

# 튜플 값 한번에 변수에 할당하기
my_tuple=(1,2,3)
a,b,c=my_tuple
print(a) # 1
print(b) # 2
print(c) # 3
print("")
# 한번에 여러개 할당하는 방법
my_tuple = (1,2,3,4,5,6,7,8,9,10)
a,b,*c=my_tuple
print(a) # 1
print(b) # 2
print(c) # [3,4,5,6,7,8,9,10]

