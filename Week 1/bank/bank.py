def main():
    greeting = input("Greeting: ").strip().lower()
    payback(greeting)


# $0 even for "hello, foo"
def payback(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif "h" == greeting[0]:
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()
