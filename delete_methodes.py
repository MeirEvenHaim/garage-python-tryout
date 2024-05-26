from icecream import ic
import os


def delete(client, models):
    try:
        u_q = int(
            input(
                "Do you want to delete a client or a model? Press '1' for client and '2' for model:\n "
            )
        )
    except ValueError:
        print("That's not a valid choice. Please enter a number.")
        return
    if u_q == 1:
        for i in range(len(client)):
            ic(f"{i}:{client[i]}")
        try:
            delete_question_c = int(input("Which client would you like to delete? "))
            client.pop(delete_question_c)
        except ValueError:
            print("That's not a valid index. Please enter a number.")
        except IndexError:
            print("That index is out of range. Please enter a valid index.")
    elif u_q == 2:
        for j in range(len(models)):
            ic(f"{j}:{models[j]}")
        try:
            delete_question_m = int(input("Which model would you like to delete? "))
            models.pop(delete_question_m)
        except ValueError:
            print("That's not a valid index. Please enter a number.")
        except IndexError:
            print("That index is out of range. Please enter a valid index.")


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
