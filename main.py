from googleapiclient.discovery import build

import pandas as pd


# Data viz packages
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# copy the api key generated in google cloud services
api_key = 'AIzaSyBBxURD5xXthseVM3K5pBlmqk1kjwxkKfA'
channel_id = 'UCm4E1b5TjstT8UUIk7mb-MA'
 

youtube = build('youtube', 'v3', developerKey = api_key)

#function to get channel statistics

def get_channel_stats(youtube, channel_id):

  all_data = []

  request = youtube.channels().list(
      part='snippet,contentDetails,statistics',id = channel_id)

  response = request.execute()

  #loop through items
  for item in response['items']:
    data = {'channel Name' : item['snippet']['title'],
            'playlist_id' : item['contentDetails']['relatedPlaylists']['uploads']
            }
    all_data.append(data)        

  return all_data


channel_statistics = get_channel_stats(youtube, channel_id)
channel_data = pd.DataFrame(channel_statistics)
channel_data
playlist_id = 'UUm4E1b5TjstT8UUIk7mb-MA'


# function to get video ids
def get_video_ids(youtube, playlist_id):
    
    video_ids = []
    
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults = 50
    )
    response = request.execute()
    
    for item in response['items']:
        video_ids.append(item['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId = playlist_id,
                    maxResults = 50,
                    pageToken = next_page_token)
        response = request.execute()

        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')
        
    return video_ids
  
  video_ids = get_video_ids(youtube, playlist_id)
  
  
  
  # function to get video details
  def get_video_details(youtube, video_ids):

    all_video_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute() 

        for video in response['items']:
            stats_to_keep = {'title': video['snippet']['title'], 'description': video['snippet']['description'],
                             'view_count':video['statistics']['viewCount'], 'like_count':video['statistics']['likeCount']
                            }
        
            all_video_info.append(stats_to_keep)
    
    return pd.DataFrame(all_video_info)
  
  video_df =  get_video_details(youtube, video_ids)
  video_df
  
  
  # data pre-processing
  
  #check is there are any null values
  video_df.isnull().any()
  # Check data types
  video_df.dtypes
  
  # Convert count columns to numeric
 numeric_cols = ['view_count', 'like_count']
 video_df[numeric_cols] = video_df[numeric_cols].apply(pd.to_numeric, errors = 'coerce', axis = 1)
  
  

from googleapiclient.discovery import build
import pandas as pd

#for data visualization
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


copy the api key generated in google cloud services

api_key = 'AIzaSyBBxURD5xXthseVM3K5pBlmqk1kjwxkKfA'
channel_id = 'UCm4E1b5TjstT8UUIk7mb-MA'
 

youtube = build('youtube', 'v3', developerKey = api_key)

function to get channel statistics

def get_channel_stats(youtube, channel_id):

  all_data = []

  request = youtube.channels().list(
      part='snippet,contentDetails,statistics',id = channel_id)

  response = request.execute()

  #loop through items
  for item in response['items']:
    data = {'channel Name' : item['snippet']['title'],
            'playlist_id' : item['contentDetails']['relatedPlaylists']['uploads']
            }
    all_data.append(data)        

  return all_data

channel_statistics = get_channel_stats(youtube, channel_id)

channel_data = pd.DataFrame(channel_statistics)

channel_data

playlist_id = 'UUm4E1b5TjstT8UUIk7mb-MA'

function to get video ids

def get_video_ids(youtube, playlist_id):
    
    video_ids = []
    
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        maxResults = 50
    )
    response = request.execute()
    
    for item in response['items']:
        video_ids.append(item['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId = playlist_id,
                    maxResults = 50,
                    pageToken = next_page_token)
        response = request.execute()

        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')
        
    return video_ids

video_ids = get_video_ids(youtube, playlist_id)

len(video_ids)

206

function to get video details

def get_video_details(youtube, video_ids):

    all_video_info = []
    
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute() 

        for video in response['items']:
            stats_to_keep = {'title': video['snippet']['title'], 'description': video['snippet']['description'],
                             'view_count':video['statistics']['viewCount'], 'like_count':video['statistics']['likeCount']
                            }
        
            all_video_info.append(stats_to_keep)
    
    return pd.DataFrame(all_video_info)

data pre-processing

check is there are any null values

title          False
description    False
view_count     False
like_count     False
dtype: bool



# Check data types
video_df.dtypes

#EDA  
#Best performing videos

ax = sns.barplot(x = 'title', y = 'view_count', data = video_df.sort_values('view_count', ascending=False)[0:9])
plot = ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos:'{:,.0f}'.format(x/1000) + 'K'))

#Worst performing videos

ax = sns.barplot(x = 'title', y = 'view_count', data = video_df.sort_values('view_count', ascending=True)[0:9])
plot = ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.show()

#Views vs. likes

sns.scatterplot(data = video_df, x = 'like_count', y = 'view_count')



  
  
  







