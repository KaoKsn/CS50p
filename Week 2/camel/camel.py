def main():
    # Assume camelCase is provided.
    name = input("camelCase: ").strip()
    print(f"snake_case: {snake_case(name)}")


def snake_case(name):
    words = []
    part = ""

    # Create a list of words from the camelCase.
    for char in name:
        # If capital letter encountered.
        if char.isupper():
            words.append(part + "_")
            # Reinitialize word.
            part = char.lower()
        # Develop word.
        else:
            part += char
    # Add the last word.
    words.append(part)

    # Generate the snake_case name.
    snake_case_name = ""
    for word in words:
        snake_case_name += word
    
    return snake_case_name


if __name__ == "__main__":
    main()
