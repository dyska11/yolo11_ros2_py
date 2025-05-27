cmake_minimum_required(VERSION 3.5)
project(kapal)

# Temukan dependensi yang diperlukan
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

# Install folder 'kapal' yang berisi Python script
install(DIRECTORY kapal/
  DESTINATION lib/${PROJECT_NAME}
  USE_SOURCE_PERMISSIONS
)

# Install folder 'launch'
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install file Python sebagai executable
install(PROGRAMS
  kapal/yolo_detector.py
  kapal/decision_maker.py
  kapal/motor_controller.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
