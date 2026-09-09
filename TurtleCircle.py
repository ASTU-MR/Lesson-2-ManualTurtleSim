import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class RurMover(Node):
    def __init__(self):
        super().__init__('rur_mover')
        self.publisher_twist = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.main()

    def main(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = -3.14
        self.publisher_twist.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    mover = RurMover()

    rclpy.spin(mover)

    mover.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()