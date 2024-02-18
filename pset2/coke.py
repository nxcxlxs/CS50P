price = 50

while price > 0:
# while (price := (price - coin)) > 0:

    print("Amount Due:", price)
    coin = int(input("Insert Coin: "))
        match coin:
            case 25 | 10 | 5:
                break
            case _:
                print("Amount Due:", price)

    price -= coin

    if price == 0:
        print("Change Owed: 0")

    elif price < 0:
        print("Change Owed:", price*-1)
# if price <= 0:
    # print("Change Owed:", abs(price))

