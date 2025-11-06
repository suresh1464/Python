monthly_sales = [42,38,33,38,40,45]
months = ["Jan","Feb","Mar","Apr","May","Jun"]
threshold = 35
for sale_amount,month in zip(monthly_sales,months):
    if sale_amount < threshold:
        print(f"Sales amount {sale_amount} is less than threshold {threshold}")
        break
    else:
        print(f"Sales amount {sale_amount} is greater than threshold {threshold}")
