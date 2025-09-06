# Assume the mass is entered as an integer.
def main():
    m = int(input("m (kg): "))
    converter(m)


def converter(m):
    c = 300000000
    E = m*pow(c, 2)
    print(E)


if __name__ == "__main__":
    main()
