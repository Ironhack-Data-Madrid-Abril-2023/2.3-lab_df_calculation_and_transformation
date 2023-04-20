def find_short(s):
    # your code here
    c = 0
    p = 0
    primera = 0
    for i in s:
        c +=1
        if i == ' ':
            if primera == 0:
                primera = 1
                p = c-1
                c = 0
            elif c < p:
                print('entro', c, p)
                p = c-1
                c = 0
            else:
                c = 0
    return p
find_short("Let's travel abroad shall we")