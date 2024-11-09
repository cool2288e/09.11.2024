with open("quotes.txt", "r", encoding="utf-8") as sigma:
    data =sigma.read()


print(data)

answer = input("Напиши своє прізвище")

with open("quotes.txt", "a", encoding="utf-8") as sigma:
    sigma.write("\n + answer")
with open("quotes.txt", "r", encoding="utf-8") as sigma:
    data =sigma.read()


print(data)

