import cv2
import argparse

def get_args():
    parser = argparse.ArgumentParser("Face Detection with opencv")
    i_desc = "Path to image- default = 1.png"
    parser._action_groups.pop()
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument("-i", help=i_desc, default=0)
    args = parser.parse_args()
    return args


args = get_args()
xpath = '/home/artichoke/Downloads/intel/face-detection-adas-0001/FP32/face-detection-adas-0001.xml'
bpath = '/home/artichoke/Downloads/intel/face-detection-adas-0001/FP32/face-detection-adas-0001.bin'
network = cv2.dnn.readNet(xpath, bpath)
network.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
cap = cv2.VideoCapture(args.i)
ret,frame = cap.read()
if ret:
    blob = cv2.dnn.blobFromImage(frame, size=(672, 384), ddepth=cv2.CV_8U)
    network.setInput(blob)
    out = network.forward()
    for det in out.reshape(-1, 7):
        conf = float(det[2])
        xmin = int(det[3] * frame.shape[1])
        ymin = int(det[4] * frame.shape[0])
        xmax = int(det[5] * frame.shape[1])
        ymax = int(det[6] * frame.shape[0])
        if conf > 0.5:
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), color=(0, 255, 0))
    cv2.imshow('frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

