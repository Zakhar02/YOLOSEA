## YOLO Sea Object Detection

python train.py --rect --epochs 3 --data ../dataset.yml --weights yolov5m-cls.pt --cfg models/yolov5m.yaml

--rect - for rectangular training, in contrast to mosaic, finds bounding box as a whole <br>
--weights - may be found on https://github.com/ultralytics/yolov5#pretrained-checkpoints
