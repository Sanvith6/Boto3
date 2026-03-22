import json

from botocore.exceptions import ClientError

from create_function import create_function
from delete_function import delete_function
from list_functions import list_functions


def lambda_handler(event, context):
    body = event.get("body", event)
    if isinstance(body, str):
        body = json.loads(body)

    action = body.get("action")

    try:
        if action == "create":
            response = create_function(
                function_name=body.get("function_name"),
                role_arn=body.get("role_arn"),
                python_file_name=body.get("python_file_name"),
                zip_file_path=body.get("zip_file_path"),
                runtime=body.get("runtime", "python3.12"),
                timeout=body.get("timeout", 30),
                memory_size=body.get("memory_size", 128),
                description=body.get("description", "Production Lambda function created with boto3"),
            )
        elif action == "delete":
            function_name = body.get("function_name")
            if not function_name:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"message": "function_name is required"})
                }
            response = delete_function(function_name)
        elif action == "list":
            response = list_functions()
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "action must be create, delete or list"})
            }

        return {
            "statusCode": 200,
            "body": json.dumps(response, default=str)
        }
    except ValueError as error:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": str(error)})
        }
    except FileNotFoundError:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "zip_file_path not found"})
        }
    except ClientError as error:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(error)})
        }
