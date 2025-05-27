from launch import LaunchDescription
from launch_ros.actions import Node
import time


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='kapal',
            executable='yolo_detector',
            name='yolo_detector',
            output='screen'
        ),
        Node(
            package='kapal',
            executable='decision_maker',
            name='decision_maker',
            output='screen'
        ),
        Node(
            package='kapal',
            executable='motor_controller',
            name='motor_controller',
            output='screen'
        )
    ])
for i in range(10):
    print(f"Output ke-{i}")
    time.sleep(1)  # Delay 1 detik
