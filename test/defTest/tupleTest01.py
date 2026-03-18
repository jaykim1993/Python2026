# 튜플 : 여러개의 데이터를 순서대로 저장하며
    # 수정, 삭제, 추가 안됨
    # 사용법 : a = (10, 20, 30) or 10, 20, 30
    # 접근 : a[0]
    # 함수 내에서 리턴값이 여러개일때,
    # 튜플에 담아서 내보내면 좋다.
score = (90, 85, 100)
print(score)
# score[1] = 80 <- 수정하려하면 오류남
print(score[1])

fruits = ('apple', 'banana', 'orange')
for fruit in fruits:
    print(fruit , end=" ") # 가로 출력
    # print(fruit) 세로 출력
print()

if 'banaa' in fruits:
    print("존재함")
else:
    print("존재안함")

t = 10, 20, 30
print(t)

# 문제 : 주어진 자료를 이용하여 합계, 평균 구하기
scores = (80, 50, 75, 90)
sum = 0
for score in scores:
    sum += score
print("합계 : ", sum)
avg = int(sum/len(scores))
print("평균 : ", avg)