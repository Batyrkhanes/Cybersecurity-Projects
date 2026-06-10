import psutil
import time
import subprocess
import json
import serial

ser = serial.Serial("COM4", 115200, timeout=1)


def get_gpu_nvidia():
    try:
        result = subprocess.check_output([
            "nvidia-smi",
            "--query-gpu=utilization.gpu",
            "--format=csv,noheader,nounits"
        ])

        return int(result.decode().strip())

    except:
        return 0


def collect_data():
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    down = (net2.bytes_recv - net1.bytes_recv) / 1024 / 1024
    up = (net2.bytes_sent - net1.bytes_sent) / 1024 / 1024

    gpu = get_gpu_nvidia()

    return {
        "cpu": int(cpu),
        "ram": f"{round(memory.used / (1024 ** 3), 1)}/{round(memory.total / (1024 ** 3), 2)}GB",
        "disk": f"{round(disk.used / (1024 ** 3), 0)}/{round(disk.total / (1024 ** 3), 0)}GB",
        "down": round(down, 2),
        "up": round(up, 2),
        "gpu": gpu
    }


while True:
    data = collect_data()
    ser.write((json.dumps(data) + "\n").encode())
    time.sleep(3)
