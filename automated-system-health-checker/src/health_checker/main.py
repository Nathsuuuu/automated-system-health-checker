import time
import psutil
from health_checker import aws_client


def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return cpu, memory, disk


def run_forever(interval=10, max_iterations=5):
    for _ in range(max_iterations):
        cpu, memory, disk = get_system_stats()
        aws_client.put_metrics(cpu, memory, disk)
        aws_client.put_log({
            "CPUPercent": cpu,
            "MemoryPercent": memory,
            "DiskPercent": disk
        })
        time.sleep(interval)



if __name__ == "__main__":
    print("Starting Automated System Health Checker...")
    run_forever()
