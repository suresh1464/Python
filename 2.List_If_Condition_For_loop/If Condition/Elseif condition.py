India = ["samosa","dall","naan"]
Chinese = ["egg role","pot sticker","fried rice"]
Italian = ["pizza","pasta","risotto"]
dish = input("enter your dish : ")

if dish in India:
    print(f"{dish} is in India")
elif dish in Chinese:
    print(f"{dish} is in Chinese")
elif dish in Italian:
    print(f"{dish} is in Italian")
else:
    print(" I dont know which cusine")

