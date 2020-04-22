# Spotify Data Analyzer
This is a set of functions used for analyzing data from Spotify.

#### Functions:
- See total amount of time listened
- See top artists and songs listened to
- Select certain months or hours to analyze
- Use a date range to review streaming data

## Downloading data from Spotify
To download your streaming data from Spotify, you'll have to go to the privacy tab underneath your account. There, you can request a download of your data, including your streaming history.

## Importing your data
When you receive your data from Spotify, download and unzip it, then put pass the directory path to the `parse` method:
```
dir = "C:/Users/example/MyData/"
history = parse(dir)
```
After that, you use the `history` variable for a variety of things:
#### Total Time:
```
time = totalTime(history)
print(time)
```
#### Artists by Time:
```
artists = artistsByTime(history)
printBT(artists)
```
#### Songs by Time:
```
songs = songsByTime(history)
printBT(songs)
```

For more examples and more detailed documentation, check out the `example.py` file