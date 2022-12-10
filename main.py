
def add_callories(foodie):

    current_sum = 0
    biggest_sum = 0

    for item in foodie:
        if item == 0:
            current_sum = 0
        else:
            current_sum += item
            biggest_sum = max(biggest_sum, current_sum)
    print(biggest_sum)


if __name__ == '__main__':

    with open('./data.txt') as f:
        food = f.readlines()

        newfoodielist = []
        for single_food in food:
            if single_food == "\n":
                food_int = 0
            else:
                food_int = int(single_food)
            newfoodielist.append(food_int)

        add_callories(newfoodielist)




