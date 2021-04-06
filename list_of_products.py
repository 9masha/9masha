from os import system
from math import ceil
user_number = ["exit", "show menu", "the cheapest", "the most expensive", "find the product in menu"]
products = [
    {"Name": "Salad", "price": 25.00},
    {"Name": "Soup", "price": 15.00},
    {"Name": "Bread", "price": 5.00},
    {"Name": "Kebab", "price": 50.00},
    {"Name": "Pizza", "price": 100.00},
]
page = 0
per_page = 2
last_page = ceil(len(products)//per_page)
while True:
    system("cls")
    print()
    for i in range(len(user_number)):
        print(i, user_number[i])
    message = int(input("Enter the number:"))

    if message == 0:
        break
    if message == 1:
        while True:
            system("cls")
            print()
            print("#"*15, "MENU", "#"*15)
            for i in range(page * per_page, page * per_page + per_page):
                try:
                    print(f' {i+1} > {products[i]["Name"]:20} {products[i]["price"]:5}')
                except:
                    pass

            for x in range(last_page + 1):
                if x == page:
                    print("[", x + 1, "]", end=" ")
                else:
                    print(x + 1, end=" ")
            print("\n")
            page_change = input('enter "p" to change page number "<" / ">"  to go to the prev / next page  "x" to exit')
            if page_change == "<" and page >= 1:
                page -= 1
            if page_change == ">" and page < last_page:
                page += 1
            if page_change == "p":
                page = (int(input("What page would you like to go to? ")) - 1)
            if page_change == "x":
                break

    if message == 2:
        system("cls")
        print("#" * 15, "Min Price", "#" * 15)
        min_i = 0
        for i in range(len(products)):
            if products[i]["price"] < products[min_i]["price"]:
                min_i = i
        print(f' {min_i} > {products[min_i]["Name"]:20} {products[min_i]["price"]:5}')

    if message == 3:
        system("cls")
        print("#" * 15, "Max Price", "#" * 15)
        max_i = 0
        for i in range(len(products)):
            if products[i]["price"] > products[max_i]["price"]:
                max_i = i
        print(f' {max_i} > {products[max_i]["Name"]:20} {products[max_i]["price"]:5}')

    if message == 4:
        system("cls")
        name_find = input("What product are you looking for?(Salad, Soup, Bread, Kebab, Pizza)")
        i = -1
        print("#" * 10, "You looked for:" + name_find, "#" * 10)
        try:
            for product in products:
                i += 1
                for name in product.values():
                    if name == name_find:
                        print(f' {i} > {products[i]["Name"]:20} {products[i]["price"]:5}')
        except:
            print("Sorry we do not have this product at the moment")


