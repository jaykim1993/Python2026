# 리스트는 배열과 같은 역할을 한다.
# 동적이다(고정길이 x)
# 숫자 문자 혼합 사용가능

heroes = []

# 값 추가 : append(값) <- 맨 뒤로 
heroes.append("아이언맨")
# print(heroes)
heroes.append("닥터 스트레인지")
# print(heroes)

# 원하는 위치 지정 추가 : insert(index, 값)
heroes.insert(1, "스칼렛 위치")
# print(heroes)
# print(heroes[1])

# 값 삭제 : remove(삭제할 값)
# 인덱스번호로 삭제 : del 리스트[index]
# 마지막 값 삭제 : 리스트.pop()
heroes.remove("스칼렛 위치")
# print(heroes)
del heroes[0]
# print(heroes)
heroes.pop()
# print(heroes)

heroes = [ "아이언맨", "토르", "헐크", "스칼렛 위치", "스파이더맨", "아이언맨", "캡틴 아메리카" ]
# for문으로 출력하기
for name in heroes:
    print(name, end=" ") # 옆으로 출력하기
print()

# 슬라이스 하기
print(heroes[2:4]) # 2부터 4 직전까지
print(heroes[:3]) # 처음부터 3 직전까지
print(heroes[3:]) # 3부터 끝까지

# '토르'가 존재하면 삭제하고 출력
if '토르' in heroes:
    heroes.remove("토르")
    for name in heroes:
        print(name, end= " ")
    print()

# 정렬하기
heroes.sort()
heroes.sort(reverse=True)
print(heroes)