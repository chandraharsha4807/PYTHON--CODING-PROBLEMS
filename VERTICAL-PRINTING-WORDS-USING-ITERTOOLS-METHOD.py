import itertools

txt = "MAM BY DORM"

l = txt.split(' ')

for i in itertools.zip_longest(*l, fillvalue=" "):
    if any(j != " " for j in i):
        print("".join(i))