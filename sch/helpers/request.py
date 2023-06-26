import os
import json
from dotenv import load_dotenv
import requests
from sch.helpers.definitions import domain, headers

load_dotenv()


def db_request(endpoint: str, data: dict):
    data["API_KEY"] = os.environ["API_KEY"]
    payload = json.dumps(data)
    url = f"{domain}{endpoint}"
    try:
        response = requests.post(url, data=payload, headers=headers, verify=False)
        if response.status_code != requests.codes.ok:
            return f"Request failed with status code: {response.status_code}"
        response_json = response.json()
        return {"error": False, "data": response_json["data"]}
    except requests.RequestException as e:
        return {"error": True, "data": f"An error occurred: {str(e)}"}
