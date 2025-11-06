def find_total(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total
'''
:param expenses: input list of expenses in integer format
:return: total expenses Suri
'''
expenses_suri = [30,45,70,90]
expenses_aaru = [40,23,10,85]

total_expenses_Suri = find_total(expenses_suri)
total_expenses_Aaru = find_total(expenses_aaru)
print("Total expenses Suri: ", total_expenses_Suri)
print("Total expenses Aaru: ", total_expenses_Aaru)