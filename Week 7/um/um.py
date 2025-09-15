import re

# /b - word boundaries. (\w to \W or vice versa).

def main():
    try:
        print(count(input("Text: ")))
    except (KeyboardInterrupt, EOFError):
        print()


def count(text):
    text = text.strip().lower()
    return len(re.findall(r"\bum\b", text))


if __name__ == "__main__":
    main()
