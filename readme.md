# YOLOv3 based Mask and non-mask identifier

## About

It is simple implementation of YOLOv3 model for detecting masked perople apart from unmasked ones in real time. Thid sydtem can be useful for entrance in this pandemic.

## Useful Links

Do follow following links for dataset, model, and trained weight file.

[Dataset From Kaggle](https://www.kaggle.com/datasets/crained/wearingmaskc19)

[Trained Weight file](https://drive.google.com/file/d/1-H_DIlCpxvlFSbZKabNWZlG1ebniHzFH/view?usp=sharing)

[YOLO darknet from AlexeyAB](https://github.com/AlexeyAB/darknet)

## Requirements

- Python version 3.8

- Python libraries listed in requirements.txt

        pip install -r requirements.txt

- [Weight](https://drive.google.com/file/d/1-H_DIlCpxvlFSbZKabNWZlG1ebniHzFH/view?usp=sharing) file. ( If you do not want to train on your own )

## Training

Follow training steps as one by one from [Training_YOLOv3.ipynb](https://github.com/AnjaanKhadka/Face-mask-Detection-using-YOLOv3/blob/master/Training_YOLOv3.ipynb) file. ( Use of [Google colab](https://colab.research.google.com/) suggested )

## Inference

First you should download [Weight](https://drive.google.com/file/d/1-H_DIlCpxvlFSbZKabNWZlG1ebniHzFH/view?usp=sharing) file and keep it in the same folder. 

- To test on image execute [test_on_photo.py](https://github.com/AnjaanKhadka/Face-mask-Detection-using-YOLOv3/blob/master/test_on_photo.py) file.

        python test_on_photo.py

- To test on image execute [test_on_video.py](https://github.com/AnjaanKhadka/Face-mask-Detection-using-YOLOv3/blob/master/test_on_video.py) file.

        python test_on_video.py

## Results

### Outputs

#### Images

![Tested on image](https://github.com/AnjaanKhadka/Face-mask-Detection-using-YOLOv3/blob/master/images/result.jpg)

#### Video

https://user-images.githubusercontent.com/43941329/183263821-332da17f-9c01-47df-bd2d-ab47219bb066.mp4

#### Training Curve

![Training Curve](https://github.com/AnjaanKhadka/Face-mask-Detection-using-YOLOv3/blob/master/images/chart_yolov3.png)