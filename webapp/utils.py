def owr(orig_list):
    for i in range(len(orig_list)//2):
        swap = orig_list[i]
        orig_list[i] = orig_list[-i-1]
        orig_list[-i-1] = swap
    return orig_list
