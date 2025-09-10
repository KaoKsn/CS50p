import requests
import sys


def main():
    # Ensure appropriate command line arguments are given.
    arg_length = len(sys.argv)

    if arg_length == 1:
        sys.exit("Missing command-line argument")

    elif arg_length == 2:
        n = get_number(sys.argv[1])
        current_value(n)

    else:
        sys.exit("Format: python bitcoin.py <non-negative integer value>")


def get_number(ip):
    # Ensure 'n' can be converted to a floating point value.
    try:
        ip = float(ip)
    except ValueError:
        sys.exit("Command-line argument is not a number")

    return ip


def current_value(n):
    # API request url.
    url = "dummy"

    try:
        request = requests.get(url)

    except requests.RequestException:
        sys.exit("Sorry, couldn't fetch results this time")

    else:
        # Get the current USD value of bitcoin as a floating value.
        unit_price = float(request.json()["data"]["priceUsd"])

        # Print the total value upto 4 decimal digits with a thousands seperator.
        print(f"${unit_price * n:,.4f}")


if __name__ == "__main__":
    main()
