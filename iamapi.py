# Import all the modules and Libraries
import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

# Open IAM Console
iam_console = aws_management_console.client(service_name="iam")

# Call IAM API
result = iam_console.list_users()

print(result)