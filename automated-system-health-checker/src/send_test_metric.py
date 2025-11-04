import boto3

cw = boto3.client("cloudwatch", region_name="ap-southeast-2")

try:
    cw.put_metric_data(
        Namespace="AutomatedSystemHealth",
        MetricData=[
            {"MetricName": "TestMetric", "Value": 1, "Unit": "Count"}
        ]
    )
    print("✅ Metric sent successfully!")
except Exception as e:
    print("❌ Failed to send metric:", e)
