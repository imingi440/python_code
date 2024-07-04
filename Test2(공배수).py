def solution(number, n, m):
    
    if number%n==0 and number%m==0:
        answer=1
    else:
        answer=0
    return answer

result= solution(60,2,3)
print(result)

result= solution(55,5,10)
print(result)

result= solution(24,3,10)
print(result)

result= solution(24,3,8)
print(result)