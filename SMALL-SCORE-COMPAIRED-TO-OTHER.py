def scores_less_than_other(list_s, number):
    temp = [0 for i in range(number)]
    for i in range(number):
        for j in range(i+1, number):
            if list_s[i]> list_s[j]:
                temp[i]+=1 
    print(*temp)

N = int(input())
list_s = list(map(int, input().split(" ")))
number = len(list_s)

scores_less_than_other(list_s, number)


'''

Given S = 13 12 11

Score of P1 is 13.
Score of P2 is 12.
Score of P3 is 11.

The number of people who played after P1 and scored less than 13 is 2(12, 11).
The number of people who played after P2 and scored less than 12 is 1(11).
The number of people who played after P3 and scored less than 11 is 0.

The output is 2 1 0

'''