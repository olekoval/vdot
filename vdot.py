import datetime

def find_vdot(tm:str, plst:list) -> int:
    i = 0
    j = 0
    while tm <= datetime.timedelta(hours = plst[i], minutes = plst[i + 1], seconds = plst[i + 2]):
        i = i + 3
        j = j + 1
        vdot = 29 + j
        if i > len(plst) - 1:
            break
    return vdot