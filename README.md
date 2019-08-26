# Youtube Playlist Titles

Does exactly what you think it does. Given a playlist ID, gets the titles of every video in the playlist.

#### Usage

1. Get a Google API key from the [Google Developer Console](https://console.developers.google.com)
2. Activate the YouTube API for your application
3. `export YT_API_KEY=<your YouTube API key>`
4. `python3 youtube_playlist_titles.py <playlist_id>`

By default the script prints the titles to STDOUT; use output redirection to get the titles in a file.

