import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):

    '''
      Looks if each octet is a word boundary or not.
      1.1.1.1. - The first, second and third '1.' are followed by 1. \W to \w.
                while the last one has no \w to follow it.
    '''
    
    if re.search(r"^((\d|[1-9]\d|1\d\d|25[0-5]|2[0-4]\d)\.?\b){4}$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()

