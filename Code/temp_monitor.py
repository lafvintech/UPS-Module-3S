import time
import subprocess

# 定义函数获取树莓派CPU温度
def get_cpu_temperature():
    try:
        output = subprocess.check_output(['vcgencmd', 'measure_temp'])
        temp_str = output.decode('utf-8').strip()
        temp = float(temp_str.split('=')[1].replace("'C", ""))
        return temp
    except Exception as e:
        print(f"Error getting temperature: {e}")
        return None

# 主程序
def main():
    interval = 5  # 检测间隔（秒）
    summary_2min = 24  # 2分钟的检测次数
    summary_10min = 120  # 10分钟的检测次数

    temperatures = []  # 存储温度数据
    count_2min = 0  # 2分钟计数器
    count_10min = 0  # 10分钟计数器

    while True:
        temp = get_cpu_temperature()
        if temp is not None:
            temperatures.append(temp)
            print(f"Current Temperature: {temp:.2f}°C")

        # 每5秒检测一次
        time.sleep(interval)

        # 每2分钟总结一次平均温度
        count_2min += 1
        if count_2min >= summary_2min:
            avg_temp_2min = sum(temperatures[-summary_2min:]) / summary_2min
            print(f"Average Temperature over the last 2 minutes: {avg_temp_2min:.2f}°C")
            count_2min = 0

        # 每10分钟总结一次平均温度
        count_10min += 1
        if count_10min >= summary_10min:
            avg_temp_10min = sum(temperatures[-summary_10min:]) / summary_10min
            print(f"Average Temperature over the last 10 minutes: {avg_temp_10min:.2f}°C")
            count_10min = 0

if __name__ == "__main__":
    main()

