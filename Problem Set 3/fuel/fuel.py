def get_fraction(prompt):
    while True:
        try:
            x, y = map(int, input(prompt).split("/"))
            percentage = (x / y) * 100

            if percentage <= 10:
                return "E"
            elif 90<= percentage <=100:
                return "F"
            elif percentage >100:
                continue
            else:
                return f"{round(percentage)}%"
        except (ValueError, ZeroDivisionError):
            print("Error: Please enter a valid fraction (x/y).")


def main():
    result = get_fraction("Fraction  ")
    print( result)


if __name__ == "__main__":
    main()
