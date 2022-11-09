# Youtube-API-analysis
Analysing the youtube channel Andrew Huberman to extract keywords from high performing content.
  



![Expolatory- data analysis](https://user-images.githubusercontent.com/111446453/200786109-90dd9f37-3bd7-4357-b872-0894e2f7e81f.png)


# Overview
Data APIs are a great source of data for data analytics projects. In this readme, I'm walking you step by step through the process of retrieving video data and channel data using Youtube Data API.


And also the techniques to Visualize the obtained data.
# Obtaining Youtube developer key
We start this project by first creating an YouTube API Key which will be our credential to access youtube data.
go to google developer console and sign through your google account
then create a new project, enable api & create a new api key, copy this api key and paste it into you code as a variable.
# Obtaining  Channel Id from source code 
Go to the below link and look through the youtube api documentation for code snippet to obtain channel id.
https://developers.google.com/youtube/v3/docs/channels/list?apix=true


For obtaining channel id of a specific channel, go to youtube and follow steps below.

![Screenshot (53)](https://user-images.githubusercontent.com/111446453/185879908-c1a88dee-a259-468c-a3f1-d19e4e45589d.png)
Click **ctrl+u** to open a new tab with source code


Next click **ctrl+f** to find itemprop="channelId"  
copy the value stored in content variable with key equal to itemprop="channelId"
then store it in a variable

![Screenshot (54)](https://user-images.githubusercontent.com/111446453/185878809-4d823838-85df-479c-8eea-9bd31450ec10.png)
# Install required python pakages
install "google-api-python-client" (which is the google python package required to access youtube api data), we will also install pandas, seaborn & Matplotlib.



# Data Scraping from Youtube Data API
Youtube data api stores all data in json form as shown in below pictorial representation.


![Screenshot (59)](https://user-images.githubusercontent.com/111446453/185903047-35e6a7d6-d1c6-4782-8fea-8460c74a743b.png)

## Extracting playlist id from channel details
We extract channel details from youtube. I.e. we extract details such as youtube channel name and playlistId.
Below is the image of code snippet of function for extracting channel details.


![Screenshot (66)](https://user-images.githubusercontent.com/111446453/185906866-6eabe163-82d0-4adf-a240-b71c7071bf76.png)


We will be loading this data into a pandas dataframe and then store the obtained playlistId in a variable named playlist_id.
## Extract video ids from playlist id using youtube api documentation
Below is the image of code snippet of function for extracting videoIds.

![Screenshot (61)](https://user-images.githubusercontent.com/111446453/185906974-31a9976f-e498-4851-9c16-f1249f3aa935.png)


We shall build a logic to extract video Ids from playlistId for a particular channel.
Below is the image of code snippet of function for extracting videoIds.


![Screenshot (62)](https://user-images.githubusercontent.com/111446453/185906991-d954d14b-d882-4b50-957b-372b230529da.png)

We shall extract details such as video title, video description, total views each video has got, total number of likes, each video has got. 
Then load these details into pandas dataframe.

![Screenshot (58)](https://user-images.githubusercontent.com/111446453/185882610-6eb8c9d6-fb75-453f-a305-5681fe32193b.png)



# Data Pre-processing
## check for null or empty values in pandas dataframe storing video details.


![Screenshot (63)](https://user-images.githubusercontent.com/111446453/185907207-a0b3da1e-ca37-4140-b56e-d4385ac39e3f.png)




## check for data type of different columns of video_df pandas data frame






![Screenshot (65)](https://user-images.githubusercontent.com/111446453/185907235-87eb9b1b-3e38-459d-84fe-682568adb2c4.png)


to use this data for visualization we need to convert likes and view count into numeric form
## converting likeCount and viewCount into numeric data type





![Screenshot (64)](https://user-images.githubusercontent.com/111446453/185907283-9cea9ea9-a063-4896-8303-3ff10a455e34.png)



# Exploratory data Analysis
The main purpose of EDA is to help look at data before making any assumptions.
It can help identify obvious errors, as well as better understand patterns within the data, detect outliers or anomalous events, find interesting relations among the variables.


## Best performing videos

![Screenshot (55)](https://user-images.githubusercontent.com/111446453/185881753-744cea0a-d386-4e82-9705-fd95e00f77f4.png)
## Worst performing videos
![Screenshot (56)](https://user-images.githubusercontent.com/111446453/185881613-615ce17c-2d9b-4765-b2c0-1adb6a6a99c5.png)

## Likes vs Views
Using scatter plot to visualize the relation between view count and like count
![Screenshot (57)](https://user-images.githubusercontent.com/111446453/185881792-b9c03223-8891-439f-af10-669e5b504e15.png)
