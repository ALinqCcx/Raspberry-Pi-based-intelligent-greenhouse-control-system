# Raspberry-Pi-based-intelligent-greenhouse-control-system
## 基于树莓派的智能温室大棚控制系统

## 技术参数和设计要求
#### 1.检测并控制温室的温湿度
智能温室大棚控制系统通过温湿度传感器检测室内的温湿度值。系统根据温湿度传感器的检测值和阈值对比改变LED的颜色及蜂鸣器工作状态，判断是否需要增加温室大棚的温度和湿度。
#### 2.检测并控制温室的气压
气压的变化对植物的光合作用有着重要的影响。智能温室大棚控制系统通过气压传感器实时检测环境气压。并得出当前海拔。
#### 3.实时显示并记录
采集到的温湿度及气压参数显示在LCD上滚动显示，并以txt.形式保存日志。以便图形化显示。

## 工作量
树莓派调试，包括系统烧录、基本操作（屏幕、VNC、SSH）、网络连接、软件安装等；代码编写，包括在树莓派中的运行、调试；以及各个传感模块的调试。

## 工作安排
06.11 完成树莓派系统烧录，网络连接及相关调试
06.12 连接电路，并完成硬件调试及代码编写
06.13 对功能进行完善及修改，增加自启动程序
06.14 增加数据处理模块，并完成报告 


# 摘要
针对农业大棚温湿度信息易变、检测效率低的问题，设计了一种农业大棚空气温湿度智能控制系统，以快速精确地检测大棚内部环境信息，从而有效地提高棚内作物的产量。首先，分析了温湿度智能控制系统的需求，并对其整体结构进行规划与设计；然后，搭建该系统的硬件功能模块，包含温湿度检测模块、数码管显示模块、气压检测模块、电源模块、报警模块和摇杆控制模块，并对不同功能模块的软件进行设计，以驱动该系统正常工作。最后，对所设计的实物装置进行了温度与湿度检测试验。试验结果表明，所设计的智能控制系统具有灵敏度强与准确度高的特性。
关键词：环境检测；农业大棚；树莓派
