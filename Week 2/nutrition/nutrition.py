# Calorie chart
calorie_dict = {
        "apple":130,
        "avocado":50,
        "banana":110,
        "cantaloupe":50,
        "grapefruit":60,
        "grapes":90,
        "honeydew melon":50,
        "kiwifruit":90,
        "lemon":15,
        "lime":20,
        "nectarine":60,
        "orange":80,
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "sweet cherries":100,
        "tangerine":50,
        "watermelon":80
    }


def main():
    fruit = input("Item: ").strip().lower()
    calories_in(fruit)


def calories_in(fruit):
    for item in calorie_dict:
        # If fruit matches, print calories.
        if fruit == item:
            print(f"Calories: {calorie_dict[item]}")

        # Otherwise, do nothing.

if __name__ == "__main__":
    main()
