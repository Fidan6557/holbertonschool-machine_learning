#!/usr/bin/env python3
""" Object detection with YOLOv3"""
from tensorflow import keras as K


class Yolo:
    """ a class Yolo that uses the Yolo v3 
    algorithm to perform object detection """
    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        self.model = K.models.load_model(model_path)
        with open(classes_path, 'r') as f:
            self.class_names = [line.strip() for line in f.readlines()] 
            self.class_t = class_t
            self.nms_t = nms_t
            self.anchors = anchors
