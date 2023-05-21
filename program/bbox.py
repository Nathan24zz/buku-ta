def get_min_point(self, coords):

    min_x = 100000
    min_y = 100000

    for item in coords:
        if item[0] < min_x:
            min_x = item[0]

        if item[1] < min_y:
            min_y = item[1]
    return [int(min_x), int(min_y)]

def get_new_coords(self, coords, min_point):
    coords[:, :1] = coords[:, :1] - min_point[0]
    coords[:, 1:2] = coords[:, 1:2] - min_point[1]
    return coords

coords = # array with shape (6,2)
min_point = get_min_point(coords)
new_bounding_box = get_new_coords(coords, min_point)
