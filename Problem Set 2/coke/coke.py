def cokemachine():
    amount_due=50
    total_paid=0
    while True:
        if amount_due>0:
            print(f"Amount Due: {amount_due}")
            coin_input= int(input("Insert Coin: "))
            if coin_input in [5,10,25]:
                amount_due-=coin_input
                total_paid+=coin_input
        else:
            if total_paid>=50:
                print(f"Change Owed: {total_paid-50}")
                break




def main():
    cokemachine()


if __name__=="__main__":
    main()


