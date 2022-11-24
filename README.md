## YOLO Sea Object Detection
<a target="_blank" href="https://colab.research.google.com/github/vBazilevich/Fall2022-CV-FinalProjectDemo/blob/master/Introduction_to_CV_On_Sea_object_detection_Live_demo.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

```
python train.py --rect --data ../dataset.yml --weights yolov5m-cls.pt --cfg models/yolov5m.yaml
```

`--rect` - for rectangular training, in contrast to mosaic, finds bounding box as a whole <br>
`--weights` - may be found on https://github.com/ultralytics/yolov5#pretrained-checkpoints
