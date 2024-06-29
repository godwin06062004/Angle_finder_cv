import cv2
import math

path = 'white_background1.jpg'
img = cv2.imread(path)
img = cv2.resize(img,(0,0),None,10,10)
pointsList = []


def mousePoints(event,x,y,flagss,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size%3 != 0:
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,255,0),2) #important try it on yourself

        cv2.circle(img,(x,y),5,(255,46,0),cv2.FILLED)
        pointsList.append([x,y])
        print(pointsList)




# pts1 = x1,y1
# pts2 = x2,y2

def gradient(pt1,pt2):
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])


def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angR = math.atan((m2-m1)/(1+(m1*m2))) # angle in radince
    angD = round(math.degrees(angR))

    if angD < 0:
        angD = angD * -1

    cv2.putText(img,str(angD),(pt1[0]-40, pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,200),2)

    



while True:

    if len(pointsList)%3 == 0 and len(pointsList) != 0:
        getAngle(pointsList)
        

    cv2.imshow("image",img)
    cv2.setMouseCallback('image',mousePoints)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        pointsList = []
        img = cv2.imread(path)
        img = cv2.resize(img,(0,0),None,3,3,)

    if key == 27:
        break

cv2.destroyAllWindows()




# angle b/w two lines
# tan (theta) = | (m1 - m2) / (1 + m1*m2) |