def main():
    str = input("Input: ").strip()
    twttrify(str)

def twttrify(str):
    twttr_str = ""

    for char in str:
        # Avoid vowels in the string.
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            continue
        else:
            twttr_str += char

    # Print the twttrified string.
    print(f"Output: {twttr_str}")


if __name__ == "__main__":
    main()
