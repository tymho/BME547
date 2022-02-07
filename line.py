def line(pt1, pt2, x):
    if pt1[0] > pt2[0]:
        slope = (pt1[1]-pt2[1])/(pt1[0]-pt2[0])
        return pt2[1] + slope * (x - pt2[0])
    else:
        slope = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        return pt1[1] + slope * (x - pt1[0])
