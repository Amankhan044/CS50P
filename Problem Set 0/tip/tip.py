
def dollars_to_float(d):
    if d.startswith("$"):
         my_dollar=d[1:-1]
         return float(my_dollar)
    else:
        return d[:-1]



def percent_to_float(p):
     my_percentage=float(p[:-1])
     my_percentage= my_percentage/100
     return float(my_percentage)

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    print(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    print(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


if __name__ == "__main__":
    main()
