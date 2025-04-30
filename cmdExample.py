### Libraries ###
import RLCounter as rlc
import time
import sys


### Variables ###
argc = len(sys.argv)


### Functions ###
def autoMode():
    print("------------------------")
    print("Auto check mode activated.")
    print("The program will check for a new match every 5 minutes.")
    print("Press Ctrl + C to stop.")
    print("------------------------")
    try:
        while True:
            print("Checking for a new match...")
            rlc.verify_last_match()
            time.sleep(300)
    except (KeyboardInterrupt):
        print("\nAuto check mode stopped.")


### Arguments ###
for i in range(1, argc):
    argument = sys.argv[i]
    if (argument.startswith("--")):
        argument = argument.removeprefix("--")

        if (argument == "auto"):
            autoMode()


### Main ###
while (True):

    # Show options
    print("MyRLCounter cmdExample")
    print("Choose an option\n")
    
    print("1. View Score")
    print("2. Check for New Match")
    print("3. Reset Score")
    print("4. Auto Check")
    print("5. Exit")

    # Get input and check if the user wants to exit
    try:
        choice = input("Choose an option: ")
        choice = choice if (choice is int) else 0
    except (KeyboardInterrupt):
        print("\n")
        choice = 5

    # Check the selected option
    match (int(choice)):
        case 1:
            score = rlc.load_score()
            print("------------------------")
            print(f"Wins: {score['wins']} | Losses: {score['losses']}")
            print("------------------------")

        case 2:
            rlc.verify_last_match()

        case 3:
            rlc.save_score({'wins': 0, 'losses': 0})
            print("------------------------")
            print("Score reset.")
            print("------------------------")

        case 4:
            autoMode()

        case 5:
            print("Exiting...")
            break

        # If the option wasn't found
        case _:
            print("Invalid choice. Please try again.")
