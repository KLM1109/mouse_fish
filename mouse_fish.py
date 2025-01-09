import pyautogui
pyautogui.FAILSAFE=False

import time
import random
from pynput.mouse import Listener
from pynput.keyboard import Listener as KeyboardListener, Key
import sys

# 定义一个标志来判断是否需要退出循环
stop_program = False
last_event_time = None
keys_pressed = set()

def on_move(x, y):
    """
    鼠标移动事件处理函数
    """
    global last_event_time
    last_event_time = time.time()  # 更新最近的鼠标事件时间

def on_click(x, y, button, pressed):
    """
    鼠标点击事件处理函数
    """
    global stop_program, last_event_time
    if pressed:
        if button.name == 'middle':  # 检查是否按下鼠标中键
            print("检测到中键点击，程序退出...")
            stop_program = True
            return False  # 停止监听

    last_event_time = time.time()  # 更新最近的鼠标事件时间

def on_scroll(x, y, dx, dy):
    """
    鼠标滚动事件处理函数
    """
    global last_event_time
    print(f"鼠标滚动，位置：({x}, {y}) 滚动方向：({dx}, {dy})")
    last_event_time = time.time()  # 更新最近的鼠标事件时间

def random_mouse_move(interval, resume_delay):
    """
    让鼠标在屏幕上随机移动，监听鼠标事件以暂停与恢复。

    :param interval: 每次移动之间的间隔时间（秒）
    :param resume_delay: 停止鼠标移动后等待的时间（秒），默认是2分钟
    """
    global last_event_time, stop_program  # 添加 global 声明，引用全局变量

    screen_width, screen_height = pyautogui.size()  # 获取屏幕尺寸

    # 开始监听鼠标事件
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        while not stop_program:  # 只有在 stop_program 为 False 时才继续移动
            # 检查是否有鼠标事件发生，且暂停时间已满
            if last_event_time is not None:
                time_since_last_event = time.time() - last_event_time
                if time_since_last_event < resume_delay:
                    # 如果鼠标事件发生不到指定的延时，继续等待
                    time.sleep(1)
                    continue
                else:
                    # 2分钟后恢复鼠标移动
                    last_event_time = None  # 重置点击时间，恢复正常循环

            # 生成随机的屏幕位置
            print("鼠标随机移动----")
            random_x = random.randint(0, screen_width - 1)
            random_y = random.randint(0, screen_height - 1)

            # 移动鼠标到随机位置
            pyautogui.moveTo(random_x, random_y, duration=random.uniform(1, 2))

            # 等待一段时间
            print(f"等待一段时间：{interval}")
            time.sleep(interval)

        listener.stop()  # 停止鼠标事件监听

if __name__ == '__main__':
    try:
        # 使用示例：每次移动间隔 10 秒，监听到鼠标事件2分钟后才恢复
        random_mouse_move(interval=10, resume_delay=120)
    except KeyboardInterrupt:
        # 如果发生 Ctrl+C 中断
        print("程序已中断")
        sys.exit()
