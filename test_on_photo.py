import cv2
import numpy as np
from test_on_video import filter_detected
'''
This code is useful for single case if multiple case scenerio need to modify the loop part from out in outs onwards
'''


#Take input path of the file so that we can get the path of the file and use it to be passed on the yolo model and predict weather required item found or not

image_path=input('Enter path of the Image: ')
image_path= r'{}'.format(image_path)
print(image_path)
img=cv2.imread(image_path)
height_original,width_original,_ = img.shape
# img = cv2.resize(img, None, fx=0.4, fy=0.4)
height, width, channels = img.shape

#Loading our weights as yolo Net Model  with having valid layers and outputlayer to give final output and classes present as well so that it can be useful to keep track of all the classes to be prediced
net = cv2.dnn.readNet("yolov3_best.weights", "yolov3.cfg")
classes = ["Mask","No-Mask"]
layer_names = net.getLayerNames()
output_layers = [layer_names[i-1] for i in net.getUnconnectedOutLayers()]

#Converting Image to Blob initially then passing it to our Yolo Network and taking the output from output_layers.
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

#outs is really complicated array basically all pixels represented in array so loop over them and find the place where confidence is max 

font = cv2.FONT_HERSHEY_SIMPLEX
detected = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence>0.9:
            # print(class_id,confidence,detection[0] * width,detection[1] * width) #Get class id confidence, center x and y position
            obj_name=classes[class_id] #Get obj name from classes list with class id index
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            detected.append([x,y,x+w,y+h,obj_name,confidence])
            # img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            # img = cv2.putText(img,obj_name,(x-5,y-5), font,1.5, (255,0,0), 2)         

    # print(f"Before : {detected}")

if detected != []:
    detected = filter_detected(detected)
print(f"    After: {detected}\n")
# print(detected)
for detects in detected:
    x1, y1, x2, y2, obj_name, confidence = detects
    print(detects)
    img = cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
    img = cv2.putText(img,f"{obj_name} ({int(confidence*100)}%)",(x1-5,y1-5), font,1, (255,0,0), 2)
    
imS = cv2.resize(img, (width_original, height_original))
cv2.imshow("output", imS)    
# cv2.imwrite("result.jpg",img)
key = cv2.waitKey(0)