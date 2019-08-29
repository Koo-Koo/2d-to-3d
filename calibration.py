import numpy as np
import cv2
import sys

hom = ""

def get_h(points,w,h):
    global hom
    src_pts = np.array(points)
    dst_pts = np.array([[-w,h],[-w,-h],[w,-h],[w,h]])
    retval, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5)
    hom = retval        
    np.savetxt("homography.csv", hom, delimiter=",")
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
    np.savetxt("crosspoint.csv",p,delimiter=',')
    print("crosspoint created")


def main():
    if len(sys.argv)!=3 :
        print("error")
        return
    w = float(sys.argv[1])
    h = float(sys.argv[2])
    points = []
    f = open("points",'r')
    for _ in range(4):
        tmp = f.readline()
        tmp = list(tmp.strip("\n").split())
        tmp = [float(s) for s in tmp]
        points.append(tmp)
    get_h(points,w,h)
    get_cross(points)
    

if __name__ =="__main__":
    main()