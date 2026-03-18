menus = {"아메리카노": 3000, "라떼": 3500, "에이드": 4000}




def order_coffee(name, qty=1):
    global menus
    if name in menus:
        print(f"{name} {qty}잔 주문 완료. 총액: {menus[name]:,}원")
    else:
        print(f"죄송합니다. {name} 메뉴는 준비되어 있지 않습니다.")
    return

order_coffee("아메리카노")
order_coffee("라떼", 3)
