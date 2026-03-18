# 함수안에서 전역변수 사용하기

def cal_area(radius):
    global area # 전역변수 사용하기 위해 global 붙여서 선언
    area = 3.14 * radius ** 2
    return
    
area = 0 # area 전역 , 초기값 선언
r = float(input("반지름 입력: "))
cal_area(r)
print(area)