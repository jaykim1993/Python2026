# 기준 날짜 (연체 확인용)
today = '2025-06-10'
# 도서 목록
books = [
{'id':'B001','title':'파이썬 완전정복','author':'홍길동','genre':'IT','total':3,'available':2},
{'id':'B002','title':'데이터분석 입문','author':'김데이','genre':'IT','total':2,'available':2},
{'id':'B003','title':'알고리즘의 이해','author':'이알고','genre':'IT','total':2,'available':1},
{'id':'B004','title':'채식주의자 완성','author':'한강','genre':'소설','total':4,'available':4},
{'id':'B005','title':'82년생 김지영의','author':'조남주','genre':'소설','total':3,'available':3},
]
# 대출 기록
borrows = [
{'borrow_id':'B-001','member':'박지수','book_id':'B003','borrow_date':'2025-05-20','due_date':'2025-06-03','returned':False},
{'borrow_id':'B-002','member':'최우진','book_id':'B001','borrow_date':'2025-05-25','due_date':'2025-06-08','returned':False},
]

# ================== 함수 목록 ================== 

# 도서 목록 조회
def show_books():
    print("=================================================================================================")
    print("도서ID\t\t 제목\t\t\t 저자\t\t 장르\t\t 전체\t 가능\t 상태\t")
    print("-------------------------------------------------------------------------------------------------")
    for book in books:
            if book["available"] == 0: availText = "대출불가"
            else : availText = "대출가능"
            print(f"{book['id']}\t\t {book['title']}\t {book['author']}\t\t {book['genre']}\t\t {book['total']}\t {book['available']}\t {availText}")
    print("=================================================================================================\n")
    return

# 도서 대출
def borrow_book(member, book_id):
    global today
    # borrow_id 값 만들기
    new_borrow_id = f"B-00{len(borrows)+1}"
    borrows.append({'borrow_id':new_borrow_id,'member':member,'book_id':book_id,'borrow_date':today,'due_date':'2025-06-24', 'returned':False})
    print(f"{inputName} 님이 '{bookInfo['title']}' 을(를) 대출되었습니다.")
    return

# 도서 반납
isReturn = False
def return_book(borrow_id):
    global isReturn
    bookId = ""
    for borrow in borrows:
        if borrow_id == borrow['borrow_id'] and borrow['returned'] == False:
            bookId = borrow['book_id']
            borrow['returned'] = True
            isReturn = True
        elif borrow_id == borrow['borrow_id'] and borrow['returned'] == True:
            print("이미 반납된 도서입니다.")
    if isReturn:
        for book in books:
            if bookId == book['id']:
                book['available'] += 1
                print(f"\n[반납 완료] '{book['title']}' 이(가) 반납되었습니다.")
    else:
        print("해당 대출 기록이 없습니다.")
    return 

# 대출 현황 조회
def show_borrows():
    print("=================================================================================================")    
    print("대출번호\t 회원명\t\t 도서제목\t\t 대출일\t\t 반납예정일\t 반납여부")
    print("-------------------------------------------------------------------------------------------------")
    for borrow in borrows:
        if borrow['returned']: returnText = "반납완료"
        else: returnText = "대출중"
        for book in books:
            if borrow['book_id'] == book['id']:
                bookTitle = book['title']
        print(f"{borrow["borrow_id"]}\t\t {borrow['member']}\t\t {bookTitle}\t {borrow['borrow_date']}\t {borrow["due_date"]}\t {returnText}")
    print("=================================================================================================")
    return

# 연체 현황 조회
def show_overdue():
    global today
    print(f"\n연체현황 (기준일: {today})")
    print("===================================================================")
    print("대출번호\t 회원명\t\t 도서제목\t\t 반납예정일")
    print("-------------------------------------------------------------------")
    for borrow in borrows:
        if borrow['due_date'] < today:
            for book in books:
                if borrow['book_id'] == book['id']:
                    bookTitle = book['title']
            print(f"{borrow["borrow_id"]}\t\t {borrow['member']}\t\t {bookTitle}\t {borrow["due_date"]}")
    print("===================================================================")
    return

# 장르별 통계
def show_genre_stats():
    print("===============================")
    print("장르\t 전체권수\t 대출중\t")
    print("-------------------------------")
    ITs = []
    fictions = []
    returnCntIT = 0
    returnCntFiction = 0
    for book in books:
        if book['genre'] == 'IT': ITs.append(book)
        if book['genre'] == '소설': fictions.append(book)
    for borrow in borrows:
        for book in ITs:
            if borrow['book_id'] == book['id'] and borrow['returned'] == False:
                returnCntIT += 1
        for book in fictions:
            if borrow['book_id'] == book['id'] and borrow['returned'] == False:
                returnCntFiction += 1
    print(f"IT\t {len(ITs)}\t\t {returnCntIT}")
    print(f"소설\t {len(fictions)}\t\t {returnCntFiction}")
    print("===============================")
    return

# 뒤로가기 함수
def backMenu():
    back = input("\n뒤로가기 - ENTER")
    print()




# ================== 실행 프로그램 ================== 

while True:
    print("=== 도서관 대출 관리 시스템 ===")
    print("   1. 도서 목록 조회")
    print("   2. 도서 대출")
    print("   3. 도서 반납")
    print("   4. 대출 현황 조회")
    print("   5. 연체 현황 조회")
    print("   6. 장르별 통계")
    print("   0. 종료")
    option = input("메뉴를 선택하세요: ")
    if option == "1":
        print("\n도서 목록 조회")
        while True:
            show_books()
            backMenu()
            break
    elif option == "2":
        print("\n도서 대출")
        show_books()
        while True:
            inputName = input("회원명을 입력하세요: ")
            while True:
                inputBookID = input("대출할 도서ID를 입력하세요 : ").upper()
                bookInfo = None
                for book in books:
                    if book['id'] == inputBookID:
                        bookInfo = book
                        break
                if bookInfo is None:
                    print("등록되지 않은 도서입니다.")
                elif bookInfo['available'] == 0:
                    print("현재 대출 가능한 도서가 없습니다.")
                else:
                    bookInfo['available'] -= 1
                    borrow_book(inputName, inputBookID)
                    break
            backMenu()
            break        
    elif option == "3":
        print("\n도서 반납")
        while True:
            while True:
                inputBorrowID = input("대출번호를 입력하세요: ").upper()
                return_book(inputBorrowID)
                if isReturn:
                    break
            backMenu()
            break
    elif option == "4":
        print("\n대출 현황 조회")
        show_borrows()
        while True:
            backMenu()
            break
    elif option == "5":
        show_overdue()
        while True:
            backMenu()
            break
    elif option == "6":
        print("\n장르별 통계")
        show_genre_stats()
        while True:
            backMenu()
            break
    elif option == "0":
        print("프로그램을 종료합니다.")
        break