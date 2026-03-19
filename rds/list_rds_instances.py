import boto3
from botocore.exceptions import ClientError

aws_management_console = boto3.session.Session(profile_name="default")
rds_console = aws_management_console.client(service_name="rds")

try:
    paginator = rds_console.get_paginator("describe_db_instances")
    for page in paginator.paginate():
        for instance in page.get("DBInstances", []):
            print(instance["DBInstanceIdentifier"])
except ClientError as error:
    print(f"Unable to list RDS instances: {error}")
