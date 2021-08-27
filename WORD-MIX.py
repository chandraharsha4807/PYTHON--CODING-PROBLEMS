n = input()

#print(n)

string_list = n.split(" ")
#print(string_list)


#print(len(n))


for j in range(len(n)):
    for i in range(len(string_list)):
        if j < len(string_list[i]):
            new = string_list[i][j]
            
            print(new, end = "")
    print(end = " ")


'''

                  
Welcome to your first problem


W	t	y	f	p	Wtyfp
e	o	o	i	r	eooir
l		u	r	o	luro
c		r	s	b	crsb
o			t	l	otl
m				e	me
e				m	em


OUTPUT 

Wtyfp eooir luro crsb otl me em





'''  