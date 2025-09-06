def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = dollars * percent

    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    p = float(p.replace("%", ""))
    if 0 <= p <= 100:
        p = p/100
        return round(p, 2)
    else:
        p = input("What percentage would you like to tip? ")
        return percent_to_float(p)


if __name__ == "__main__":
    main()
