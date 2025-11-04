import boto3
import time
import json

AWS_REGION = "ap-southeast-2"
METRIC_NAMESPACE = "AutomatedSystemHealth"
LOG_GROUP = "AutomatedSystemHealthLogs"
LOG_STREAM = "HealthCheckerStream"

cw = boto3.client("cloudwatch", region_name=AWS_REGION)
logs = boto3.client("logs", region_name=AWS_REGION)


def _ensure_log_group():
    try:
        logs.create_log_group(logGroupName=LOG_GROUP)
        print(f"Created log group: {LOG_GROUP}")
    except logs.exceptions.ResourceAlreadyExistsException:
        pass


def _ensure_log_stream():
    try:
        logs.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)
        print(f"Created log stream: {LOG_STREAM}")
    except logs.exceptions.ResourceAlreadyExistsException:
        pass


def put_metrics(cpu, memory, disk):
    metric_data = [
        {"MetricName": "CPUPercent", "Value": cpu, "Unit": "Percent"},
        {"MetricName": "MemoryPercent", "Value": memory, "Unit": "Percent"},
        {"MetricName": "DiskPercent", "Value": disk, "Unit": "Percent"},
    ]
    print("Sending metrics:", cpu, memory, disk)
    try:
        cw.put_metric_data(Namespace=METRIC_NAMESPACE, MetricData=metric_data)
    except Exception as e:
        print("Failed to send metrics:", e)


def put_log(message: dict):
    _ensure_log_group()
    _ensure_log_stream()
    try:
        logs.put_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=LOG_STREAM,
            logEvents=[{"timestamp": int(time.time() * 1000), "message": json.dumps(message)}],
        )
    except Exception as e:
        print("Failed to send log:", e)
