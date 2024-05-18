def convert(text):
    return text.replace(":)", "🙂").replace(":(","🙁")

def main():
    user_input = input("Input your text: ")
    converted=convert(user_input)
    print(converted)

if __name__ == "__main__":
    main()

