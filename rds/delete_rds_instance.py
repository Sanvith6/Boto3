import boto3
from botocore.exceptions import ClientError

DB_INSTANCE_IDENTIFIER = "replace-with-rds-instance-id"

aws_management_console = boto3.session.Session(profile_name="default")
rds_console = aws_management_console.client(service_name="rds")

try:
    response = rds_console.delete_db_instance(
        DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER,
        SkipFinalSnapshot=True,
        DeleteAutomatedBackups=True,
    )
    print(f"RDS instance deletion started: {DB_INSTANCE_IDENTIFIER}")
    print(response)
except ClientError as error:
    print(f"Unable to delete RDS instance {DB_INSTANCE_IDENTIFIER}: {error}")
