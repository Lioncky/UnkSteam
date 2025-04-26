import keyboard
import time

def main():
    print("等待按下Ctrl开始...")
    while not keyboard.is_pressed('ctrl'): time.sleep(0.1)
        
    print("按键模拟完成，0.5秒后启动操作...")
    time.sleep(0.5)
    while True:
        
        if keyboard.is_pressed('ctrl'):
            print("Ctrl 键被按下，停止脚本。")
            break
        
        keyboard.press('down')
        time.sleep(0.2)
        keyboard.release('down')
        time.sleep(0.1)

main()
