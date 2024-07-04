def solution(a, b, flag):
    result=0
    if flag==True:
        result = a+b
    else:
        result = a-b
    return result
    

print(solution(-4, 7, True))

print(solution(-4, 7, False))