import re


def main():
    print(parse(input("HTML: ").strip()))


def parse(tag):
    if url := re.search(r'^.+\bsrc="(?:https?://(?:www\.)?youtube\.com/embed/(\w+))".+$', tag):
        return f"https://youtu.be/{url.group(1)}"

        ''' Also can be done this way:
                        return re.sub(r'https?://(?:www\.)?youtube\.com/embed', "https://youtu.be", url.group(1))
        '''

    else:
        return None


if __name__ == "__main__":
    main()
