import json
import datetime
import os



def parse(dir):
    merged_files = []
    with open("mydata/0result.json", "w") as outfile:
        for file in os.listdir(dir):
            if file.startswith('StreamingHistory'):
                with open(dir + file, encoding="utf8") as infile:
                    file_data = json.load(infile)
                    merged_files += file_data
        json.dump(merged_files, outfile)
    with open('mydata/0result.json', encoding='utf8') as file:
        history = json.load(file)
    return history

def artistsByTime(history):
    artists = {}
    for x in history:
        if x['artistName'] not in artists:
            artists[x['artistName']] = 0
    for x in artists:
        for y in history:
            if y['artistName'] == x:
                artists[x] += y['msPlayed']
    return artists

def songsByTime(history):
    songs = {}
    for x in history:
        if x['trackName'] not in songs:
            songs[x['trackName']] = 0
    for x in songs:
        for y in history:
            if y['trackName'] == x:
                songs[x] += y['msPlayed']
    return songs

def fastForward(history):
    songsMax = {}
    for x in history:
        if x['trackName'] not in songsMax and x['msPlayed'] > 30000:
            songsMax[x['trackName']] = 0
    for x in songsMax:
        for y in history:
            if y['trackName'] == x and y['msPlayed'] > songsMax[x]:
                songsMax[x] = y['msPlayed']
    fastForwardCount = {}
    for x in songsMax:
        fastForwardCount[x] = [0,0]
    for x in fastForwardCount:
        for y in history:
            if y['trackName'] == x and y['msPlayed'] < (songsMax[x] - 5000):
                fastForwardCount[x][0] += 1
            if y['trackName'] == x and y['msPlayed'] >= (songsMax[x] - 5000):
                fastForwardCount[x][1] += 1
    for x in sorted(fastForwardCount, key=fastForwardCount.get, reverse=True):
        percentage = (fastForwardCount[x][0]/(fastForwardCount[x][0] + fastForwardCount[x][1]))*100
        print(f"{x:<50} {fastForwardCount[x][0]}\({fastForwardCount[x][0]}+{fastForwardCount[x][1]}) {percentage:.2f}%")

def printBT(dict):
    for x in sorted(dict, key=dict.get, reverse=True):
        print("{:<100} {:<20}".format(x, msToHMS(dict[x])))

def totalTime(history):
    total = 0
    for x in history:
        total += x['msPlayed']
    return total

def dateSlice(start, end, dict):
    arr = []
    startDate = datetime.datetime.strptime(start, '%b %d %Y')
    endDate = datetime.datetime.strptime(end, '%b %d %Y')
    for x in dict:
        songTime = datetime.datetime.strptime(x['endTime'], '%Y-%m-%d %H:%M')
        if startDate < songTime < endDate:
            arr.append(x)
    return arr

def monthSlice(month, dict):
    arr = []
    for x in dict:
        songTime = datetime.datetime.strptime(x['endTime'], '%Y-%m-%d %H:%M')
        if songTime.month == month:
            arr.append(x)
    return arr

def hourSlice(hour, dict):
    arr = []
    for x in dict:
        songTime = datetime.datetime.strptime(x['endTime'], '%Y-%m-%d %H:%M') - datetime.timedelta(hours=6)
        if songTime.hour == hour:
            arr.append(x)
    return arr

def msToHMS(ms):
    hours = ((ms / 1000) / 60) / 60
    minutes = (hours % 1) * 60
    seconds = (minutes % 1) * 60
    time = f"{int(hours)}:{int(minutes):02}:{seconds:05.2f}"
    return time