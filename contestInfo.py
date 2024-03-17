import json
from tabulate import tabulate
from customWith3 import customAPI


def reading(filename):
    with open(filename, "r") as f:
        config = json.load(f)
    return config


def contestGetInfo(api, contest_id, info_fields):
    contest_info = api.contestGetInfo(contest_id)
    filtered_info = {}
    for field, include in info_fields.items():
        if include:
            filtered_info[field] = contest_info.get(field, "N/A")
    return filtered_info


def contestInfoing():
    api = customAPI()
    info_config = reading("submissions/contestInfo.json")
    contest_id = info_config.get("id")
    info_fields = info_config.get("info_fields", {})

    try:
        contest_info = contestGetInfo(api, contest_id, info_fields)
        print(f"\nContest Info for Contest ID {contest_id}:\n")
        table_data = [[key.capitalize(), value] for key, value in contest_info.items()]
        print(tabulate(table_data, headers=["Field", "Value"], tablefmt="grid"))
    except Exception as e:
        print("Error:", e)


