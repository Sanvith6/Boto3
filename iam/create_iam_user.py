import boto3
from botocore.exceptions import ClientError

USER_NAME = "replace-with-new-iam-user-name"

aws_management_console = boto3.session.Session(profile_name="default")
iam_console = aws_management_console.client(service_name="iam")

try:
    response = iam_console.create_user(UserName=USER_NAME)
    print(f"IAM user created: {USER_NAME}")
    print(response)
except ClientError as error:
    print(f"Unable to create IAM user {USER_NAME}: {error}")
