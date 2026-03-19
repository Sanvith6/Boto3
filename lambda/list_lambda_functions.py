import boto3
from botocore.exceptions import ClientError

aws_management_console = boto3.session.Session(profile_name="default")
lambda_console = aws_management_console.client(service_name="lambda")

try:
    paginator = lambda_console.get_paginator("list_functions")
    for page in paginator.paginate():
        for function in page.get("Functions", []):
            print(function["FunctionName"])
except ClientError as error:
    print(f"Unable to list Lambda functions: {error}")
