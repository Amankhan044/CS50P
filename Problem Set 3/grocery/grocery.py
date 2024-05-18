def grocery():
    my_items = {}
    while True:
        try:
            item = input().upper().strip()
            if item:
                if item not in my_items:
                    my_items[item] = 1
                else:
                    my_items[item] += 1
            else:
                break
        except EOFError:
            break  
    sorted_dict = dict(sorted(my_items.items()))
    for item, count in sorted_dict.items():
        print(count, item)

def main():
    grocery()

if __name__ == "__main__":
    main()
