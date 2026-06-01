import csv
import random


def load_csv(filename):
    items = []

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                items.append(row["name"])

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        print("Please make sure the CSV file is in the same folder as this Python file.")
        exit()

    except KeyError:
        print(f"Error: {filename} must have a column called 'name'.")
        exit()

    return items


def get_game_mode():
    while True:
        print("\nSelect game mode:")
        print("1. 1v1")
        print("2. 2v2")

        choice = input("Enter option 1 or 2: ").strip()

        if choice == "1":
            return "1v1", 2
        elif choice == "2":
            return "2v2", 4
        else:
            print("Please enter either 1 or 2.")


def get_number_of_humans(total_players):
    while True:
        try:
            humans = int(input(f"How many human players? 0 to {total_players}: "))

            if 0 <= humans <= total_players:
                return humans
            else:
                print(f"Please enter a number between 0 and {total_players}.")

        except ValueError:
            print("Please enter a valid number.")


def create_player_labels(mode, total_players, number_of_humans):
    labels = []

    if mode == "2v2" and number_of_humans >= 3:
        print("\nEnter Team 1 players:")

        for player_number in range(1, 3):
            if player_number <= number_of_humans:
                name = input(f"Enter name for P{player_number}: ").strip()

                if name == "":
                    name = f"User {player_number}"

                labels.append(f"P{player_number} - {name}")
            else:
                cpu_number = player_number - number_of_humans
                labels.append(f"P{player_number} - CPU {cpu_number}")

        print("\nEnter Team 2 players:")

        for player_number in range(3, 5):
            if player_number <= number_of_humans:
                name = input(f"Enter name for P{player_number}: ").strip()

                if name == "":
                    name = f"User {player_number}"

                labels.append(f"P{player_number} - {name}")
            else:
                cpu_number = player_number - number_of_humans
                labels.append(f"P{player_number} - CPU {cpu_number}")

    else:
        for player_number in range(1, total_players + 1):
            if player_number <= number_of_humans:
                name = input(f"Enter name for P{player_number}: ").strip()

                if name == "":
                    name = f"User {player_number}"

                labels.append(f"P{player_number} - {name}")
            else:
                cpu_number = player_number - number_of_humans
                labels.append(f"P{player_number} - CPU {cpu_number}")

    return labels


def randomise_players(player_labels, characters, rackets):
    if len(characters) < len(player_labels):
        print("Error: Not enough characters in characters.csv.")
        exit()

    if len(rackets) < len(player_labels):
        print("Error: Not enough rackets in rackets.csv.")
        exit()

    chosen_characters = random.sample(characters, len(player_labels))
    chosen_rackets = random.sample(rackets, len(player_labels))

    results = []

    for i, label in enumerate(player_labels):
        results.append({
            "label": label,
            "character": chosen_characters[i],
            "racket": chosen_rackets[i]
        })

    return results


def print_results(mode, results):
    print("\n==============================")
    print("Mario Tennis Fever Randomiser")
    print("==============================")
    print(f"Mode: {mode.upper()}\n")

    if mode == "1v1":
        for player in results:
            print(f"{player['label']}")
            print(f"  Character: {player['character']}")
            print(f"  Racket:    {player['racket']}")
            print()

    elif mode == "2v2":
        team_1 = results[:2]
        team_2 = results[2:]

        print("Team 1")
        for player in team_1:
            print(f"  {player['label']}: {player['character']} + {player['racket']}")

        print("\nTeam 2")
        for player in team_2:
            print(f"  {player['label']}: {player['character']} + {player['racket']}")

    print("==============================\n")


def main():
    print("Welcome to the Mario Tennis Fever Randomiser!")

    mode, total_players = get_game_mode()
    number_of_humans = get_number_of_humans(total_players)
    player_labels = create_player_labels(mode, total_players, number_of_humans)

    characters = load_csv("data/characters.csv")
    rackets = load_csv("data/rackets.csv")

    while True:
        results = randomise_players(player_labels, characters, rackets)
        print_results(mode, results)

        again = input("Randomise again with the same players? yes/no: ").strip().lower()

        if again not in ["yes", "y"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()