#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# －－－－湖南创乐博智能科技有限公司－－－－
#  文件名：27_humiture.py
#  版本：V2.0
#  author: zhulin
# 说明：湿度传感器检测实验
#####################################################
import Adafruit_DHT
import time
import RPi.GPIO as GPIO  # Import GPIO library

makerobo_pin = 16  # DHT11 温湿度传感器管脚定义

# GPIO口定义
def makerobo_setup():
    global sensor
    sensor = Adafruit_DHT.DHT11
def get_temperature_and_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, makerobo_pin)
    if humidity is not None and temperature is not None:
        return temperature,humidity
    else:
        return None,None

# 循环函数
def loop():
    while True:
        temperature,humidity = get_temperature_and_humidity()
        if humidity is not None and temperature is not None:
            print('Temperature: {0:0.1f}°C  Humidity: {1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
        time.sleep(1)  # 延时1s

def destroy():
    GPIO.cleanup()  # 释放资源

# 程序入口
if __name__ == '__main__':
    makerobo_setup()
    try:
        loop()
    except KeyboardInterrupt:  # 当按下Ctrl+C时，将执行destroy()子程序。
        destroy()