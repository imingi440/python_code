# 딕셔너리 장점 : 키만 알고 있으면 바로 값을 뽑아낼 수가 있기 때문에 빠르다.
# 딕셔너리 단점 : 키를 모르면 값을 알 수가 없다.

# 딕셔너리 생성
my_dict={'LName':'Lee','FName':'Mingi','Age':'25'}
print(my_dict["LName"])
print(my_dict["FName"])
print(my_dict["Age"])

# 딕셔너리 값 변경
my_dict={'LName':'Lee','FName':'Mingi','Age':'25'}
print(my_dict)

my_dict['LName']='Park'
print(my_dict['LName'])

my_dict['FName']='Chulsoo'
print(my_dict['FName'])

my_dict['Age']='20'
print(my_dict['Age'])

# 딕셔너리 키, 값 쌍 삭제
my_dict={'LName':'Lee','FName':'Mingi','Age':'25'}

del my_dict['LName']
print(my_dict)

my_dict.pop('FName')
print(my_dict)

#모든 키 값 쌍 얻기
my_dict={'LName':'Lee','FName':'Mingi','Age':'25'}
print(my_dict.items())# 딕셔너리의 키와 값 두개 다 추출한다 items()

# 모든 키 얻기
my_dict={'LName':'Lee','FName':'Mingi','Age':'25'}
print(my_dict.keys()) # 딕셔너리의 모든 키를 보여준다. keys()

# 모든 값 얻기
my_dict={'LName':'Lee','FName':'Mingi','Age':'25'}
print(my_dict.values()) # 딕셔너리의 모든 값을 보여준다. values()

# 딕셔너리 비우기
my_dict={'LName':'Lee','FName':'Mingi','Age':'25'}
print(my_dict)
my_dict['Birth']="2000.03.23"  # 딕셔너리 값 추가
print(my_dict)

my_dict.clear()# 딕셔너리의 모든 키와 값을 비운다. clear()
print(my_dict)