# youtube-rss-grabber

This script takes a YouTube channel URL and generates its RSS Feed URL. It works by making a call to the webpage from which it extracts the `channel_id`, which no longer appears in the channel's URL since YouTube has switched to account handles.

## Usage

- Run the script with `./get-rss.py` or using Python3. For the former, may need to run `chmod +x get-rss.py` first to make the script executable.
- The channel URL (in the form of `https://www.youtube.com/@LMGClips`) may be entered when prompted, or passed as an argument with the `-u` or `--url` option.