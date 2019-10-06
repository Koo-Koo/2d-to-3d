import numpy as np
import cv2
import sys

hom = ""

# calculate line equation from two points
def regression(p1, p2):
    from scipy.stats import linregress
    p1, p2 = list(p1), list(p2)
    p = list()
    p.append(p1)
    p.append(p2)
    x_coords, y_coords = zip(*p)
    slope, intercept, r_value, p_value, std_err = linregress(x_coords, y_coords)
    return slope, intercept

def get_angle(points, cross):
    # calculate anlge to rotate models
    # we need to rotate models because the output of hmr is calculated 
    # as close as the input image; Since we are moving models on the plane
    # the user gave, we need to rotate models
    
    # line 1: top-left and bottom-left
    m1, c1 = regression(points[0], points[1])

    # line 2: top-right and bottom-right
    m2, c2 = regression(points[3], points[2])

    if m1 == m2:
        print('parallel error')
        return None
    
    # find vanishing point
    v = [(c2-c1)/(m1-m2), m1*((c2-c1)/(m1-m2))+c1]
    # line 3: vanishing point and cross point
    m3, c3 = regression(cross, v)
    
    theta = np.arctan2(1, m3)
    c,s = np.cos(theta), np.sin(theta)
    R = [[c, 0, s], [0, 1, 0], [-s, 0, c]]
    np.savetxt("cali/rotate.csv", R, delimiter=",")
    print("rotation matrix saved")

def get_h(points,w,h):
    global hom
    src_pts = np.array(points)
    dst_pts = np.array([[-w,h],[-w,-h],[w,-h],[w,h]])
    retval, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5)
    hom = retval        
    np.savetxt("cali/homography.csv", hom, delimiter=",")
    print("homography created")


def get_cross(points):
    # line1 : (x11,y11) (x12,y12) 
    # line2 : (x21,y21) (x22,y22)
    x11 = points[0][0]; y11 = points[0][1]
    x12 = points[2][0]; y12 = points[2][1]
    x21 = points[1][0]; y21 = points[1][1]
    x22 = points[3][0]; y22 = points[3][1]
    if x12==x11 or x22==x21:
        print('delta x=0')
        if x12==x11:
            cx = x12
            m2 = (y22 - y21) / (x22 - x21)
            cy = m2 * (cx - x21) + y21
            return cx, cy
        if x22==x21:
            cx = x22
            m1 = (y12 - y11) / (x12 - x11)
            cy = m1 * (cx - x11) + y11
            return cx, cy
        
    m1 = (y12 - y11) / (x12 - x11)
    m2 = (y22 - y21) / (x22 - x21)
    if m1==m2:
        print('parallel error')
        return None
    cx = (x11 * m1 - y11 - x21 * m2 + y21) / (m1 - m2)
    cy = m1 * (cx - x11) + y11
    p = np.array([cx,cy])
    np.savetxt("cali/crosspoint.csv",p,delimiter=',')
    print("crosspoint created")
    return p


def main():
    if len(sys.argv)!=3 :
        print("error")
        return
    w = float(sys.argv[1])
    h = float(sys.argv[2])
    points = []
    f = open("cali/points",'r')
    for _ in range(4):
        tmp = f.readline()
        tmp = list(tmp.strip("\n").split())
        tmp = [float(s) for s in tmp]
        points.append(tmp)
    get_h(points,w,h)
    p = get_cross(points)
    get_angle(points, p)
    

if __name__ =="__main__":
    main()