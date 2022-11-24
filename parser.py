import json
import os


def parse(s):
    with open("./dataset/annotations/instances_" + s + ".json") as f:
        data = json.load(f)

    images = data["images"]
    annotations = data["annotations"]
    i = 0
    for a in annotations:
        name = a["image_id"]
        if name != images[i]["id"]:
            i += 1
        # dataset provides us bounding boxes as absolute coordinates
        # of top left corner (x,y) and width and height dimensions in pixels.
        # However, YOLOv5 expects input as coordinates of the center of the rectange, width and height,
        # normalized to the total width and height of the image. So, coordinates and dimensions are values between 0 and 1.
        # Here we apply necessary conversion.
        height, width = images[i]["height"], images[i]["width"]
        x, y, w, h = a["bbox"]
        h /= height
        w /= width
        center = x/width + w/2, y/height + h/2
        with open("./dataset/labels/" + s + '/' + str(name) + ".txt", 'a') as f:
            # In the input dataset classes are enumerated starting from 1,
            # However, YOLOv5 expects us to enumerate them from 0.
            # Here we apply necessary shifting.
            f.write("{} {} {} {} {}\n".format(
                int(a["category_id"]) - 1, center[0], center[1], w, h))


dir = ['./dataset/labels/train', './dataset/labels/val']
for d in dir:
    for f in os.listdir(d):
        os.remove(os.path.join(d, f))
parse("train")
parse("val")
