def company_info(**kwargs):
    for key in kwargs:
        print(key,kwargs[key])

company_info(ticker = "Apple",CEO = "Tim Cook",revenue = "200 Billion")
company_info(ticker = "Apple",CEO = "Tim Cook",revenue = "200 Billion",pe =20)