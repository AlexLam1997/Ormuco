
def isOverlapping(x11, x12, x21, x22):
    #(x11, x12) is closer to the origin than (x21, x22)
    if min (x21, x22) <= max(x11,x12) and min(x21,x22) >= min(x11,x12):
        return True

    if max(x21,x22) >= min(x11, x12) and max(x21,x22) <= max(x11,x12):
        return True
    return False
