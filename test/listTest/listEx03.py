orders = [
{'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
{'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
{'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
{'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
{'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'}
]
amount = 0
paid = []

for order in orders:
    if order['status'] == "PAID":
        paid.append(order)

for order in paid:
    print(f"{order['id']} 번 주문 / 상품: {order['product']} / 금액: {order['amount']:,}원")
    amount += order['amount']
print(f"\n총 결제 금액: {amount:,}원")



