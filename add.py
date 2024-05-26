from validation import is_valid_input, is_valid_choice


def add(client, models):
    add_q = int(
        input(
            "do you want to add a client or a model? press '1' for client and '2' for models"
        )
    )
    if not is_valid_choice(add_q, 2):
        print("pick a number in range of 1-2")
    if add_q == 1:
        client_q1 = input("what is your name?")
        client_q2 = input("what is your car firm?")
        client.append([client_q1, client_q2])

    else:
        car_info1 = input("what is your car modle?")
        try:
            car_info2 = int(
                input("What is the year of your car manufacture date (numbers only)?")
            )
        except ValueError:
            print("That's not a valid year. Please enter a number.")
            return
        car_info3 = input("what is your car color?")
        models.append([car_info1, car_info2, car_info3])
