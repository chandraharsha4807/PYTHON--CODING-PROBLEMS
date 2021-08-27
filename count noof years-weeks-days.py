N = int(input())

#years = int(N/365)
weeks = int((N%365)/7)
days = int((N%365)%7)

#print("{} years".format(years))
print("{} days".format(days))
print("{} weeks".format(weeks))