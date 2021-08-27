time = int(input())

Days = (time//86400)
time = time%(86400)
Hours = (time//3600)
time %= 3600
Minutes = (time//60)
time %= 60
Seconds = time

print("{} Days".format(Days),"{} Hours".format(Hours),"{} Minutes".format(Minutes),"{} Seconds".format(Seconds))


