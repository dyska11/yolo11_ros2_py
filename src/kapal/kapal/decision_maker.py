import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class DecisionMaker(Node):
    def __init__(self):
        super().__init__('decision_maker')
        self.subscription = self.create_subscription(String, '/direction', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

    def listener_callback(self, msg):
        twist = Twist()
        if msg.data == "forward":
            twist.linear.x = 0.5
            twist.angular.z = 0.0
        elif msg.data == "left":
            twist.linear.x = 0.0
            twist.angular.z = 0.5
        elif msg.data == "right":
            twist.linear.x = 0.0
            twist.angular.z = -0.5
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0

        self.publisher_.publish(twist)
        self.get_logger().info(f'Published cmd_vel: linear={twist.linear.x}, angular={twist.angular.z}')


def main(args=None):
    rclpy.init(args=args)
    node = DecisionMaker()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
