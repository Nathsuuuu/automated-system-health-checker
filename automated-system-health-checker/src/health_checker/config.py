import os
METRIC_NAMESPACE = os.getenv("METRIC_NAMESPACE", "AutomatedSystemHealth")
LOG_GROUP = os.getenv("LOG_GROUP", "/automated/system-health")
LOG_STREAM = os.getenv("LOG_STREAM", "instance-logs")
SAMPLE_INTERVAL_SECONDS = int(os.getenv("SAMPLE_INTERVAL_SECONDS", "30"))
AWS_REGION = os.getenv("AWS_REGION", "ap-southeast-2")
