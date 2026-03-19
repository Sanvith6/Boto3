import boto3
from botocore.exceptions import ClientError

aws_management_console = boto3.session.Session(profile_name="default")
s3_console = aws_management_console.client(service_name="s3")

try:
    response = s3_console.list_buckets()
    for bucket in response.get("Buckets", []):
        print(bucket["Name"])
except ClientError as error:
    print(f"Unable to list S3 buckets: {error}")
