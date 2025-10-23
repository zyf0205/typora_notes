# 鱼香ros一键安装脚本

```plain
wget http://fishros.com/install -O fishros && . fishros
```

# 小海龟

rosrun turtlesim turtlesim_node

rosrun turtlesim turtle_teleop_key

# 图形化查看节点

rqt_graph

# 简单指令

rosnode list

rostopic list

rosnode info /turtlesim

# 工作空间

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742789595673-44b04fec-6361-425c-b5c7-21d54577da51.png)

## 创建工作空间：（工作空间>功能包）

mkdir -p catkin_ws/src

cd catkin_ws/

cd src

catkin_init_workspace 

## 编译工作空间

cd 工作空间

catkin_make 编译

catkin_make install 生成install文件夹

## 创建功能包（放在src里面）：

cd src/

catkin_create_pkg test_pkg roscpp rospy std_msgs std_msgs geometry_msgs turtlesim(后面是依赖)

## 编译功能包

cd 工作空间

catkin_make 

## 添加环境变量

按照如下添加环境变量就可以愉快使用了

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742790566898-8d9ea80a-fa30-446f-942a-8878c52fbdcf.png)

# 话题

## 创建发布者

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742804971911-5b41820d-d2dc-4611-b275-c8472faf2d37.png)

## 编译前提

在功能包的CMakeLists.txt中的【install】上面添加下面两句语句

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742805201776-69d41ca1-cef0-4892-b759-6153f61be5f3.png)

add_executable(velocity_publisher src/velocity_publisher.cpp)  将src/velocity_publisher.cpp编译为可执行velocity_publisher

target_link_libraries(velocity_publisher ${catkin_LIBRARIES}) 将可执行velocity_publisher与catkin_LIBRARIES链接

## 创建订阅者

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742806493583-18fa037e-e22d-4069-8a23-b4c6f12aa2de.png)

# 自定义话题消息

在功能包中创建msg文件夹方便管理

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742806662879-f207830c-fcfa-4849-b34b-2425c70ad877.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742806555616-9825f52a-d046-44d4-a8c6-c665f28b5b81.png)

创建msg文件：

touch Person.msg

消息定义示例：

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742806967364-e29713a3-bab5-4b0c-a6d1-1100f7f378db.png)

在package.xml中添加功能包依赖

<build_depend>message_generation</build_depend>

<exec_depend>message_runtime</exec_depend>

如果使用了自定义消息类型还要添加这一句

add_dependencies(pose_subscriber ${PROJECT_NAME}_generate_messages_cpp)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742807336852-b5cf655e-428f-4932-bbd6-50b9491229dc.png)

在CMakeLists.txt中添加

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742807725006-aab4287e-b7c5-458f-a4ea-63cc74cab1a2.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742807738708-5ae1bd8f-0f80-4a08-bad1-92c8c31813a2.png)

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742807678770-be13661d-c606-47bf-b0b1-710859b76a36.png)

# 服务

rosservice相关指令

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742824342616-74c68f7d-92d0-4013-a35d-28c2cccac9f3.png)

示例

rosservice call /clear "{}"

# 参数模型

在同一个ros环境中，每一个节点都可以访问ros master中的参数

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742823753302-42801601-8ae2-4503-b3d7-4e856ce568c1.png)

与参数有关的rosparam指令

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742823968886-84f73bb5-73ed-4c28-87b0-67f4894d287c.png)

将参数保存到文件中

rosparam dump param.yaml

将参数从文件中加载

rosparam load param.yaml

# 坐标系管理

查看两个海龟的相对位置

rosrun tf tf_echo turtle1 turtle2

打开rviz

rosrun rviz rviz -d $(rospack find turtle_tf)/rviz/turtle_rviz.rviz

![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742826817165-5b04aa49-d27a-4a8f-ac24-f30e8b279b41.png)

# launch启动![img](https://cdn.nlark.com/yuque/0/2025/png/50704934/1742827045210-337bbae9-ecbd-4304-9e9b-1a85224ab674.png)

output:是否打印日志

respawn：挂掉了是否重启

required：。。。。。。