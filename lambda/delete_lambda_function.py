import boto3
from botocore.exceptions import ClientError

FUNCTION_NAME = "replace-with-lambda-function-name"

aws_management_console = boto3.session.Session(profile_name="default")
lambda_console = aws_management_console.client(service_name="lambda")

try:
    response = lambda_console.delete_function(FunctionName=FUNCTION_NAME)
    print(f"Lambda function deleted: {FUNCTION_NAME}")
    print(response)
except ClientError as error:
    print(f"Unable to delete Lambda function {FUNCTION_NAME}: {error}")
