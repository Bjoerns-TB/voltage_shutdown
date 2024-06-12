# ros2_voltage_shutdown
ROS2-subscriber to shutdown a system below a certaoin voltage level.

**Input:** Voltage level from a BatteryState topic \
**Output:** Shutdown command.

# ROS2 Package/Module Behaviour

# Prerequisite: Software
* Ubuntu 2.04 (64bit) or newer
* Robot Operating System 2, ROS2 (Version Humble)
* A ROS2-publisher for the voltage like the [pet_ros2_currentsensor](https://github.com/Pet-Series/pet_ros2_currentsensor_ina219_pkg)

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

## Parameters

```sh
# standalone executable
ros2 run voltage_shutdown voltage_shutdown_node --ros-args -p param1:=arg1 -p param2:=arg2
```

### Static Camera Stream Configuration

The camera stream is configured once when the node starts via the following static read-only parameters:

| name              | type                  | description |
| ----------------- | --------------------- |  ---------- |
| `topic`          | `string` | selects the topic [default: `/battery_status`]
| `voltage`            | `double`              | defines the voltage triggering the shutdown [default: `11.0`].
