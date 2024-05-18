def total_cost(prompt):
    total_item_costs=0
    menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
   }

    while True:
        try:
            item = input(prompt).title().strip()
            total_item_costs +=menu[item]
            print(f"Total: ${total_item_costs:.2f}")
        except EOFError:
            print("\n")
            break
        except KeyError:
            pass

def main():
    total = total_cost("Item: ")
    print( total)


if __name__ == "__main__":
    main()
