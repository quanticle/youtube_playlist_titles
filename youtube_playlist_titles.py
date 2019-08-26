#! /usr/bin/python3

import json
import os
import requests
import sys

youtube_api_key = os.environ['YT_API_KEY']

def get_titles_from_page(page_json):
    playlist_items = page_json["items"]
    return [item["snippet"]["title"] for item in playlist_items]

def get_page(playlist_id, page_token=None):
    params = {
        "key": youtube_api_key,
        "playlistId": playlist_id,
        "part": "snippet"
    }
    if page_token:
        params["pageToken"] = page_token
    
    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems", params)
    return response.json()

def get_all_titles(playlist_id):
    page_json = get_page(playlist_id)
    next_page_token = page_json.get("nextPageToken")
    titles = list(get_titles_from_page(page_json))
    while(next_page_token):
        page_json = get_page(playlist_id, page_token=next_page_token)
        titles.extend(get_titles_from_page(page_json))
        next_page_token = page_json.get("nextPageToken")
    return titles

def main():
    if not youtube_api_key:
        print("Please set $YT_API_KEY with your YouTube API key")
        sys.exit(1)
    if len(sys.argv) < 2:
        print("Usage: youtube_playlist_titles.py playlist_id")
        sys.exit(2)
    playlist_id = sys.argv[1]
    all_titles = get_all_titles(playlist_id)
    for title in all_titles:
        print(title)

if __name__ == "__main__":
    main()
