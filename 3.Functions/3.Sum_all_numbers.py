def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

Total1 = sum_all(1,2,3,4,5,6)
total2 = sum_all(1,2,3,4,5,6,7)
total3 = sum_all(1,2,3,4,5,6,7,8)
print(Total1)
print(total2)
print(total3)