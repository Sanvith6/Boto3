# Boto3 Learning Project

This repository contains small Python scripts for practicing AWS automation with `boto3`. The examples now cover:

- IAM user listing and deletion
- EC2 instance management
- S3 bucket listing and deletion
- Lambda function listing and deletion
- RDS instance listing and deletion

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

## Project Structure

- `iam/`  
  Contains IAM learning scripts:
  `boto3_test.py`, `console_management.py`, `iamapi.py`, `delete_iam_user.py`, and `resouce-client.py`

- `ec2/`  
  Contains EC2 learning scripts:
  `describe_instances.py`, `launch_ec2.py`, `start_ec2.py`, `stop_ec2.py`, and `terminate_ec2.py`

- `s3/`  
  Contains S3 learning scripts:
  `list_s3_buckets.py` and `delete_s3_bucket.py`

- `lambda/`  
  Contains Lambda learning scripts:
  `list_lambda_functions.py` and `delete_lambda_function.py`

- `rds/`  
  Contains RDS learning scripts:
  `list_rds_instances.py` and `delete_rds_instance.py`

## How To Run

Run any script directly with Python:

```bash
python iam/iamapi.py
python ec2/describe_instances.py
python ec2/launch_ec2.py
python s3/list_s3_buckets.py
python lambda/list_lambda_functions.py
python rds/list_rds_instances.py
```

## Important Notes

- Review all hardcoded AWS values before running scripts that delete or modify AWS resources.
- Launching, starting, stopping, terminating, or deleting AWS resources can affect billing and availability.
- `s3/delete_s3_bucket.py` only works on an empty bucket.
- `rds/delete_rds_instance.py` uses `SkipFinalSnapshot=True`, which permanently removes the DB instance without creating a final snapshot.
- `iam/console_management.py` imports `boto3_test.py`, so running it depends on that file being present in the same folder.
- This repository is best treated as a practice sandbox rather than production-ready automation.

## Suggested Improvements

- Move hardcoded instance IDs and AMI IDs into variables or environment variables.
- Add region configuration to each script.
- Add error handling for missing credentials and failed AWS API calls.
- Rename `resouce-client.py` to `resource-client.py` for clarity.
