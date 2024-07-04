def solution(year):
    
    if year%4==0:
        if year%100!=0 or year%400==0:
            answer=1
        else:
            answer=0
    else:
        answer=0

    return answer

result=solution(2012)
print(result)