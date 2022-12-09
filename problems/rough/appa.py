from icecream import ic
rent = 0.28*12
total = 0.28*12

for i in range(0, 34):
    new_rent = rent + rent/10
    total += new_rent
    rent = new_rent
    ic(rent, total)

ic(total, rent)


