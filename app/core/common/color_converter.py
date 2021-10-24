import cv2
import numpy


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % tuple(rgb)


def yuv_to_rgb(yuv):
    return cv2.cvtColor(numpy.uint8([[yuv]]), cv2.COLOR_YUV2RGB)[0][0]


def yuv_to_hex(yuv):
    rgb = yuv_to_rgb(yuv)
    return rgb_to_hex(rgb)
