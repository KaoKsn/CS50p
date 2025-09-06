def main():
    str = input("Enter String: ").strip()
    convert(str)


def convert(str):
    str = str.replace(":)", "🙂").replace(":(", "🙁")
    print(str)


if __name__ == "__main__":
    main()
