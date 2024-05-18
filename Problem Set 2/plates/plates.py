
def calories_counter(cal):
    fruit_calories={
        "Apple": 130,
        "Avocado":50 ,
        "Banana": 110,
        "Cantaloupe":50 ,
        "Grapefruit":60 ,
        "Grape":90 ,
        "Honeydew": 50,
        "Kiwifruit":90 ,
        "Lemon":15 ,
        "Lime": 20,
        "Nectarine":60 ,
        "Orange":80 ,
        "Peach": 60,
         "Pear": 100,
       "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }

    for k in fruit_calories:
        if k.lower()==cal.lower():
            print(f"Calories: {fruit_calories[k]}")
            return

        print("invalid fruit name")





def main():
    fruit_name=input("Item: ")
    calories_counter(fruit_name)



if __name__=="__main__":
    main()    
