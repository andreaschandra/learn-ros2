# Notes from Docs

[Humble Docs](https://docs.ros.org/en/humble/index.html)

[Installation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)

## Tutorials

### Beginner: CLI Tools

Adding source to shell startup script.
Obj: biar ga `source /opt/ros/humble/setup.bash` tiap kali buka terminal

```
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

list executables
`ros2 pkg executables <package-name>`

Example:
```
ros2 pkg executables turtlesim
```

Return
```
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```

You can see the nodes, and their associated topics, services, and actions, using the list subcommands of the respective commands:

```
ros2 node list
ros2 topic list
ros2 service list
ros2 action list
```

### Beginner: Client libraries

Install colcon
```
sudo apt install python3-colcon-common-extensions
```

Build package
```
colcon build --symlink-install
```