n_1 = input()
n_2 = input()
n_3 = input()

list_1 = n_1.split()
#print(list_1)
list_2 = n_2.split()
#print(list_2)
list_3 = n_3.split()
#print(list_3)

if (list_1[0] == list_2[0] == list_3[0] == "O") or \
    (list_1[1] == list_2[1] == list_3[1] == "O") or \
    (list_1[2] == list_2[2] == list_3[2] == "O") or \
    (list_1[0] == list_2[1] == list_3[2] == "O") or \
    (list_1[2] == list_2[1] == list_3[0] == "O") or \
    (list_1[0] == list_1[1] == list_1[2] == "O") or \
    (list_2[0] == list_2[1] == list_2[2] == "O") or \
    (list_3[0] == list_3[1] == list_3[2] == "O"):
    print("Abhinav Wins")
elif (list_1[0] == list_2[0] == list_3[0] == "X") or \
    (list_1[1] == list_2[1] == list_3[1] == "X") or \
    (list_1[2] == list_2[2] == list_3[2] == "X") or \
    (list_1[0] == list_2[1] == list_3[2] == "X") or \
    (list_1[2] == list_2[1] == list_3[0] == "X") or \
    (list_1[0] == list_1[1] == list_1[2] == "X") or \
    (list_2[0] == list_2[1] == list_2[2] == "X") or \
    (list_3[0] == list_3[1] == list_3[2] == "X"):
    print("Anjali Wins")

else:
    print("Tie")