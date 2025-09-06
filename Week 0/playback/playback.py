# Get user input.
str = input("Input String: ").strip()

fstr = ""

# Handle multiple whitespaces in the middle.
for value in str.split():
    if fstr != "":
        fstr = fstr + " " + value
    else:
        fstr = value

fstr = fstr.replace(" ", "...")

# Print the output
print(fstr)
