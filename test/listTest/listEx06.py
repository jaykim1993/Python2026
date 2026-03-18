role_menus = {
'ADMIN' : ['대시보드', '회원관리', '상품관리', '주문관리', '통계', '시스템설정'],
'MANAGER': ['대시보드', '상품관리', '주문관리', '통계'],
'USER' : ['대시보드', '내정보', '주문내역'],
}
# 사용자 목록
users = [
{'name': '관리자김', 'role': 'ADMIN'},
{'name': '매니저박', 'role': 'MANAGER'},
{'name': '일반이', 'role': 'USER'},
{'name': '일반최', 'role': 'USER'},
]


for user in users:
    name = user["name"]
    role = user["role"]
    menus = role_menus[role] 
    print(f"{name} [{role}]")
    for menu in menus:
        print(f" - {menu}")
    print() 

target_menu = '통계'

print(f"[{target_menu}] 메뉴 접근 가능 사용자 목록:")

for user in users:
    role = user["role"]
   
    if target_menu in role_menus[role]:
        print(f"- {user['name']} ({role})")