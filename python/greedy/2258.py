import sys
input = sys.stdin.readline

N, M = map(int, input().split())
meet_list = []
now_price = 0
now_pound = 0
for i in range(N):
    meet_list.append(list(map(int, input().split())))
meet_list.sort(key = lambda x:(x[1], -x[0]))
print(meet_list)

for pound, price in meet_list:
    now_pound+=pound
    now_price+=price
    if now_pound >= M:
        if price<now_price:
            now_price = price
        break
if now_pound <M:
    now_price = -1

print(now_price)
print(now_pound)