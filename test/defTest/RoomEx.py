rooms = [
    {"room_id":101, "name":"스탠다드A", "price":100000, "maxOccupancy":2, "status":True},
    {"room_id":102, "name":"스탠다드B", "price":120000, "maxOccupancy":2, "status":True},
    {"room_id":103, "name":"스탠다드C", "price":150000, "maxOccupancy":3, "status":True},
    {"room_id":201, "name":"디럭스A\t", "price":200000, "maxOccupancy":4, "status":True},
    {"room_id":202, "name":"디럭스B\t", "price":250000, "maxOccupancy":4, "status":True},
    {"room_id":203, "name":"디럭스C\t", "price":300000, "maxOccupancy":4, "status":True},
    {"room_id":301, "name":"럭셔리A\t", "price":400000, "maxOccupancy":5, "status":True},
    {"room_id":302, "name":"럭셔리B\t", "price":450000, "maxOccupancy":5, "status":True},
    {"room_id":303, "name":"스위트룸", "price":500000, "maxOccupancy":6, "status":True},
    ]
reservations = []
bookPossibleRoom = []
maxPeople = 0
    
# 전체 객실 목록을 출력합니다. 
def show_rooms(only_available):
    print("\n=================================================================")
    print("ID\t객실명\t\t가격\t\t최대인원\t상태")
    print("-----------------------------------------------------------------")
    global rooms, bookPossibleRoom
    if only_available:
        for room in rooms:
           if room["status"]:
               print(f"{room["room_id"]}\t{room["name"]}\t{room["price"]:,}\t\t{room["maxOccupancy"]}\t\t{room_status(room["status"])}")
               bookPossibleRoom.append(room["room_id"])
    else:
        for room in rooms:
            print(f"{room["room_id"]}\t{room["name"]}\t{room["price"]:,}\t\t{room["maxOccupancy"]}\t\t{room_status(room["status"])}")
    print("=================================================================\n")
    return

# 해당 방이 예약 가능한지 확인
def make_reservation(res_list, room_id, guest_name, people, days):
    global rooms
    # 예약 목록 탐색
    # 예약 목록 추가
    # 객실 상태 변경
    for room in rooms:
        if room_id == room["room_id"]:
            room["status"] = False
    res_list.append((guest_name, room_id, people, days))
    print(f"    [성공] {guest_name}님, {room_id}호 예약이 완료되었습니다.\n")


# 예약 목록에서 해당 방의 예약을 삭제
def cancel_reservation(res_list, room_id):
    for room in rooms:
        if room_id == room["room_id"]:
            room["status"] = True
            print("해당 예약이 삭제되었습니다.\n")
            for book in res_list:
                if room_id == book[1]:
                    res_list.remove(book)
    return

# 방 상태 한글 변환
def room_status(rs):
    if rs:
        status = "예약가능"
    else:
        status = "예약불가"
    return status

# 뒤로가기
def backMenu():
    back = input("뒤로가기 - ENTER")
    print()


# 방 ID와 숙박일수, 인원수를 입력받아 
# 총액을 계산하여 반환
def calculate_price(room_id, days, people):
    global rooms, maxPeople
    price = 0
    for room in rooms: 
        if room_id == room["room_id"] and people > room["maxOccupancy"]:
            price = room["price"] * days + 20000*(people-room["maxOccupancy"])
        elif room_id == room["room_id"]:
            price = room["price"] * days
    return price

while True:
    print("--- 리조트 예약 관리 시스템 ---\n")
    print("    1. 객실 현황보기")
    print("    2. 객실 예약하기")
    print("    3. 예약 내역 및 매출 확인")
    print("    4. 프로그램 종료\n")
    print("------------------------------")
    option = int(input("원하는 메뉴 번호를 선택하세요: "))

    if option == 1:
        while True:
            show_rooms(False)
            while True:
                print("1. 객실 추가")
                print("2. 객실 수정")
                print("3. 객실 삭제")
                print("뒤로가기 - ENTER\t")
                option = input("원하는 메뉴 번호를 선택하세요: ")
                if option == "1":
                    print("추가 접근")
                elif option == "2":
                    print("추가 접근")
                elif option == "3":
                    print("추가 접근")
                else:
                    break
            backMenu()
            break
    elif option == 2:
        while True:
            show_rooms(True)
            while True:
                room_id = int(input("예약할 객실 ID를 입력하세요: "))
                if room_id in bookPossibleRoom: break
                else : 
                    print("해당 객실은 예약 불가합니다.")
                    continue
            guest_name = input("예약자 성함을 입력하세요: ")
            for room in rooms:
                if room_id == room["room_id"]:
                    maxPeople = room["maxOccupancy"]
            people = int(input(f"투숙 인원을 입력하세요 (최대 {maxPeople}명): "))
            days = int(input("숙박 일수를 입력하세요: "))
            make_reservation(reservations, room_id, guest_name, people, days )
            maxPeople = 0
            break
    elif option == 3:
        while True:
            print("--- 전체 예약 명단 ---")
            totalPrice = 0
            if len(reservations) == 0:
                print("현재 예약이 존재하지 않습니다.")
            else: 
                for guest_name, room_id, people, days in reservations:
                    bookPrice = calculate_price(room_id, days, people)
                    totalPrice += bookPrice
                    print(f"성함: {guest_name} | 객실번호: {room_id}호 | 인원: {people}명 | 숙박일수: {days}박{days+1}일 | 금액: {bookPrice:,}원")
                print(f"현재 확정 매출 합계: {totalPrice:,}원\n")
                while True:
                    print("1. 예약삭제")
                    print("뒤로가기 - ENTER\t")
                    option = input("원하는 메뉴 번호를 선택하세요: ")
                    if option == "1":
                        inputID = int(input("삭제할 방 번호를 입력하세요.: "))
                        cancel_reservation(reservations, inputID)
                        backMenu()
                        break
                    else:
                        break
            break
    elif option == 4:
        print("    프로그램을 종료합니다. 수고하셨습니다!")
        break

