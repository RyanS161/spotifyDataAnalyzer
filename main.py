from spotifyDataAnalyzer.methods import *


# Add the directory containing the streaming data json files here:
dir = "C:/Users/Ryan/PycharmProjects/wrapped2.0/MyData/"

# The streaming history object is created here:
history = parse(dir)

# We can use the totalTime function to view the total amount of time listened in a streaming object:
time = totalTime(history)
print(time)

# Or, we can use the mmToHMS function to view the amount in time formatted:
print(msToHMS(time))

# Next, we can view all artists played ordered by time for a certain streaming object:
artists = artistsByTime(history)

# This data is printed in an orderly table with the print By Time function:
printBT(artists)

# We can also view songs listened to by time with the songsByTime function:
songs = songsByTime(history)
printBT(songs)

# The data can also be analyzed in chunks, including hours, dates, or months
# Here, we can see during which hours the most music has been listened to:
for x in range(24):
    # The last argument for the hourSlice method is the difference from UTC
    hour = hourSlice(x, history, 6)
    print(f"{x}: {msToHMS(totalTime(hour))}")

# Next, we can use a month slice to see which artists were listened to most during March:
month = monthSlice(3, history)
printBT(songsByTime(month))

# Finally, we can use a date slice to see the most played songs for the summer:
summer = dateSlice('Jun 5 2019', 'Sep 22 2019', history)
printBT(songsByTime(summer))
