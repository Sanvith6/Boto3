# Boto3 Learning Project 

This repository is a hands-on AWS learning project built with Python and `boto3`. It contains small service-based examples for working with IAM, EC2, S3, Lambda, and RDS.

The goal of the project is to help you understand how AWS resources are created, listed, updated, and deleted from Python code.

## Services Covered

- IAM user operations
- EC2 instance operations
- S3 bucket operations
- Lambda function operations
- RDS instance operations

## Project Structure

### `iam/`
IAM examples for learning user management and basic API access.

Files:
- `create_iam_user.py` - create an IAM user
- `delete_iam_user.py` - delete an IAM user
- `iamapi.py` - list IAM users with the IAM client
- `console_management.py` - simple management-console style client setup example
- `resouce-client.py` - resource/client learning example

### `ec2/`
EC2 examples for launching and managing instances.

Files:
- `launch_ec2.py` - launch an EC2 instance
- `describe_instances.py` - list instance details
- `start_ec2.py` - start an EC2 instance
- `stop_ec2.py` - stop an EC2 instance
- `terminate_ec2.py` - terminate an EC2 instance

### `s3/`
S3 examples for bucket management.

Files:
- `create_s3_bucket.py` - create an S3 bucket
- `list_s3_buckets.py` - list S3 buckets
- `delete_s3_bucket.py` - delete an S3 bucket

### `lambda/`
Lambda examples written in a cleaner application style.

Files:
- `app.py` - main Lambda entrypoint that routes create, delete, and list actions
- `create_function.py` - create an AWS Lambda function
- `delete_function.py` - delete an AWS Lambda function
- `list_functions.py` - list AWS Lambda functions

### `rds/`
RDS examples for creating, deleting, and listing DB instances.

Files:
- `create_rds_instance.py` - create an RDS DB instance
- `delete_rds_instance.py` - delete an RDS DB instance
- `list_rds_instances.py` - list RDS DB instances

## Requirements

- Python 3.10+
- `boto3`
- AWS account with permission to use IAM, EC2, S3, Lambda, and RDS
- AWS credentials configured locally with AWS CLI, environment variables, or an IAM role

Install dependencies:

```bash
pip install boto3
```

## AWS Configuration

You can configure AWS access in one of these ways:

1. AWS CLI credentials
2. Environment variables
3. IAM role when running inside AWS

Common AWS CLI setup:

```bash
aws configure
```

Example environment variables:

```bash
set AWS_ACCESS_KEY_ID=your_access_key
set AWS_SECRET_ACCESS_KEY=your_secret_key
set AWS_DEFAULT_REGION=ap-south-1
```

## How To Run

Run any script directly with Python from the project root.

Examples:

```bash
python iam/create_iam_user.py
python ec2/launch_ec2.py
python s3/create_s3_bucket.py
python lambda/create_function.py
python rds/create_rds_instance.py
```

## Lambda Application Flow

The `lambda/` folder contains both direct boto3 scripts and a deployable Lambda entrypoint.

### Main entrypoint

`lambda/app.py` exposes:

```python
lambda_handler(event, context)
```

It reads an `action` value from the event and routes to:
- `create_function`
- `delete_function`
- `list_functions`

### Example Lambda events

Create function:

```json
{
  "action": "create",
  "function_name": "orders-service",
  "role_arn": "arn:aws:iam::123456789012:role/orders-lambda-role",
  "python_file_name": "app.py",
  "zip_file_path": "orders-service.zip",
  "runtime": "python3.12",
  "timeout": 30,
  "memory_size": 128
}
```

Delete function:

```json
{
  "action": "delete",
  "function_name": "orders-service"
}
```

List functions:

```json
{
  "action": "list"
}
```

If you deploy the Lambda application in AWS, use this handler value:

```text
app.lambda_handler
```

## Code Style In This Project

This repository uses two learning styles:

- Simple script-style examples in folders like `ec2/`, `iam/`, and `s3/`
- Cleaner production-learning examples in `lambda/` and `rds/`

The newer Lambda and RDS files include:
- input validation
- clearer return values
- realistic example names
- better structure for reuse

## Important Notes

- Some files still contain placeholder values that must be replaced before running.
- Creating EC2, Lambda, RDS, and other AWS resources may incur AWS charges.
- `rds/delete_rds_instance.py` deletes the DB instance with `SkipFinalSnapshot=True`.
- `s3/delete_s3_bucket.py` works only when the bucket is empty unless additional object deletion logic is added.
- `lambda/create_function.py` expects the deployment zip to contain the Python file named in `python_file_name`.
- `resouce-client.py` contains a spelling mistake in the filename, but it is kept as-is to match the current project.

## Learning Outcomes

By working through this project, you can learn:
- how to authenticate AWS access with boto3
- how to create AWS service clients
- how to call AWS APIs from Python
- how to structure simple AWS automation scripts
- how to move from script-style code toward cleaner reusable code

## Suggested Next Improvements

- Add region configuration to every file
- Add `.env` or environment-based configuration
- Add request validation helpers shared across services
- Add tagging support for EC2, Lambda, and RDS resources
- Add exception handling for missing credentials and permissions
- Add unit tests with mocked boto3 clients
- Rename `resouce-client.py` to `resource-client.py`

## License

This project is distributed under the license included in [`LICENSE`](LICENSE).
