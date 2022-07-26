from operator import sub
import math


def Required_line(p_1,angle,origin):
    m_0 = (math.tan((angle * math.pi) / 180))
    c_0 = origin[1] - m_0 * origin[0]
    slope_1 = map(sub, p_1[1], p_1[0])
    slope_1 = list(slope_1)
    m_1 = slope_1[1] / slope_1[0]
    # We are checking the lines will intersect or not
    a_1 = p_1[0][1] - m_0 * p_1[0][0] - c_0
    a_2 = p_1[1][1] - m_0 * p_1[1][0] - c_0
    c_1 = p_1[0][1] - m_1 * p_1[0][0]
    if ((a_1 * a_2) > 0):# The points of the lines segments are of same sign then it should not be included
        print("Line is excluded" )
    else:
        line_segment=[]
        line_segment.append(p_1)
    return (Distance(m_1,c_1,p_1,m_0,c_0,origin))

def Distance(m_1, c_1, p_1, m_0, c_0, origin):
    x_1 = (m_0-m_1)/(c_1-c_0)
    y_1 = m_0*(x_1)+c_0

    distance= math.sqrt((origin[0]-x_1)**2 + (origin[1]-y_1)**2) # Distance formula
    dist=[]
    dist.append(distance)
    return dist

all_line_segments = []
all_dist = []
origin=[]
for j in range(2):
    z = int(input("Enter Points for Origin ", ))
    origin.append(z)
print(origin)

angle =int(input("Enter direction :"))
p1=[]
d1=[]

n = int(input("Enter number Line Segments:"))
for k in range(n):
    input_list = []
    for i in range(2):
        list1 = []
        for j in range(2):
            z = int(input("Enter Points for line ",))
            list1.append(z)
        input_list.append(list1)
    p1 = input_list
    d1 = Required_line(p1,angle,origin)
    if(d1 == None):
        d1 = [100]
    all_line_segments.append(p1)
    all_dist.append(d1)

print("List of line segments", all_line_segments)
print("List of distances", all_dist)
min_dist=all_dist.index(min(all_dist))
print("Line segment nearest to the point ",origin," is ",all_line_segments[min_dist])















































