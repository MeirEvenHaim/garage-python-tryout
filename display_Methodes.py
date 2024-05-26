from icecream import ic


def exit_1():
    exit()


# Function to get user


def display_C(client):
    for c in range(len(client)):
        ic(client[c])


def display_M(models):
    for m in range(len(models)):
        ic(models[m])


def info(client, models):
    info_c = int(
        input(
            "do you want to see the sum of you clients ir the sum of your car models? press '1' for clients and '2' for models"
        )
    )
    if info_c == 1:
        print(f"total clients in the archives are{len(client)}")

    else:
        print(f"total car models in archives are {len(models)}")
