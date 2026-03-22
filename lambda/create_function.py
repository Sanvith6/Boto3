import os

import boto3
from botocore.exceptions import ClientError


DEFAULT_RUNTIME = "python3.12"
DEFAULT_HANDLER_FUNCTION = "lambda_handler"
DEFAULT_TIMEOUT = 30
DEFAULT_MEMORY_SIZE = 128


def create_function(
    function_name,
    role_arn,
    python_file_name,
    zip_file_path,
    runtime=DEFAULT_RUNTIME,
    timeout=DEFAULT_TIMEOUT,
    memory_size=DEFAULT_MEMORY_SIZE,
    description="Production Lambda function created with boto3",
):
    if not function_name:
        raise ValueError("function_name is required")
    if not role_arn:
        raise ValueError("role_arn is required")
    if not python_file_name:
        raise ValueError("python_file_name is required")
    if not zip_file_path:
        raise ValueError("zip_file_path is required")

    handler_name = f"{os.path.splitext(python_file_name)[0]}.{DEFAULT_HANDLER_FUNCTION}"

    with open(zip_file_path, "rb") as zip_file:
        zipped_code = zip_file.read()

    lambda_console = boto3.client("lambda")

    response = lambda_console.create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Role=role_arn,
        Handler=handler_name,
        Code={"ZipFile": zipped_code},
        Timeout=timeout,
        MemorySize=memory_size,
        Description=description,
        Publish=True,
    )

    return {
        "function_name": response["FunctionName"],
        "function_arn": response["FunctionArn"],
        "runtime": response["Runtime"],
        "handler": handler_name,
        "state": response.get("State", "Pending"),
    }


if __name__ == "__main__":
    FUNCTION_NAME = "orders-service"
    ROLE_ARN = "arn:aws:iam::123456789012:role/orders-lambda-role"
    PYTHON_FILE_NAME = "app.py"
    ZIP_FILE_PATH = "orders-service.zip"

    try:
        response = create_function(
            function_name=FUNCTION_NAME,
            role_arn=ROLE_ARN,
            python_file_name=PYTHON_FILE_NAME,
            zip_file_path=ZIP_FILE_PATH,
        )
        print("Lambda function created successfully")
        print(response)
    except (ValueError, FileNotFoundError, ClientError) as error:
        print(f"Unable to create Lambda function: {error}")
