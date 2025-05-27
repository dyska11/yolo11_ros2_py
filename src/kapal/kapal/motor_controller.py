import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial
import time

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.listener_callback, 10)
        
        # Setup Serial ESP32 (sesuaikan port-nya)
        self.esp32 = serial.Serial('/dev/ttyUSB0', 9600)  # sesuaikan dengan port ESP32
        time.sleep(2)  # Waktu tunggu ESP32 siap
        self.get_logger().info("Connected to ESP32")

    def listener_callback(self, msg):
        linear_speed = msg.linear.x
        angular_speed = msg.angular.z
        self.get_logger().info(f'Received cmd_vel - Linear: {linear_speed}, Angular: {angular_speed}')

        if linear_speed > 0:
            self.maju()
        elif angular_speed > 0:
            self.kiri()
        elif angular_speed < 0:
            self.kanan()
        else:
            self.stop()

    def maju(self):
        self.esp32.write(b'maju\n')
        self.get_logger().info("Command sent: MAJU")

    def kiri(self):
        self.esp32.write(b'kiri\n')
        self.get_logger().info("Command sent: KIRI")

    def kanan(self):
        self.esp32.write(b'kanan\n')
        self.get_logger().info("Command sent: KANAN")

    def stop(self):
        self.esp32.write(b'stop\n')
        self.get_logger().info("Command sent: STOP")


def main(args=None):
    rclpy.init(args=args)
    node = MotorController()
    rclpy.spin(node)
    node.esp32.close()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
