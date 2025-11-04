# Automated System Health Checker

Monitors CPU, Memory, and Disk; sends metrics to AWS CloudWatch and logs to CloudWatch Logs.

## Quickstart
1. Create an IAM role with cloudwatch + logs permissions.
2. Configure AWS credentials or attach role to host.
3. Create a Python venv and install dependencies:
