# voltage_shutdown
ROS2-subscriber to shutdown a system below a certaoin voltage level.

**Input:** Voltage level from a BatteryState topic \
**Output:** Shutdown command.

# ROS2 Package/Module Behaviour

# Prerequisite: Software
* Ubuntu 2.04 (64bit) or newer
* Robot Operating System 2, ROS2 (Version Humble)
* A ROS2-publisher for the voltage

## Dowload and install this ROS2 packages
Create a ROS2 workspace (in my exampel '~/ws_ros2/') \
Dowload ROS2 package by using 'git clone'

`Ubuntu Shell`
```
~$ mkdir -p ~/ws_ros2/src
~$ cd ~/ws_ros2/src
~/ws_ros2/src$ git clone https://github.com/Bjoerns-TB/voltage_shutdown.git
~/ws_ros2/src$ cd ..
~/ws_ros2$ colcon build --symlink-install
~/ws_ros2$ source /opt/ros/humble/setup.bash
~/ws_ros2$ source ./install/setup.bash
```

# ROS2 Launch sequence
`Ubuntu Shell #1`
```
$ ros2 run voltage_shutdown voltage_shutdown_node  
