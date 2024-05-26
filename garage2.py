from icecream import ic
from enum import Enum
from add import add
from delete_methodes import delete
from display_Methodes import display_C, display_M, exit_1, info
from updata import update
import json

client = [
    {'name': 'Client1', 'car_firm': 'Firm1'},
    {'name': 'Client2', 'car_firm': 'Firm2'},
    # ...
]  # [Name , Model]
models = [
    {'model': 'gege', 'color':'black', 'firm':'blahblah'},
     {'model': 'gegea', 'color':'blacka', 'firm':'blahblahaa'},
    # ...
]  # [Model , Color , Year]


class Garage(Enum):
    DISPLAY_CLIENT = 1
    DISPLAY_MODELS = 2
    ADD = 3
    DELETE = 4
    EXIT = 5
    UPDATE = 6
    MENU = 7

# TODO: Add back button

def menu():
    while True:
        ic("1-" + Garage.DISPLAY_CLIENT.name)
        ic("2-" + Garage.DISPLAY_MODELS.name)
        ic("3-" + Garage.ADD.name)
        ic("4-" + Garage.DELETE.name)
        ic("5-" + Garage.EXIT.name)
        ic("6-" + Garage.UPDATE.name)
        ic("7-" + Garage.MENU.name)
        try:
            user_c = int(input("Press enter to get to the menu:\n"))
        except ValueError:
            print("That's not a valid choice. Please enter a number.")
            continue
        if user_c == 1:
            display_C(client)
        if user_c == 2:
            display_M(models)
        if user_c == 3:
            add(client, models)
            save_data()
        if user_c == 4:
            delete(client, models)
        if user_c == 5:
            exit_1()
        if user_c == 6:
            update(client, models)
            save_data()
        if user_c == 7:
            info(client, models)
        if user_c == 8:
            main()
            load_data()


def save_data():
    data = {"clients": client, "model": models}
    with open("garage_dataCM.json", "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open("garage_data.json", "r") as file:
            data = json.load(file)
            client.extend(data.get("clients", []))
            models.extend(data.get("models", []))
    except FileNotFoundError:
        print("No existing data found. Starting with empty lists.")


def main():
    load_data()
    menu()


if __name__ == "__main__":
    main()
