import boto3

session = boto3.Session()

iam = session.client("iam")

for user in iam.list_users()["Users"]:
    print(user["UserName"])