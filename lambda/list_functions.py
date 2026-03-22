import boto3
from botocore.exceptions import ClientError


def list_functions():
    lambda_console = boto3.client("lambda")
    response = lambda_console.list_functions()

    functions = []
    for function in response.get("Functions", []):
        functions.append(
            {
                "function_name": function["FunctionName"],
                "runtime": function.get("Runtime"),
                "last_modified": function.get("LastModified"),
            }
        )

    return {
        "message": "Lambda functions fetched successfully",
        "count": len(functions),
        "functions": functions,
    }


if __name__ == "__main__":
    try:
        response = list_functions()
        print("Lambda functions listed successfully")
        print(response)
    except ClientError as error:
        print(f"Unable to list Lambda functions: {error}")
