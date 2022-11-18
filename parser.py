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
        height, width = images[i]["height"], images[i]["width"]
        x, y, w, h = a["bbox"]
        h /= height
        w /= width
        center = x/width + w/2, y/height + h/2
        with open("./dataset/labels/" + s + '/' + str(name) + ".txt", 'a') as f:
            f.write("{} {} {} {} {}\n".format(
                int(a["category_id"]) - 1, center[0], center[1], w, h))


dir = ['./dataset/labels/train', './dataset/labels/val']
for d in dir:
    for f in os.listdir(d):
        os.remove(os.path.join(d, f))
parse("train")
parse("val")
