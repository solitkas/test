def Number_Guessing():
    import random
    n = random.randint(1, 10)
    guess = int(input("Enter any number: "))
    while n != guess:
        if guess > n:
            print("To high")
            guess = int(input("Enter number again: "))
        if guess < n:
            print("To low")
            guess = int(input("Enter number again: "))
        else:
            break
    print("you win")


if __name__ == "__main__":
    Number_Guessing()
