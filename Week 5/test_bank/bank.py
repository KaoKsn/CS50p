def main():
    greeting = input("Greeting: ")
    print(value(greeting))


# $0 even for "hello, foo"
def value(greeting):
    # Maintain uniformity and sanitize any whitespaces
    greeting = greeting.strip().lower()

    # Ensure greetings exists.
    if greeting:
        if greeting.startswith("hello"):
            return "$0"
        elif "h" == greeting[0]:
            return "$20"
        else:
            return "$100"


if __name__ == "__main__":
    main()
