def keypoint_normalization(keypoints, img_size):
    kpts = []
    width,height = img_size
    for i in range(0, len(keypoints), 3):
        x,y,v = keypoints[i:i+3]
        if v == 0:
            kpts = kpts + ["{:.6f}".format(x/width),"{:.6f}".format(y/height), "{:.6f}".format(v)]
        else:
            kpts = kpts + ["{:.6f}".format(x/width),"{:.6f}".format(y/height), "{:.6f}".format(2)]
    return kpts

def bounding_box_normalization(bbox, img_size):
    lx,ly,w,h = bbox
    x = lx+(w/2)
    y = ly+(h/2)
    
    width,height = img_size
    
    dw = 1.0 / width
    dh = 1.0 / height

    x *= dw
    w *= dw
    y *= dh
    h *= dh

    return ["{:.6f}".format(x),"{:.6f}".format(y),"{:.6f}".format(w),"{:.6f}".format(h)]
