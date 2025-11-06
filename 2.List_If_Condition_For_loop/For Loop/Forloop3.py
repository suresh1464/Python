Expense = [1200,1300,1400,1500,1600]
total_expense = 0
for i,expense in enumerate(Expense):
    print(f"Month {i+1}, Expense {expense}")
    total_expense += expense
print("Total Expense = ", total_expense)