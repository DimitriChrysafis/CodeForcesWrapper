import json
from tabulate import tabulate
from customWith3 import customAPI


def read(filename):
    with open(filename, "r") as f:
        config = json.load(f)
    return config


def GETINFO(api, handle, info_fields):
    user_info = api.USERINFO(handle)
    filtered_info = {}
    for field, include in info_fields.items():
        if include:
            filtered_info[field] = user_info.get(field, "N/A")
    return filtered_info


def infoForUsering():
    api = customAPI()
    info_config = read("submissions/configForUser.json")
    handle = info_config.get("username")
    info_fields = info_config.get("info_fields", {})

    try:
        user_info = GETINFO(api, handle, info_fields)
        print(f"\nUser Info for {handle}:\n")
        table_data = [[key.capitalize(), value] for key, value in user_info.items()]
        print(tabulate(table_data, headers=["Field", "Value"], tablefmt="grid"))
    except Exception as e:
        print("Error:", e)
