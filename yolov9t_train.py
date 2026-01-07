from ultralytics import YOLO

# Modeli yükle (YOLOv9)
model = YOLO("yolov9t.pt")

# Eğitimi başlat
model.train(
    data="brain-tumor.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    device=0,            # GPU kullanımı
    project="BrainTumor_Project",
    name="yolov9t_run"   # Klasör adı karışmasın
)