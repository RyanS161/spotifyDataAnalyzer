from methods import *

dir = "MyData/"
total = parse(dir)


print(msToHMS(totalTime(total)))


#songs = songsByTime(total)
#printBT(songs)

'''
summer = dateSlice('May 5 2019', 'Aug 8 2019', total)

artists = artistsByTime(summer)
printBT(artists)

'''

'''
for x in range(24):
    month = hourSlice(x, total)
    print(x,msToHMS(totalTime(month)))
'''

#print(totalTime(day))
#artists = artistsByTime(day)
#printBT(artists)
#songs = songsByTime(history)
#printBT(songs)
