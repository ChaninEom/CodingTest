# mycode
num_teams = int(input())

skill_score_list = list(map(int, input().split()))
skill_score_list.sort()
min_score = skill_score_list[0]+skill_score_list[-1]

for i in range(num_teams-1):
    now_score = skill_score_list[i+1]+skill_score_list[-(i+2)]
    if (now_score < min_score): min_score = now_score
print(min_score)

# top tear code

# n=int(input())
# d=sorted(list(map(int, input().split())))
# r=[d[i]+d[2*n-1-i] for i in range(n)]
# print(min(r))