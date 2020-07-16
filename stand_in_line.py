def next_in_line(lst, num):
    if lst == []:
        return "No list has been selected"
    else:
        return lst[1:] + [num]
