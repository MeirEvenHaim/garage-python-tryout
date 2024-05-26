from display_Methodes import display_C, display_M
from validation import is_valid_input


# Main update function
def update(clients, models):
    print(
        "1. Update a client"
    )  # directs the user to the client update function directory update_client(index)
    print(
        "2. Update a model"
    )  # directs the user to the model update function update_model(index)
    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("That's not a valid choice. Please enter a number.")
        update(clients, models)

    ## add validation
    # Get user choice
    if not is_valid_input(user_choice, 2):
        print("Pick either 1 or 2")
    # Update a client
    if (
        user_choice == 1
    ):  # cy choosing 1 the user will get the client list printed and from it it will need to pick an index by puting an index input the    update_client(index) finction will get activiated effectively updating the list
        display_C(clients)
        index = int(
            input("Which client would you like to update? Enter the index: ")
        )  # an integer input to pick an index inside the client list
        update_client(
            index, clients
        )  # takes the index integer the user picked and apllying it tot he update client function
    # Update a model
    elif user_choice == 2:
        # same way as picking 1 but on the model list.
        display_M(models)
        index = int(input("Which model would you like to update? Enter the index: "))
        update_model(index, models)


def update_client(index, client):
    print("1. Update client name")
    print("2. Update client car firm")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("That's not a valid choice. Please enter a number.")
        update_client(index, client)

    # Get user choice
    if not is_valid_input(choice, 2):
        print("blahblah")
    # Update client name
    if choice == 1:
        new_name = input("Enter the new name: ")
        client[index]['name'] = new_name
    # Update client car firm
    elif choice == 2:
        new_car_firm = input("Enter the new car firm: ")
        client[index]['firm'] = new_car_firm


# Function to update model information


def update_model(
    index, models
):  # this function gives you the choice using the print function to pick between model color and year
    print("1. Update model")
    print("2. Update color")
    print("3. Update year")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("That's not a valid choice. Please enter a number.")
        return

    ## add validation
    # Get user choice
    # this line of code take the user input transfers it to an integer using it as the index to update the information from
    choice = int(input("Enter your choice: "))
    if not is_valid_input(choice, 3):
        print("blahblah")

    # Update model
    if choice == 1:  # if player picked 1 it will be model that he changes
        # takes the answer from the user on the model update and changes the correct calue in its position inside the list
        new_model = input("Enter the new model: ")
        # This line updates the model of the car in the models list. It uses the index to find the correct car in the list, and [0] to access the model field of the car. It then assigns the value of new_model to this field, effectively updating the model of the car.
        # models = [
            # 0: {name: "Ferrari", "Year": 2024}, 
            # 1: {name: "Fiat", "Year": 1999},
            # 2: {name: "Lamburgini", "Year": 2006}
        # ]
        models[index]['model'] = new_model

    # Update color
    elif choice == 2:
        new_color = input("Enter the new color: ")
        # using the {index}[0] you acceces the index to find the correct car and the correct position to update effectivly changing the data in this position in the list
        models[index]['color'] = new_color
    # Update year
    elif choice == 3:
        new_year = int(input("Enter the new year (numbers only): "))
        models[index]['year'] = new_year
