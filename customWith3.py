import requests

class customAPI:
    def __init__(self):
        self.base_url = "https://codeforces.com/api/"

    def RECENTSUBMISSIONS(self, handle, count):
        url = f"{self.base_url}user.status?handle={handle}"
        response = requests.get(url)
        data = response.json()

        if data["status"] != "OK":
            raise Exception("Failed to fetch recent submissions")

        submissions = data["result"][:count]
        return submissions

    def USERINFO(self, handle):
        url = f"{self.base_url}user.info?handles={handle}"
        response = requests.get(url)
        data = response.json()

        if data["status"] != "OK":
            raise Exception("Failed to fetch user info")

        user_info = data["result"][0]  # Assuming only one user is returned
        return user_info

    def CONTESTINFO(self, contest_id):
        url = f"{self.base_url}contest.standings?contestId={contest_id}"
        response = requests.get(url)
        data = response.json()

        if data["status"] != "OK":
            raise Exception("Failed to fetch contest info")

        contest_info = data["result"]["contest"]
        return contest_info