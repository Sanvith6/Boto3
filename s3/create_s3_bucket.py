import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "replace-with-new-s3-bucket-name"
AWS_REGION = "us-east-1"

aws_management_console = boto3.session.Session(profile_name="default")
s3_console = aws_management_console.client(service_name="s3", region_name=AWS_REGION)

try:
    if AWS_REGION == "us-east-1":
        response = s3_console.create_bucket(Bucket=BUCKET_NAME)
    else:
        response = s3_console.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={"LocationConstraint": AWS_REGION},
        )
    print(f"S3 bucket created: {BUCKET_NAME}")
    print(response)
except ClientError as error:
    print(f"Unable to create S3 bucket {BUCKET_NAME}: {error}")
