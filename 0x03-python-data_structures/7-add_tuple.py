#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    t_a = list(tuple_a)
    t_b = list(tuple_b)
    while len(t_a) < 2:
        t_a.append(0)
    if len(t_a) > 2:
        t_a = t_a[:2]

    while len(t_b) < 2:
        t_b.append(0)
    if len(t_b) > 2:
        t_b[:2]

    return ([x + y for x, y in in zip(t_a, t_p)])
