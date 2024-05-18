def convert(n):
    nameList=""
    for i in n:
        if i.islower():
            nameList+= i
        else:
            if i.isupper():
                nameList+="_"+i.lower()
    return nameList


def main():
    name=input("camelCase: ")
    snake_case_name=convert(name)
    print("snake_case: " + snake_case_name, end="")

if __name__=="__main__":
    main()  
