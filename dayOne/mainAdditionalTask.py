# Day Two
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

def add_callories(foodie):

    result = []
    current_sum = 0
    # biggest_sum = 0

    for item in foodie:
        if item == 0:
            result.append(current_sum)
            current_sum = 0
        else:
            current_sum += item
            # biggest_sum = max(biggest_sum, current_sum)
    # print(result)

    sorted_sum = sorted(result, reverse=True)

    print("Sorted sum of calories:", sorted_sum)

    print("Three greatest:", sorted_sum[0], sorted_sum[1], sorted_sum[2])

    day_two_solution = sorted_sum[0] + sorted_sum[1] + sorted_sum[2]

    print("Solution is:", day_two_solution)


if __name__ == '__main__':

    with open('/data.txt') as f:
        food = f.readlines()

        newfoodielist = []
        for single_food in food:
            if single_food == "\n":
                food_int = 0
            else:
                food_int = int(single_food)
            newfoodielist.append(food_int)

        add_callories(newfoodielist)




