def main():
    percent = get_fuel_capacity()
    print_fuel(percent)


def get_fuel_capacity():
    while True:
        fraction = input("Fraction: ").strip().split("/")

        # Ensure that, both the numerator and denominator exist.
        if not len(fraction) == 2:
            continue

        # Handle non-integral values (floating point values, alphabets etc) - value{string literal}
        try:
            num = int(fraction[0].strip())
            deno = int(fraction[1].strip())

        except ValueError:
            continue

        else:
            # Handle div by 0.
            if deno == 0:
                continue

            fraction = num/deno

            # Handle negative and improper fractions.
            if fraction < 0 or fraction > 1:
                continue

            # Return the percent fraction.
            return round(fraction*100)


def print_fuel(percent):
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")


if __name__ == "__main__":
    main()
