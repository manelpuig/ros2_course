#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args) # initialyse ROS2 communication
    node=Node('number_publisher')
    node.get_logger().info("Hello ROS2")
    rclpy.shutdown() # close ROS2 communications


if __name__ == '__main__':
    main()