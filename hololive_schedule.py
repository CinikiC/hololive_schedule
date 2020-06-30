#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python3
# You should change your python3 interpreter location here


# Required additional packages:
# 1. bs4 (html analyse)
# 2. requests (get webpage)

from bs4 import BeautifulSoup
import requests as req
import re
from requests.cookies import RequestsCookieJar
import os
import time
import datetime


# Designed UA header for HTTP-GET request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
}


# Get cookie from domain schedule.hololive.tv
cookie_local = {}
resp = req.get("https://schedule.hololive.tv/lives/all", headers=headers)
cookie_local = resp.cookies
# Set the timezone as UTC in cookie to get schedule in UTC timezone
cookie_local.set("timezone", "UTC", domain="schedule.hololive.tv")


# Get HTML response of the schedule webpage
def get_html():
    resp = req.get("https://schedule.hololive.tv/lives/all",
                   cookies=cookie_local)
    return resp


# Get the nodes contain schedule info 
# (The real live schedule is a div tag which class is 'tab-content')
def get_raw_schedule(html):
    soup = BeautifulSoup(html.text, "lxml")
    return soup.find_all(class_="tab-content")


# Traverse all tag nodes and classify them as tags contain date, 
# time, VTuber's name and liveroom link, using class-id 
def tag_classify(tag):
    if(tag.has_attr("class")):
        class_list = tag['class']
        # Tags contain date strings always with a class-id 'holodule navbar-text'
        if('holodule' in class_list
                and 'navbar-text' in class_list):
            return "date"
        # Tags contain time strings always with a class-id contains 'datetime'
        elif('datetime' in class_list):
            return "time"
        # Tags contain VTuber name always with a class-id contains 'text-right name'
        elif('col' in class_list and 'text-right' in class_list and 'name' in class_list):
            return "name"
        # Tags contain liveroom link always with a class-id contains 'thumbnail'
        elif('thumbnail' in class_list):
            return "link"
        else:
            return "others"
    else:
        return "others"


# Confirm if the VTuber is streaming now 
# (The VTubers who are streaming will have a red border around the liveroom info card on the schedule webpage)
def is_streaming(tag):
    if(tag.has_attr("style")):
        style_list = tag['style']
        if('border: 3px red solid' in style_list):
            return True
        else:
            return False
    else:
        return False


# Format the strings from tag nodes
def format_string(string):
    return string.replace("\n", "").replace("\t", "").replace("\r", "").replace("None", "").replace(" ", "")


# Confirm if a VTuber's live is not started
# (The liveroom about to start will have strings contains 'scheduledStartTime' in their webpages)
def is_upcoming(tag):
    resp = req.get(tag['href'])
    upcoming_flag = re.search("scheduledStartTime", resp.text)
    if(upcoming_flag is not None):
        return True
    else:
        return False


# Auto detect timezone and convert UTC time (on the webpage) to user's loacl time
def utc_2_localtime(utc):
    utc_t = datetime.datetime.strptime(utc, "%m/%d %H:%M")
    local_timestamp = time.time()
    local_time = datetime.datetime.fromtimestamp(local_timestamp)
    utc_time = datetime.datetime.utcfromtimestamp(local_timestamp)
    offset = local_time - utc_time
    local = utc_t + offset
    return (datetime.datetime.strftime(local, "%m/%d %H:%M"))


raw_schedule = get_raw_schedule(get_html())         # Get the tag nodes contain schedule info
date = "date_dummy_string"                          # Date status (changed when analyse new date)
schedule = []                                       # Blank schedule list
live = {}                                           # Blank liveroom dictionary
timezone = time.strftime("%z", time.localtime())    # User's timezone


# Analyse tag nodes
for tag in raw_schedule[0].find_all():
    # Tags contain date string detected (like '06/30(日)'), update date value
    if(tag_classify(tag) == "date"):
        date = format_string(tag.string)[0:5]       # Drop week info
    # Tags contain time string detected (like '14:00'), 
    # combine date and time as a key in the dictionary
    elif(tag_classify(tag) == "time"):
        for time_string in tag.strings:
            if(time_string.replace("\n", "").replace("\t", "").replace("\r", "").replace("None", "").replace(" ", "") is not ""):
                live['time'] = utc_2_localtime(
                    date+" "+format_string(time_string))
    # Tags contain VTuber's name string detected (like 'Risu'), 
    # insert the name as a key in the dictionary
    elif(tag_classify(tag) == "name"):
        live['host'] = format_string(tag.string)
    # Tags contain liveroom link detected, 
    # get the status of the liveroom (Stream over, Streaming now or Stream will start) 
    # and insert different key in the dictionary
    elif(tag_classify(tag) == "link"):
        live['link'] = tag['href']
        if(is_streaming(tag)):
            live['status'] = 'streaming'
        elif(is_upcoming(tag)):
            live['status'] = 'upcoming'
        else:
            live['status'] = 'over'
    # If all keys of a dictionary is inserted, append it into the schedule list
    if(len(live) == 4):
        schedule.append(live)
        live = {}   # Clear the dictionary for new info


# Print in the BitBar
print("▶️")
print("---")
print("Streaming now (Click to jump to the chatroom in your web browser)")
for stream_live in schedule:
    if(stream_live['status'] == 'streaming'):
        print("🔴 " + stream_live['host'] + " | href=" + stream_live['link'])
print("---")
print("Upcoming (Auto detected timezone is UTC" + timezone + ")")
for upcoming_live in schedule:
    if(upcoming_live['status'] == 'upcoming'):
        print(upcoming_live['time']+" "+upcoming_live['host'] +
              " | href="+upcoming_live['link'])
print("---")
print("Streaming over")
for over_live in schedule:
    if(over_live['status'] == 'over'):
        print(over_live['time']+" "+over_live['host'] +
              " | href="+over_live['link'])
