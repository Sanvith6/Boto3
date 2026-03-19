import boto3
# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")



response = ec2_console.stop_instances(
    InstanceIds=['i-0b6bdf7f617f66513']
)