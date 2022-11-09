import json


def parse(s):
    with open("./dataset/Annotations/instances_" + s + ".json") as f:
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
        x /= width
        y /= height
        h /= height
        w /= width
        with open("./dataset/labels/" + s + '/' + str(name) + ".txt", 'a') as f:
            f.write("{} {} {} {} {}\n".format(
                a["category_id"], x + w/2, y + h/2, x + w, y + h))


parse("train")
parse("val")
