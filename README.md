# Face-Detection
Face detection trained model


The network features a default MobileNet backbone that includes depth-wise convolutions (3x3). Using opencv and the intermediate representation of the pretrained model for face detection.

*** Openvino 2020.1 is required and env var should be sourced before execution

Installation / Configuration

Copy the files in the manifest to the same folder 

source <path> openvino/bin/setvars

and run ...

python3 f.py -i <path to image>


default video is 0, change to -i 1.png to use test image

Manifest 

1.png

f.py

face-detection-adas-0001.xml

face-detection-adas-0001.bin

requires opencv 4.0.1
