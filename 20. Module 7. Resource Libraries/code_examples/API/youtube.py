#1 INTRO
# import os
# import requests


# from googleapiclient.discovery import build

# api_key = os.environ.get('api_key')

# youtube = build('youtube', 'v3', developerKey=api_key)

# request = youtube.channels().list(
#         part='statistics',
#         forUsername='MetallicaTV'
#     )

# response = request.execute()

# print(response)

#2 Duration
#2.1
# import os
# import requests
# import re
# from datetime import timedelta


# from googleapiclient.discovery import build

# hours_pattern = re.compile(r'(\d+)H')
# minutes_pattern = re.compile(r'(\d+)M')
# seconds_pattern = re.compile(r'(\d+)S')


# api_key = os.environ.get('api_key')

# youtube = build('youtube', 'v3', developerKey=api_key)

# request = youtube.channels().list(
#         part='contentDetails',
#         forUsername='MetallicaTV'
#     )

# playlist_request = youtube.playlists().list(
#         part='contentDetails, snippet',
#         channelId ="UCbulh9WdLtEXiooRcYK7SWw"
#     )

# playlist_request = youtube.playlistItems().list(
#         part='contentDetails',
#         playlistId ="PLJvQXRgtxlulwncoZD8DX1sdf7qGL2t7A"
#     )
# playlist_response = playlist_request.execute()

# for item in playlist_response["items"]:
#     print(item)
#     print("*"*50)
# video_ids = []
# for item in playlist_response["items"]:
#     video_id = item["contentDetails"]["videoId"]
#     video_ids.append(video_id)
#     # print(video_id)
#     # print("*"*50)
# print(",".join(video_ids))
# # print(playlist_response)
# video_request = youtube.videos().list(
#         part="contentDetails",
#         id=','.join(video_ids)
#     )

# video_response = video_request.execute()
# for item in video_response["items"]:
#     print(item)
#     print("*"*50)

# for item in video_response['items']:
#     duration = item['contentDetails']['duration']
#     # print(duration)
#     hours = hours_pattern.search(duration)
#     minutes = minutes_pattern.search(duration)
#     seconds = seconds_pattern.search(duration)

#     hours = int(hours.group(1)) if hours else 0
#     minutes = int(minutes.group(1)) if minutes else 0
#     seconds = int(seconds.group(1)) if seconds else 0
    
#     video_seconds = timedelta(
#         hours=hours,
#         minutes=minutes,
#         seconds=seconds
#     ).total_seconds()
#     print(video_seconds)
#2.2
import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

api_key = os.environ.get('api_key')

youtube = build('youtube', 'v3', developerKey=api_key)

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

total_seconds = 0


nextPageToken = None
while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId="PLJvQXRgtxlulwncoZD8DX1sdf7qGL2t7A",
        maxResults=50,
        pageToken=nextPageToken
    )

    pl_response = pl_request.execute()

    vid_ids = []
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    vid_request = youtube.videos().list(
        part="contentDetails",
        id=','.join(vid_ids)
    )

    vid_response = vid_request.execute()

    for item in vid_response['items']:
        duration = item['contentDetails']['duration']

        hours = hours_pattern.search(duration)
        minutes = minutes_pattern.search(duration)
        seconds = seconds_pattern.search(duration)

        hours = int(hours.group(1)) if hours else 0
        minutes = int(minutes.group(1)) if minutes else 0
        seconds = int(seconds.group(1)) if seconds else 0

        video_seconds = timedelta(
            hours=hours,
            minutes=minutes,
            seconds=seconds
        ).total_seconds()

        total_seconds += video_seconds

    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break

total_seconds = int(total_seconds)

minutes, seconds = divmod(total_seconds, 60)
hours, minutes = divmod(minutes, 60)

print(f'{hours}:{minutes}:{seconds}')
