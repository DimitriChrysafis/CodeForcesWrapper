from submissionForUser import getRecent
from infoForUser import infoForUsering
from contestInfo import contestInfoing
import json

def updateAndReplace(filename, key, value):
    with open(filename, "r+") as f:
        config = json.load(f)
        config[key] = value
        f.seek(0)
        json.dump(config, f, indent=4)
        f.truncate()

def main():
    print("Welcome to Codeforces Information Retrieval Tool!")
    print("Select an option:")
    print("1. Get user's info")
    print("2. Get recent submissions for a user")
    print("3. Get contest info")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        username = input("Enter the username: ")
        updateAndReplace("submissions/infoForUser.json", "username", username)
        infoForUsering()
    elif choice == "2":
        username = input("Enter the username: ")
        updateAndReplace("sample.json", "username", username)
        problem_count = input("Enter the number of recent problems to show: ")
        try:
            problem_count = int(problem_count)
            updateAndReplace("sample.json", "problem_count", problem_count)
            getRecent()
        except ValueError:
            print("Please enter an integer.")
    elif choice == "3":
        contest_id = input("Enter the contest ID: ")
        updateAndReplace("submissions/contestInfo.json", "id", contest_id)
        contestInfoing()
    else:
        print("no")

if __name__ == "__main__":
    main()
