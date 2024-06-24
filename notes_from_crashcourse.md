# Notes from crash course

## Setup

To be able to run `ros2`

```bash
source /opt/ros/humble/setup.bash
```

To be able to use colcon autocomplete

```bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

To be able to use custom package

```bash
source /home/andreas/learn-ros2/ros2_ws/install/setup.bash
```

Handle error warning SetuptoolsDeprecationWarning

```bash
pip3 install setuptools==58.2.0
```

## Create ROS 2 Python Package

```bash
ros2 pkg create <pkg_name>
```

Example:

```bash
ros2 pkg create my_robot_controller
```

Full arguments, specify python package using build-type ament_python, add dependency to rclpy
ament is a build system

```bash
ros2 pkg create my_robot_controller --build-type ament_python --dependencies rclpy
```

Side: install VS Code
```bash
sudo snap install code --classic
```

## What is a ROS2 Topic?

Prereq: run `ros2 run demo_node_cpp talker` and `ros2 run demo_node_cpp listener`

```bash
ros2 topic list
```

Return
> /chatter \
> /parameter_events \
> /rosout

Get topic info

```bash
ros2 topic info /chatter
```

Return
> Type: std_msgs/msg/String \
> Publisher count: 1 \
> Subscription count: 1

Get interface info

```bash
ros2 interface show std_msgs/msg/String
```

Return
> ros2 interface show std_msgs/msg/String \
> \# This was originally provided as an example message. \
> \# It is deprecated as of Foxy \
> \# It is recommended to create your own semantically meaningful message. \
> \# However if you would like to continue using this please use the equivalent in example_msgs. \
\
> string data

Get current topic publisher

```bash
ros2 topic echo /chatter
```

Return

> data: 'Hello World: 374' \
> --- \
> data: 'Hello World: 375' \
> --- \

## What is ROS2 Service?

Run demo node

```bash
ros2 run demo_nodes_cpp add_two_inits_server
```

Get list of service

```bash
ros2 service list
```

Return
> /add_two_ints \
> /add_two_ints_server/describe_parameters \
> /add_two_ints_server/get_parameter_types \
> /add_two_ints_server/get_parameters \
> /add_two_ints_server/list_parameters \
> /add_two_ints_server/set_parameters \
> /add_two_ints_server/set_parameters_atomically

Get service type

```bash
ros2 service type /add_two_ints
```

Return
> example_interfaces/srv/AddTwoInts

Get service type detail

```bash
ros2 interface show example_interfaces/srv/AddTwoInts
```

Return
> int64 a \
> int64 b \
> --- \
> int64 sum

Call the service

```bash
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts '{"a": 5, "b": 2}'
```

Return
> requester: making request: example_interfaces.srv.AddTwoInts_Request(a=5, b=2) \
> \
> response: \
> example_interfaces.srv.AddTwoInts_Response(sum=7)


## Write a ROS2 Service Clinet with Python

Find out how many times the topic subscriber get an update every second.

```bash
ros2 run turtlesim turtlesim_node
```

```bash
ros2 topic list
```

Return
> /parameter_events \
> /rosout \
> /turtle1/cmd_vel \
> /turtle1/color_sensor \
> /turtle1/pose 

```bash
ros2 topic hz /turtle1/pose
```

Return
> average rate: 62.437 \
> &nbsp;&nbsp;&nbsp;&nbsp;min: 0.014s max: 0.018s std dev: 0.00067s window: 64 \
> average rate: 62.521 \
> &nbsp;&nbsp;&nbsp;&nbsp;min: 0.014s max: 0.018s std dev: 0.00071s window: 127

It means that the topic `/turtle1/pose` get updated every 60times per second.
