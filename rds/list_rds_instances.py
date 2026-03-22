import boto3
from botocore.exceptions import ClientError


def list_rds_instances():
    rds_console = boto3.client("rds")
    response = rds_console.describe_db_instances()

    instances = []
    for instance in response.get("DBInstances", []):
        instances.append(
            {
                "db_instance_identifier": instance["DBInstanceIdentifier"],
                "engine": instance["Engine"],
                "db_instance_status": instance["DBInstanceStatus"],
                "db_instance_class": instance["DBInstanceClass"],
            }
        )

    return {
        "message": "RDS instances fetched successfully",
        "count": len(instances),
        "instances": instances,
    }


if __name__ == "__main__":
    try:
        response = list_rds_instances()
        print("RDS instances listed successfully")
        print(response)
    except ClientError as error:
        print(f"Unable to list RDS instances: {error}")
