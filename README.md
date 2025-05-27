# 🔍 YOLOv11 ROS 2 Python Object Detection

Python-based object detection node using YOLOv11 integrated with ROS 2.  
This project allows real-time object detection and publishing detection results as ROS 2 messages.

---

## ✅ Features

- 🔎 Object detection using YOLOv11 (PyTorch)
- 🧠 Real-time inference on live camera or video feed
- 🛰️ ROS 2 publisher for detection results (`sensor_msgs/msg/Image`, `custom_msgs`, etc.)
- 🎯 Easy to modify for robot applications

---

## ⚙️ Tools & Dependencies

Pastikan sistem Anda sudah memiliki hal berikut:

- ✅ **Python 3.8+**
- ✅ **ROS 2** (Foxy, Humble, atau kompatibel)
- ✅ **YOLOv11** (versi PyTorch)
- ✅ **Pip packages**:
  - `torch` dan `torchvision`
  - `opencv-python`
  - `numpy`
  - `cv_bridge` (ROS 2 Python binding)
  - `rclpy` (ROS 2 Python client library)

Install semua dependency Python dengan:
```bash
pip install torch torchvision opencv-python numpy
Pastikan juga cv_bridge sudah terinstall via ROS 2:

sudo apt install ros-${ROS_DISTRO}-cv-bridge
Model Setup

    Download YOLOv11 model .pt (hasil training custom atau pre-trained)
    Contoh:

yolov11/
└── best.pt

Sesuaikan path model di script Python Mas (misalnya di main.py):

    model = torch.hub.load('path/to/yolov11', 'custom', path='yolov11/best.pt')

    Tambahkan file label kalau perlu (coco.names, dll.)

🔨 Build Instructions

Karena ini node Python, tidak perlu di-compile. Cukup letakkan dalam struktur package ROS 2.

Contoh struktur:

ros2_ws/
└── src/
    └── yolo11_ros2_py/
        ├── yolo11_ros2_py/
        │   └── main.py
        ├── package.xml
        └── setup.py

Build workspace:

cd ~/ros2_ws
colcon build
source install/setup.bash

🚀 Running the Node

Jalankan node deteksi:

ros2 run yolo11_ros2_py main
