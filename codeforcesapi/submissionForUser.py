import json
from tabulate import tabulate
from termcolor import colored
from customWith3 import customAPI

def read(filename):
    with open(filename, "r") as f:
        config = json.load(f)
    return config

def filter(submission, problems_config):
    problem = submission.get("problem", {})
    filtered_problem = {}
    for field, include in problems_config.items():
        if include and field in problem:
            filtered_problem[field] = problem[field]
    return filtered_problem

def getRecent():
    api = customAPI()
    config = read("sample.json")
    handle = config["username"]
    count = config["problem_count"]
    submissions_config = read("submissions/configForSubmissions.json")
    problems_config = read("submissions/configForProblems.json")
    submissions = api.RECENTSUBMISSIONS(handle, count)
    print(f"\nRecent Submissions for {handle}:\n")
    table_data = []
    headers = []
    for field, include in problems_config.items():
        if include:
            headers.append(field.capitalize().replace("Seconds", "Time").replace("Id", "ID").replace("Count", ""))
    headers.extend([field.capitalize() for field, include in submissions_config.items() if include])
    for submission in submissions:
        row = []
        problem = filter(submission, problems_config)
        for field, include in submissions_config.items():
            if include:
                if field == "problem":
                    row.extend(problem.values())
                else:
                    value = submission.get(field, "N/A")
                    if field == "verdict":
                        value = colored(value, "green" if value == "OK" else "red")
                    row.append(value)
        table_data.append(row)

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

