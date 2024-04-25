import requests
import os

tt_client_key = "REPLACE"
tt_client_secret = "REPLACE"

def create_client_access_token():
    url = "https://open.tiktokapis.com/v2/oauth/token/"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }

    data = {
        "client_key": tt_client_key,
        "client_secret": tt_client_secret,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, headers=headers, data=data)

    return response.json()

def grab_videos(access_token: str):
    url = "https://open.tiktokapis.com/v2/research/video/query/"

    headers = {
        "authorization": f"bearer {str(access_token)}",
        "Content-Type": "application/json"
    }

    data = {
    "query": {
        "and": [
            {"operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"]},
            {"operation": "EQ", "field_name": "hashtag_name", "field_values": ["fashion"]}
        ]
    },
        "start_date": "20240418",
        "end_date": "20240425",
        "max_count": 10
    }

    print(f"bearer {str(access_token)}")

    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response data
        print('yahoo')
    else:
        print("Request failed with status code:", response.status_code)

    return response.json()

    
if __name__ == "__main__":
    grab_videos()