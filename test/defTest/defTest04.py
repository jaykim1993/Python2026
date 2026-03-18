# 파이썬의 함수는 return 여러개 받을 대
# -> 튜플 사용
# 예제
# 값 2개 입력받아서 더하기

def cal(a, b):
    sum_def = a + b
    diff_def = a - b
    return (sum_def, diff_def) # 튜플

resultA, resultB = cal(10, 5) # 여러 개의 값 받을때 변수 선언 여러개 하면 각각 담김
print(f"합: {resultA}, 차: {resultB}")