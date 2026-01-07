from ultralytics import YOLO

# Modeli yükle
model = YOLO("yolov8n.pt")

# Eğitimi başlat
model.train(
    data="brain-tumor.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    device=0,            # GPU kullanımı
    project="BrainTumor_Project",
    name="yolov8n_run"   # Klasör adı karışmasın
)