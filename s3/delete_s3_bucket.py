import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "replace-with-s3-bucket-name"

aws_management_console = boto3.session.Session(profile_name="default")
s3_console = aws_management_console.client(service_name="s3")

try:
    response = s3_console.delete_bucket(Bucket=BUCKET_NAME)
    print(f"S3 bucket deleted: {BUCKET_NAME}")
    print(response)
except ClientError as error:
    print(f"Unable to delete S3 bucket {BUCKET_NAME}: {error}")
