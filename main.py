import os
from tiktok import (
    grab_videos,
    create_client_access_token
)
import json

# os.environ["TIKTOK_CLIENT_KEY"] = "REPLACE"
# os.environ["TIKTOK_CLIENT_SECRET"] = "REPLACE"

if __name__ == '__main__':
    client_token_obj = create_client_access_token()
    if(client_token_obj['access_token'] == None):
        print('No access token')
        exit()

    print(grab_videos(client_token_obj['access_token']))