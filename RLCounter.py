### Libraries ###
import requests
import json


### Variables ###

# Configuration Variables
api_key = 'XXX-XXX-XXX-XXX-XXX' # Change this with your API Key from tracker.gg
username = 'dummy' # Change this with your Rocket League account username
platform = 'epic' # Change this with your platform name (epic, steam, xbl, psn, switch)

# Software Variables
url = f'https://public-api.tracker.gg/v2/rocket-league/standard/profile/{platform}/{username}'
headers = {'TRN-Api-Key': api_key}
score_archive = "score.txt"
last_match_id_file = "last_match.txt"


### Functions ###

# Load the score
def load_score():
    try:
        with open(score_archive, 'r') as file:
            return json.load(file)
    except:
        return {'wins': 0, 'losses': 0}

# Save the score
def save_score(score):
    with open(score_archive, 'w') as file:
        json.dump(score, file)

# Load the id from the last match
def load_last_match_id():
    try:
        with open(last_match_id_file, 'r') as file:
            return file.read().strip()
    except:
        return ""

# Save the id from the last match
def save_last_match_id(match_id):
    with open(last_match_id_file, 'w') as file:
        file.write(match_id)

# Verify the last match
def verify_last_match(show_message : bool = True):
    response = requests.get(url, headers=headers)

    if (response.status_code != 200):
        print("Error loading API: verify your key or username.")
        return

    data = response.json()

    matches = data['data']['segments']
    last = next((i for i in matches if i['type'] == 'playlist'), None)

    if (not last):
        print("No match found.")
        return

    match_id = last['metadata']['matchId']
    result = last['metadata'].get('result')

    last_saved_id = load_last_match_id()

    if (match_id == last_saved_id):
        print("No new match.")
        return

    score = load_score()

    if (result == 'win'):
        score['wins'] += 1
        print("You win!")
    elif (result == 'loss'):
        score['losses'] += 1
        print("You lose!")
    else:
        print("No result found. (custom or private match, not counted)")
        return

    save_score(score)
    save_last_match_id(match_id)
