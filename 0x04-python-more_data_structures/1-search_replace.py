#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        t = []
        for i in range(len(my_list)):
            if my_list[i] == search:
                t.append(replace)
            else:
                t.append(my_list[i])
        return t
    else:
        return None
