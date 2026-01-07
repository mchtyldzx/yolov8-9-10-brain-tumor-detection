from ultralytics import YOLO

# Modeli yükle (YOLOv10)
model = YOLO("yolov10n.pt")

# Eğitimi başlat
model.train(
    data="brain-tumor.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    device=0,
    project="BrainTumor_Project",
    name="yolov10n_run"
)