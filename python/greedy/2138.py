# mycode
import sys

num = int(sys.stdin.readline())
status = list(map(int, sys.stdin.readline().rstrip()))
target = list(map(int, sys.stdin.readline().rstrip()))
status_tmp = status.copy()
raw_target = ''.join(list(map(str, target)))
def first_try():
    calc = 0
    for i in range(1, num):
        if status[i-1] != target[i-1]:
            status[i-1] = 1-status[i-1]%2
            status[i] = 1-status[i]%2
            if i != num-1:
                status[i+1] = 1-status[i+1]%2
            calc += 1
    return ''.join(list(map(str, status))), calc

def second_try():
    calc = 1
    status = status_tmp
    status[0], status[1] = 1-status[0]%2, 1-status[1]%2
    for i in range(1, num):
        if status[i-1] != target[i-1]:
            status[i-1] = 1-status[i-1]%2
            status[i] = 1-status[i]%2
            if i != num-1:
                status[i+1] = 1-status[i+1]%2
            calc +=1
    return ''.join(list(map(str, status))), calc

result, calc = first_try()
if result == raw_target:
    print(calc)
else:
    result, calc = second_try()
    if result == raw_target:
        print(calc)
    else:
        print(-1)


# top tear code
# n = int(input())
# data = list(str(input()))
# d = data[:]
# t = list(str(input()))
# ans = 0

# for i in range(1, n):
#     if d[i-1] != t[i-1]:
#         d[i-1] = '1' if d[i-1] == '0' else '0'
#         d[i] = '1' if d[i] == '0' else '0'
#         if i + 1 < n:
#             d[i+1] = '1' if d[i+1] == '0' else '0'
#         ans += 1

# if ''.join(d) == ''.join(t):
#     print(ans)
# else:
#     d = data
#     ans = 1
#     d[0] = '1' if d[0] == '0' else '0'
#     d[1] = '1' if d[1] == '0' else '0'

#     for i in range(1, n):
#         if d[i-1] != t[i-1]:
#             d[i-1] = '1' if d[i-1] == '0' else '0'
#             d[i] = '1' if d[i] == '0' else '0'
#             if i + 1 < n:
#                 d[i+1] = '1' if d[i+1] == '0' else '0'
#             ans += 1
#     if ''.join(d) == ''.join(t):
#         print(ans)
#     else:
#         print(-1)