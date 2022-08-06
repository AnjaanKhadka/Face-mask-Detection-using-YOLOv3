import cv2
import numpy as np 
import pandas as pd
from itertools import product

# Calculating ratio of intersection of area with sum of areas. it is similar to IoU but calculations are faster as we need approx value only.
def intersection(boxA,boxB):
    area = 0
    Ax1,Ay1,Ax2,Ay2 = boxA
    Bx1,By1,Bx2,By2 = boxB
    a1 = (Ax2-Ax1)*(Ay2-Ay1)
    a2 = (Bx2-Bx1)*(By2-By1)
    dx = min(Ax2,Bx2) - max(Ax1,Bx1)
    dy = min(Ay2,By2) - max(Ay1,By1)
    if a1+a2>0:
        area = dx*dy/(a1+a2)*2
    if area > 0: return area
    else: return 0


# To remove boxes with high ratio of overlaping areas
def filter_detected(detected):
    
    df = pd.DataFrame.from_records(data = detected,columns=['xmin','ymin','xmax','ymax','obj_name','confidence'])
    # return detected
    # print(df)
    to_drop = []
    for (index, row), (index2, row2) in product(df.iterrows(), repeat=2):
        boxA = [row['xmin'], row['ymin'], row['xmax'], row['ymax']]
        boxB = [row2['xmin'], row2['ymin'], row2['xmax'], row2['ymax']]
        
        # print(f"boxA = {boxA}\nboxB = {boxB}\nArea = {intersection(boxA,boxB)}\n")
        
        if (intersection(boxA,boxB) >= 0.5 and row2['confidence'] < row['confidence']):
            to_drop.append(index2)
        
    for drops in to_drop:
        try:
            df.drop(drops, inplace=True)
        except:
            pass
    return df.values.tolist()
              
def detect():    
    cap = cv2.VideoCapture(0)

    #loading Deep Neural Network for Yolo weights and yolo config file with classes name specified and finally outputlayer connected.
    net = cv2.dnn.readNet("yolov3_best.weights", "yolov3.cfg")
    classes = ["Mask","No-Mask"]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]
    # print(output_layers)

    while True: 
        ret,img=cap.read()
        # img = cv2.resize(img, None, fx=0.6, fy=0.6)
        height, width, channels = img.shape
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)
        font = cv2.FONT_HERSHEY_SIMPLEX
        detected = []
        for out in outs:
            # detected = pd.DataFrame(columns=['xmin','ymin','xmax','ymax','obj_name','confidence'])
            for detection in out:
                # print(detection)
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                # print(type(confidence))
                if confidence>=0.8:
                    obj_name=classes[class_id] #Get obj name from classes list with class id index
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    # df1 = pd.DataFrame(data=[x,y,x+w,y+h,obj_name,confidence])
                    # # df1 = pd.DataFrame({'xmin':x,'ymin':y,'xmax':x+h,'ymax':y+w,'obj_name':obj_name,'confidence':confidence}) 
                    # detected.append(df1,ignore_index=True)
                    
                    detected.append([x,y,x+w,y+h,obj_name,confidence])
                    
                    # img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
                    # img = cv2.putText(img,obj_name,(x-5,y-5), font,0.5, (255,0,0), 1)            
        # print(f"Before: {detected}")
        if detected != []:
            detected = filter_detected(detected)
        # print(f"    After: {detected}\n")
        for detects in detected:
            x1, y1, x2, y2, obj_name, confidence = detects
            
            img = cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
            img = cv2.putText(img,f"{obj_name} ({int(confidence*100)}% )",(x-5,y-5), font,0.7, (255,0,0), 2)
    
        # if d == 1:
        #     break
        # img = cv2.resize(img,)   
        cv2.imshow('output',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    
    
    
if __name__ == "__main__":
    detect()