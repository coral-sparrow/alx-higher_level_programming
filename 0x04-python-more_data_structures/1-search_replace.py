#!/usr/bin/python3

def search_replace(my_list, search, replace):
    t = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            t.append(replace)
            i += 1
            break
        else:
            t.append(my_list[i])
    if i == len(my_list) - 1:
        return t
    else:
        t += my_list[i:]
        return t
