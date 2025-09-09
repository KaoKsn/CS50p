from emoji import emojize

def main():
    str = input("Input: ").strip().lower()
    print(f"Output: {emojize(str, language = "alias")}")

if __name__ == "__main__":
    main()

