"""Pose subscriber."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class PoseSubscriberNode(Node):
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subscriber_ = self.create_subscription(
            msg_type=Pose, topic="/turtle1/pose", callback=self.pose_callback, qos_profile=10
        )

    def pose_callback(self, msg:Pose):
        self.get_logger().info(f"({msg.x}, {msg.y})")


def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()
