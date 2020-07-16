def correct_signs(txt):
    spt = txt.split(" ")

    length = int((len(spt) - 1) / 2)

    for i in range(length):
        a = float(spt[i*2])
        sign = spt[i*2 + 1]
        b = float(spt[i*2 + 2])

        if sign == "<":
            if a >= b:
                return False
        
        if sign == ">":
            if a <= b: 
                return False

    
    return True



