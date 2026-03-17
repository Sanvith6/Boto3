import boto3_test

iam_console = boto3_test.resource("iam")

for each_user in iam_console.users.all():
    print(each_user.name)