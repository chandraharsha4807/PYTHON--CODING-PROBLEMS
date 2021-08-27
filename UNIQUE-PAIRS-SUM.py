def get_unique_pairs(num_list, pair_sum):
    stop_index = len(num_list) -1
    unique_pairs_set =set()
    for cur_index in range(stop_index):
        num_1 = num_list[cur_index]
        num_2 = pair_sum - num_1
        remaining_list = num_list[cur_index+1:]
        if num_2 in remaining_list:
            pair = (num_1, num_2)
            sorted_pair = tuple(sorted(pair))
            unique_pairs_set.add(sorted_pair)
            #print(unique_pairs_set)

    return unique_pairs_set

num_list = list(map(int, input().split()))
pair_sum = int(input())
unique_pairs = get_unique_pairs(num_list, pair_sum)
#print(num_list)
for pair in unique_pairs:
    print(" ".join((str(p) for p in pair)))
