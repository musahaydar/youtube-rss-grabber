#! /usr/bin/env python3
from argparse import ArgumentParser
import requests
import re

def main():
    parser = ArgumentParser()
    parser.add_argument("-u", "--url", type=str, default="")
    args = parser.parse_args()
    url = args.url

    if url == "":
        url = input("Enter a YouTube Channel URL: ")
    
    # grab the channel's webpage
    channel_page = requests.get(url)
    if channel_page.status_code != 200:
        print("There was an error connecting to YouTube.")
        return
    
    # extract the channel_id
    res = re.search("channel_id=([^\"]*)", channel_page.content.decode('utf-8'))
    channel_id = res.group(1)
    print("Channel ID: " + channel_id)
    print("RSS Feed: https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id)


if __name__ == '__main__':
    main()
