def addResult(teams, name, result):
    if name in teams:
        L = teams[name]
    else:
        L = [0, 0, 0]
    if result == 'win':
        L[0] += 1
    elif result == 'draw':
        L[1] += 1
    else:
        L[2] += 1
    teams[name] = L

def calcPoints(name, results):
    points = 3*results[0] + results[1]
    return (points, name, results)

def toString(teamRec):
    points, name, results = teamRec
    won, lost, draw = results
    played = won + lost + draw
    s = f'Team: {name}, Matches Played: {played}, Won: {won}, Lost: {draw}, Draw: {lost}, Points: {points}'
    return s
n = int(input()) 
teams = {}
if n == 0:
    print("No Output")
else:
    for i in range(n):
        line = input().split(';')
        team1 = line[0].strip()
        team2 = line[1].strip()
        result = line[2].strip()
        addResult(teams, team1, result)
        if result == 'win':
            result = 'loss'
        elif result == 'loss':
            result = 'win'
        addResult(teams, team2, result)

L = []
for name in teams:
    L.append(calcPoints(name, teams[name]))

L.sort(reverse=True)

for rec in L:
     print(toString(rec))