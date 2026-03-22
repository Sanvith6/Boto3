import boto3
from botocore.exceptions import ClientError


def delete_function(function_name):
    if not function_name:
        raise ValueError("function_name is required")

    lambda_console = boto3.client("lambda")

    response = lambda_console.delete_function(
        FunctionName=function_name
    )

    return {
        "message": "Lambda function deletion started successfully",
        "function_name": function_name,
        "response_metadata": response.get("ResponseMetadata", {}),
    }


if __name__ == "__main__":
    FUNCTION_NAME = "orders-service"

    try:
        response = delete_function(FUNCTION_NAME)
        print("Lambda function deleted successfully")
        print(response)
    except (ValueError, ClientError) as error:
        print(f"Unable to delete Lambda function: {error}")
