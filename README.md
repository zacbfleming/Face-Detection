# Face-Detection
Face detection trained model


The network features a default MobileNet backbone that includes depth-wise convolutions (3x3). Using opencv and the intermediate representation of the pretrained model for face detection.

Installation / Configuration

Copy the files in the manifest to the same folder and run ...

python3 f.py -i <path to image>
  
Manifest 
f.py
face-detection-adas-0001.xml
face-detection-adas-0001.bin

f.py requires opencv 4.0.1
