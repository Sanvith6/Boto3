import boto3 
# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")
# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")



response = ec2_console.run_instances(
    ImageId='ami-0312bcacbe51d03c8',
    InstanceType='t3.micro',
    MinCount=1,
    MaxCount=1
    )
