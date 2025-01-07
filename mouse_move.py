import pyautogui
import time
import random
from pynput.mouse import Listener  # 导入pynput库中的Listener
import sys

# 定义一个标志来判断是否需要退出循环
stop_program = False

def on_click(x, y, button, pressed):
    global stop_program
    # 如果按下右键，则设置停止标志为True
    if button.name == 'right' and pressed:
        print("检测到右键点击，程序结束...")
        stop_program = True
        return False  # 返回False以停止监听

def random_mouse_move(interval=0.5):
    """
    让鼠标在屏幕上随机移动。

    :param interval: 每次移动之间的间隔时间（秒）
    """
    screen_width, screen_height = pyautogui.size()  # 获取屏幕尺寸

    # 开始监听鼠标事件
    with Listener(on_click=on_click) as listener:
        while not stop_program:  # 只有在 stop_program 为 False 时才继续移动
            # 生成随机的屏幕位置
            random_x = random.randint(0, screen_width - 1)
            random_y = random.randint(0, screen_height - 1)

            # 移动鼠标到随机位置
            pyautogui.moveTo(random_x, random_y, duration=random.uniform(1, 2))

            # 等待一段时间
            time.sleep(interval)

        listener.stop()  # 停止监听鼠标事件

if __name__ == '__main__':
    try:
        # 使用示例：每次移动间隔 10 秒
        random_mouse_move(interval=10)
    except KeyboardInterrupt:
        # 如果发生 Ctrl+C 中断
        print("程序已中断")
        sys.exit()
