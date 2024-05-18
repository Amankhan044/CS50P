def omitted(s):
    omitted_str = ''
    for i in s:
        if i.isupper() and i in "AEIOU":
            continue  # Skip uppercase vowels
        elif i.islower() and i in "aeiou":
            continue  # Skip lowercase vowels
        else:
            omitted_str += i  # Append character if not a vowel
    return omitted_str  # Return the modified string


def main():
    user_input = input("enter a string of text: ")
    omitted_text = omitted(user_input)
    print(omitted_text)


if __name__ == "__main__":
    main()
