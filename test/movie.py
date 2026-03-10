cinema_name = "PYTHON CINEMA"
ticket_num = "2026-0309-01"
room_info = "7관 (4층)"
movie_name = "파이썬의 습격"
running_time = "14:30 ~ 16:10"

adult, p_adult, q_adult = "일반 성인", 15000, 2
teen, p_teen, q_teen = "청소년", 10000, 1

amt_adult = p_adult * q_adult
amt_teen = p_teen * q_teen

total = amt_adult + amt_teen

print("=" * 60)
print(f"{cinema_name:^60}")
print("=" * 60)
print(f"티켓번호 : {ticket_num}")
print(f"상영관   : {room_info}")
print(f"영화명   : {movie_name}")
print(f"상영시간 : {running_time}")
print("-" * 60)
print(f"{'구분':<20} {'단가':<12} {'인원':>5} {'금액':>12}")
print("-" * 60)
print(f"{adult:<16} {p_adult:<16,} {q_adult:>7} {amt_adult:>14,}")
print(f"{teen:<17} {p_teen:<16,} {q_teen:>7} {amt_teen:>14,}")
print("=" * 60)
print(f"{'총 결제 금액':<40} {total:>14,}")
print("=" * 60)