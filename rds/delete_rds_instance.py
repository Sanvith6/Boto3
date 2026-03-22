import boto3
from botocore.exceptions import ClientError


def delete_rds_instance(db_instance_identifier):
    if not db_instance_identifier:
        raise ValueError("db_instance_identifier is required")

    rds_console = boto3.client("rds")

    response = rds_console.delete_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        SkipFinalSnapshot=True,
        DeleteAutomatedBackups=True,
    )

    db_instance = response["DBInstance"]
    return {
        "db_instance_identifier": db_instance["DBInstanceIdentifier"],
        "db_instance_status": db_instance["DBInstanceStatus"],
        "message": "RDS instance deletion started successfully",
    }


if __name__ == "__main__":
    DB_INSTANCE_IDENTIFIER = "orders-db"

    try:
        response = delete_rds_instance(DB_INSTANCE_IDENTIFIER)
        print("RDS instance deletion started successfully")
        print(response)
    except (ValueError, ClientError) as error:
        print(f"Unable to delete RDS instance: {error}")
