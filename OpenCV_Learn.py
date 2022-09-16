import cv2
import numpy as np

#three types of images
# 1-> black and white 0 and 1
# 2-> grey scale images 0 to 255
# 3-> rgb

#opencv work on numpy array


#Read an image

img = cv2.imread(r'C:\Users\VISH\Documents\mentorship\img/b11.jpg')

# print(img)  # show numpy area ..check by type(img)
# cv2.imshow("window", img)
# cv2.waitKey(0)

# #convert into greyscale image
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("window", img_gray)
# cv2.waitKey(0)
# print(img_gray.shape)   #(1235, 3395)

# img[:,:,0]=0  #blue wale channel ko 0 kr diya to baki 2 hi bache
# img[:,:,1]=0 #now green is 0
# cv2.imshow("window", img)
# cv2.waitKey(0)


# imgBlue = img[:,:,0]
# imgGreen = img[:,:,1]
# imgRed = img[:,:,2]
# new_img = np.hstack((imgBlue, imgGreen,imgRed))
# cv2.imshow("window", new_img)
# cv2.waitKey(0)


# #Resize
# img_resize = cv2.resize(img,(256,256))
# #to half the image  img.shape[1]//2, img.shape[0]//2
#
# cv2.imshow("window", img_resize)
# cv2.waitKey(0)


# #flip the image
#
# img_flip = cv2.flip(img,-1)  #0 -> ulta , 1 -> horizontal flip, -1 -> combine of both
# cv2.imshow("window", img_flip)
# cv2.waitKey(0)


# #crop the image
#
# img_crop = img[100:300,200:500]
# cv2.imshow("window", img_crop)
# cv2.waitKey(0)


# #save an image
#
# cv2.imwrite('iit_smal.jpg', img_crop)   #kis name se save, kisko krna hai


# #drawing shape (rectangle, square, circle...)
#
# img1 = np.zeros((512,512,3))  #create an image  (zeroes means black image)
#
# #Rectangle
# cv2.rectangle(img1,pt1=(100,100), pt2=(300,300),color=(255,0,0), thickness=3)  #color is blue ... as BGR order
# #thickness =-1 means filling
#
# #Circle
# cv2.circle(img1, center=(100,100),radius=50, color=(0,0,255), thickness=-1)
#
# #line
# cv2.line(img1, pt1=(0,0), pt2=(512,512), thickness=2, color=(0,255,0))
#
# #add text
#
# cv2.putText(img1, org=(200,100), fontScale=4, color= (0,255,255), thickness=2, lineType= cv2.LINE_AA,
#             text="Hello", fontFace = cv2.FONT_ITALIC)
# cv2.imshow('window',img1)
# cv2.waitKey(0)


#Live Direct Drawing

img2 = np.zeros((512,512,3))

# while True:
#     cv2.imshow("window",img2)
#
#     if cv2.waitKey(1) & 0xFF == ord('x'):   # 1 represt 1 milisecond
#         # press x to close
#         break
# cv2.destroyAllWindows()


# example2 to click ,move ,,,and some event on img
# def draw(event, x,y, flags, params):
#     # print("hello")
#     if event ==0:
#         print("Mouse moved")
#     elif event ==1:
#         # print("Mouse downclick")
#         cv2.circle(img2, center=(x, y), radius=50, color=(0, 0, 255), thickness=-1)
#     elif event ==4:
#         print("Mouse up clicked")  #mouse ko chhod rha
# cv2.namedWindow(winname= 'window')
# cv2.setMouseCallback("window", draw)   #check kr rha ki mouse click hua ya nhi
#
# while True:
#     cv2.imshow("window",img2)
#
#     if cv2.waitKey(1) & 0xFF == ord('x'):   # 1 represt 1 milisecond
#         # press x to close
#         break
# cv2.destroyAllWindows()


#example3 to draw ...

# drawing = False  #drwaing krna hai ya nhi
# ix=-1
# iy =-1
# def draw(event, x,y, flags, params):
#     global drawing, ix,iy
#     if event ==1:
#         drawing =True
#         ix = x
#         iy = y
#     elif event ==0:
#         if drawing == True:
#             cv2.rectangle(img2, pt1=(ix,iy),pt2=(x,y),color = (12,23,34),thickness=-1)
#     elif event ==4:
#         drawing = False
#         cv2.rectangle(img2, pt1=(ix,iy),pt2=(x,y), color=(12, 23, 34), thickness=-1)
# cv2.namedWindow(winname= 'window')
# cv2.setMouseCallback("window", draw)   #check kr rha ki mouse click hua ya nhi
#
# while True:
#     cv2.imshow("window",img2)
#
#     if cv2.waitKey(1) & 0xFF == ord('x'):   # 1 represt 1 milisecond
#         # press x to close
#         break
# cv2.destroyAllWindows()



# #Building Cropping Tool
#
# flag = False
# ix = -1
# iy =-1
# def crop(event,x,y, flags, params):
#     global ix,iy,flag
#     if event ==1:
#         flag = True
#         ix =x
#         iy =y
#
#     elif event ==4:
#         fx = x
#         fy = y
#         flag = False
#         cv2.rectangle(img, pt1 =(ix,iy), pt2 = (x,y), thickness=1, color=(0,0,0))
#         #crop tools
#         cropped = img[iy:fy, ix:fx]
#         cv2.imshow("new_window",cropped)
#         cv2.waitKey(0)
#
# cv2.namedWindow(winname="window1")
# cv2.setMouseCallback("window1", crop)
#
# while True:
#     cv2.imshow("window1", img)
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break
#
# cv2.destroyAllWindows()



#video
# #make video
# cap = cv2.VideoCapture(0)    # 0 means my webcam
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
#
# while True:
#     ret, frame = cap.read()
#     out.write(frame)
#     # print(ret)
#     # img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # black and white screen
#     # cv2.imshow("webcam", img_gray)
#     cv2.imshow("webcam",frame)
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break
#
# out.release()
# cv2.destroyAllWindows()



#to play video
import time

cap = cv2.VideoCapture('output.avi')
while True:
    ret, frame = cap.read()

    time.sleep(1/20)   # same speed se jesa save kiya tha 1/20 because 20 frame rate set kiya the ,yadi y fun use nhi karenge to fast chalenga
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()