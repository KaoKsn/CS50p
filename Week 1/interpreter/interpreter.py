def main():
    print(">>> ", end='')

    # Sanitize input.

    # 1. Whitespaces.
    expression = input().strip().split()
    _ = 0
    for value in expression:
        expression[_] = value.strip()
        _ += 1

    # Invalid Expression.
    if len(expression) != 3:
        return print("Invalid Expression, Form: x y z")

    # 2. Invalid Operator.
    if expression[1] not in ['+', '-', '*', '/']:
        return print("Use: [ + , - , *, /]")

    # 3. Invalid Operands.
    if not expression[0].isnumeric() or not expression[2].isnumeric():
        return print("Invalid Operand(s)")

    # 4. Division by 0.
    if expression[1] == '/' and expression[2] == '0':
        return print("Can't divide by 0")

    # Call interpreter on a valid expression.
    interpreter(expression)


def interpreter(expression):
    opr1, opr2 = float(expression[0]), float(expression[2])

    # Perform the related operation.
    match expression[1]:
        case '+':
            print(round(opr1+opr2, 1))
        case '-':
            print(round(opr1-opr2, 1))
        case '*':
            print(round(opr1*opr2, 1))
        case '/':
            print(round(opr1/opr2, 1))


if __name__ == "__main__":
    main()
