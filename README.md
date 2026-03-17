# Boto3 Learning Project

This repository contains small Python scripts for practicing AWS automation with `boto3`. The examples focus on two core areas:

- IAM user listing
- EC2 instance management

The code is written as simple learning exercises, so several scripts use hardcoded values such as the AWS profile name, AMI ID, and EC2 instance ID.

## Requirements

- Python 3
- `boto3`
- AWS credentials configured locally
- An AWS CLI profile named `default` for scripts that use `boto3.session.Session(profile_name="default")`

Install boto3 with:

```bash
pip install boto3
```

## Project Files

- `boto3_test.py`  
  Creates a basic boto3 session and lists IAM users with an IAM client.

- `console_management.py`  
  Imports `boto3_test` and uses an IAM resource interface to print user names.

- `iamapi.py`  
  Creates a session with the `default` profile and prints the result of `iam.list_users()`.

- `resouce-client.py`  
  Demonstrates both the IAM client and IAM resource approaches in one script.

- `describe_instances.py`  
  Lists EC2 instance IDs from `describe_instances()`.

- `launch_ec2.py`  
  Launches an EC2 instance using a hardcoded AMI ID and instance type.

- `start_ec2.py`  
  Starts a hardcoded EC2 instance.

- `stop_ec2.py`  
  Stops a hardcoded EC2 instance.

- `terminate_ec2.py`  
  Terminates a hardcoded EC2 instance.

## How To Run

Run any script directly with Python:

```bash
python iamapi.py
python describe_instances.py
python launch_ec2.py
```

## Important Notes

- Review all hardcoded AWS values before running the EC2 scripts.
- Launching, starting, stopping, or terminating EC2 instances can affect billing and availability.
- `console_management.py` imports `boto3_test.py`, so running it depends on that file being present and working as expected.
- This repository is best treated as a practice sandbox rather than production-ready automation.

## Suggested Improvements

- Move hardcoded instance IDs and AMI IDs into variables or environment variables.
- Add region configuration to each script.
- Add error handling for missing credentials and failed AWS API calls.
- Rename `resouce-client.py` to `resource-client.py` for clarity.
