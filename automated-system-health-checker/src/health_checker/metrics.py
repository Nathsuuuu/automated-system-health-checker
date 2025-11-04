import psutil, time
from datetime import datetime

def sample_metrics():
    cpu = psutil.cpu_percent(interval=None)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    ts = int(time.time() * 1000)
    return {
        "timestamp_ms": ts,
        "cpu_percent": cpu,
        "memory_percent": mem,
        "disk_percent": disk,
        "iso_time": datetime.utcfromtimestamp(ts/1000).isoformat() + "Z"
    }
