import random
def main():
    #class
    weeks = 16
    print(weeks, type(weeks))

    classes = 5
    print(classes, type(classes))

    tuition = 6000
    print(tuition, type(tuition))

    cost_per_week = (tuition / classes) / weeks
    print(cost_per_week, type(cost_per_week))

    classes_per_week = 3
    print(classes_per_week, type(classes_per_week))

    cost_per_class = cost_per_week / classes_per_week
    print(cost_per_class, type(cost_per_class))

    print("The cost per class is:", cost_per_class)

    # foods
    favorite_foods = ["pizza", "burgers", "sushi", "tacos", "pasta"]
    print(favorite_foods, type(favorite_foods))

    random_food = random.choice(favorite_foods)
    print(random_food, type(random_food))

    print("The randomly selected food is:", random_food)
main()