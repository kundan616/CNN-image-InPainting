import numpy as np
import cv2
import os
import random
import pickle
i=1
image_folder='val2017/'
lis=os.listdir(image_folder)
print(len(lis))
data=[]
normdata=[]
for im_name in lis:
    imgn=cv2.imread(image_folder+im_name)
    img1=cv2.resize(imgn,(300,300))
    normdata.append(img1)
    cv2.imwrite('norm/{}.jpg'.format(i),img1)


    x1=np.floor(random.uniform(0, 1)*300)
    y1=np.floor(random.uniform(0, 1)*300)
    x2=np.floor(random.uniform(0, 1)*300*0.25)
    y2=np.floor(random.uniform(0, 1)*300*0.25)

    xmin=int(x1-x2)
    if x1-x2 <0:
        xmin=0

    ymin=int(y1-y2)
    if y1-y2<0:
        ymin=0

    xmax=int(x1+x2)
    if x1+x2>300:
        xmax=300
        
    ymax=int(y1+y2)
    if y1+y2>300:
        ymax=300    

    img1[xmin:xmax,ymin:ymax]=0

    
    cv2.imwrite('pro/{}.jpg'.format(i),img1)
    data.append(img1)
    print(i)
    i+=1
