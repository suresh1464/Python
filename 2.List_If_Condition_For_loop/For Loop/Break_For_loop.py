monthly_sales = [42,38,33,38,40,45]

threshold = 35

for sales in monthly_sales:
    if sales <= threshold:
        print(f"Sales amount: {sales} is less that threshold: {threshold}")
        break
    else:
        print(f"Sales amount: {sales} is greater than threshold: {threshold}")
