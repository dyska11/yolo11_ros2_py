import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from ultralytics import YOLO
import cv2
import time

# Mapping class ID ke warna dan nama
CLASS_MAP = {
    0: ("Bola Hijau", (0, 255, 0)),   # Hijau
    1: ("Bola Merah", (0, 0, 255))    # Merah
}

class YoloDetector(Node):
    def __init__(self):
        super().__init__('yolo_detector')
        self.publisher_ = self.create_publisher(String, '/direction', 10)
        self.model = YOLO('/home/f/Documents/dataset/runs/detect/train/weights/best.pt')
        self.cap = cv2.VideoCapture(2)

        if not self.cap.isOpened():
            self.get_logger().error('Could not open webcam.')
            exit()

        self.timer = self.create_timer(0.05, self.detect_callback)  # 20 Hz
        self.prev_time = time.time()

    def detect_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error('Failed to grab frame.')
            return

        # Prediksi objek dengan YOLO
        results = self.model.predict(frame, imgsz=640)

        green_detected = False
        red_detected = False

        for result in results[0].boxes.data:
            class_id = int(result[5])
            if class_id == 0:  # bolaHijau
                green_detected = True
            elif class_id == 1:  # bolaMerah
                red_detected = True

        direction = "stop"
        if green_detected and red_detected:
            direction = "forward"
        elif green_detected:
            direction = "left"
        elif red_detected:
            direction = "right"

        msg = String()
        msg.data = direction
        self.publisher_.publish(msg)
        self.get_logger().info(f'Detected direction: {direction}')

        # Tampilkan hasil deteksi bounding box di frame asli
        for box in results[0].boxes.data:
            x1, y1, x2, y2, _, class_id = map(int, box[:6])
            
            # Ambil warna dan nama class dari CLASS_MAP
            label, color = CLASS_MAP.get(class_id, ("Unknown", (255, 255, 255)))
            
            # Gambar bounding box dan label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

        # Hitung FPS
        curr_time = time.time()
        fps = 1.0 / (curr_time - self.prev_time)
        self.prev_time = curr_time

        # Tampilkan FPS di frame
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2, cv2.LINE_AA)

        # Tampilkan frame di window
        cv2.imshow("YOLO Detection", frame)

        # ESC buat keluar
        if cv2.waitKey(1) & 0xFF == 27:
            self.cap.release()
            cv2.destroyAllWindows()
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = YoloDetector()
    rclpy.spin(node)
    node.cap.release()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
