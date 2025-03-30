def main():
    user = input("Enter text: ")
    print(shorten(user))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
    return word



if __name__ == "__main__":
    main()