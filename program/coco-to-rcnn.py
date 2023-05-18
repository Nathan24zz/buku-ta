def bounding_box_xywh_to_xyxy(bbox):
    x1, y1, w, h = bbox
    x2 = x1 + w
    y2 = y1 + h

    return [x1, y1, x2, y2]
