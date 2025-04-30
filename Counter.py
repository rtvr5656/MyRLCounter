# If you don't have the library, install it with "pip install requests"
# This script is designed to track the number of wins and losses in Rocket League.
# It uses the Tracker Network API to get the match history of a player.
# Just fill in the variables below and run the script.

import requests
import time
import json

# Configuration | if you don't know what to put, read the Help.txt file
api_key = ''
username = ''
platform = ''
url = f'https://public-api.tracker.gg/v2/rocket-league/standard/profile/{platform}/{username}'
headers = {'TRN-Api-Key': api_key}
score_archive = "score.txt"
last_match_id_file = "last_match.txt"


def load_score():
    try:
        with open(score_archive, 'r') as file:
            return json.load(file)
    except:
        return {'wins': 0, 'losses': 0}

def save_score(score):
    with open(score_archive, 'w') as file:
        json.dump(score, file)

def load_last_match_id():
    try:
        with open(last_match_id_file, 'r') as file:
            return file.read().strip()
    except:
        return ""

def save_last_match_id(match_id):
    with open(last_match_id_file, 'w') as file:
        file.write(match_id)

def verify_last_match(show_message=True):
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error loading API: verify your key or username.")
        return

    data = response.json()

    matches = data['data']['segments']
    last = next((i for i in matches if i['type'] == 'playlist'), None)

    if not last:
        print("No match found.")
        return

    match_id = last['metadata']['matchId']
    result = last['metadata'].get('result')

    last_saved_id = load_last_match_id()

    if match_id == last_saved_id:
        print("No new match.")
        return

    score = load_score()

    if result == 'win':
        score['wins'] += 1
        print("You win!")
    elif result == 'loss':
        score['losses'] += 1
        print("You lose!")
    else:
        print("No result found. (custom or private match, not counted)")
        return

    save_score(score)
    save_last_match_id(match_id)


def menu():
    while True:
        print("|----------------------------|")
        print("|--      by Dhunted          |")
        print("|-- Rocket League Counter    |")
        print("|----------------------------|")
        print("1. View score")
        print("2. Check for new match")
        print("3. Reset score")
        print("4. Auto check mode")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            score = load_score()
            print("------------------------")
            print(f"Wins: {score['wins']} | Losses: {score['losses']}")
            print("------------------------")

        elif choice == '2':
            verify_last_match()

        elif choice == '3':
            save_score({'wins': 0, 'losses': 0})
            print("------------------------")
            print("Score reset.")
            print("------------------------")

        elif choice == '4':
            print("------------------------")
            print("Auto check mode activated.")
            print("The program will check for a new match every 5 minutes.")
            print("Press Ctrl + C to stop.")
            print("------------------------")
            try:
                while True:
                    print("Checking for a new match...")
                    verify_last_match()
                    time.sleep(300)
            except KeyboardInterrupt:
                print("\nAuto check mode stopped.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

menu()
