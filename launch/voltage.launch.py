import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='voltage_shutdown',
            executable='voltage_shutdown_node',
            output='screen',
            parameters=[{
                'topic': '/battery_status',
                'voltage': 11.0
                }]
    )
    ])