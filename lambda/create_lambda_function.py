import boto3
from botocore.exceptions import ClientError

FUNCTION_NAME = "replace-with-new-lambda-function-name"
RUNTIME = "python3.12"
ROLE_ARN = "replace-with-lambda-execution-role-arn"
HANDLER_NAME = "lambda_function.lambda_handler"
ZIP_FILE_PATH = "replace-with-path-to-deployment-package.zip"

aws_management_console = boto3.session.Session(profile_name="default")
lambda_console = aws_management_console.client(service_name="lambda")

try:
    with open(ZIP_FILE_PATH, "rb") as zip_file:
        zipped_code = zip_file.read()

    response = lambda_console.create_function(
        FunctionName=FUNCTION_NAME,
        Runtime=RUNTIME,
        Role=ROLE_ARN,
        Handler=HANDLER_NAME,
        Code={"ZipFile": zipped_code},
        Publish=True,
    )
    print(f"Lambda function created: {FUNCTION_NAME}")
    print(response)
except FileNotFoundError:
    print(f"Deployment package not found: {ZIP_FILE_PATH}")
except ClientError as error:
    print(f"Unable to create Lambda function {FUNCTION_NAME}: {error}")
