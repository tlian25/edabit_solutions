def jazzify(lst):
    new_lst = []
    for s in lst:
        if s[-1] == '7':
            new_lst.append(s)
        else:
            new_lst.append(s + '7')
    
    return new_lst