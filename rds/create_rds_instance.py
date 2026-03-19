import boto3
from botocore.exceptions import ClientError

DB_INSTANCE_IDENTIFIER = "replace-with-new-rds-instance-id"
DB_INSTANCE_CLASS = "db.t3.micro"
ENGINE = "mysql"
MASTER_USERNAME = "replace-with-master-username"
MASTER_USER_PASSWORD = "replace-with-master-password"
ALLOCATED_STORAGE = 20

aws_management_console = boto3.session.Session(profile_name="default")
rds_console = aws_management_console.client(service_name="rds")

try:
    response = rds_console.create_db_instance(
        DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER,
        DBInstanceClass=DB_INSTANCE_CLASS,
        Engine=ENGINE,
        MasterUsername=MASTER_USERNAME,
        MasterUserPassword=MASTER_USER_PASSWORD,
        AllocatedStorage=ALLOCATED_STORAGE,
        PubliclyAccessible=False,
    )
    print(f"RDS instance creation started: {DB_INSTANCE_IDENTIFIER}")
    print(response)
except ClientError as error:
    print(f"Unable to create RDS instance {DB_INSTANCE_IDENTIFIER}: {error}")
