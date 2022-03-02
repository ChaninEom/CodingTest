# my code

import sys

input = sys.stdin.readline()

price = int(input)
money = 1000
last_charge = money-price
num_charge = 0
charge_list = [500, 100, 50, 10, 5, 1]

for kind_charge in charge_list:
    if (last_charge ==0) or (kind_charge == 1):
        num_charge += last_charge
        break
    else:
        now_num, now_charge = last_charge//kind_charge, last_charge%kind_charge
        num_charge += now_num
        last_charge = now_charge

print(num_charge)



# top ranked code

# price = 1000 - int(input())
# coin = [500, 100, 50, 10, 5, 1]
# coinAmount = 0

# for i in coin :
#     coinAmount += price//i
#     price = price%i


# print(coinAmount)