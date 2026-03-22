import boto3
from botocore.exceptions import ClientError


DEFAULT_DB_INSTANCE_CLASS = "db.t3.micro"
DEFAULT_ENGINE = "mysql"
DEFAULT_ALLOCATED_STORAGE = 20
DEFAULT_MASTER_USERNAME = "adminuser"


def create_rds_instance(
    db_instance_identifier,
    master_user_password,
    db_instance_class=DEFAULT_DB_INSTANCE_CLASS,
    engine=DEFAULT_ENGINE,
    master_username=DEFAULT_MASTER_USERNAME,
    allocated_storage=DEFAULT_ALLOCATED_STORAGE,
):
    if not db_instance_identifier:
        raise ValueError("db_instance_identifier is required")
    if not master_user_password:
        raise ValueError("master_user_password is required")

    rds_console = boto3.client("rds")

    response = rds_console.create_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        DBInstanceClass=db_instance_class,
        Engine=engine,
        MasterUsername=master_username,
        MasterUserPassword=master_user_password,
        AllocatedStorage=allocated_storage,
        PubliclyAccessible=False,
    )

    db_instance = response["DBInstance"]
    return {
        "db_instance_identifier": db_instance["DBInstanceIdentifier"],
        "db_instance_class": db_instance["DBInstanceClass"],
        "engine": db_instance["Engine"],
        "db_instance_status": db_instance["DBInstanceStatus"],
    }


if __name__ == "__main__":
    DB_INSTANCE_IDENTIFIER = "orders-db"
    MASTER_USER_PASSWORD = "ReplaceWithSecurePassword123!"

    try:
        response = create_rds_instance(
            db_instance_identifier=DB_INSTANCE_IDENTIFIER,
            master_user_password=MASTER_USER_PASSWORD,
        )
        print("RDS instance creation started successfully")
        print(response)
    except (ValueError, ClientError) as error:
        print(f"Unable to create RDS instance: {error}")
