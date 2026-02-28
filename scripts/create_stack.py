import boto3

STACK_NAME = "django-multiapp-stack"

cf = boto3.client("cloudformation")
ec2 = boto3.client("ec2")

# Read template
with open("../cloudformation/template.yaml", "r") as f:
    template_body = f.read()


# Get default VPC
def get_default_vpc():
    response = ec2.describe_vpcs(
        Filters=[{"Name": "isDefault", "Values": ["true"]}]
    )
    return response["Vpcs"][0]["VpcId"]


# Get 3 subnets from VPC
def get_subnets(vpc_id):
    response = ec2.describe_subnets(
        Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
    )
    subnets = [subnet["SubnetId"] for subnet in response["Subnets"]]
    return subnets[:3]


# Check stack exists
def stack_exists(stack_name):
    try:
        cf.describe_stacks(StackName=stack_name)
        return True
    except:
        return False


# Create stack
def create_stack():

    vpc_id = get_default_vpc()
    subnets = get_subnets(vpc_id)

    parameters = [
        {"ParameterKey": "VPCId", "ParameterValue": vpc_id},
        {"ParameterKey": "Subnet1", "ParameterValue": subnets[0]},
        {"ParameterKey": "Subnet2", "ParameterValue": subnets[1]},
        {"ParameterKey": "Subnet3", "ParameterValue": subnets[2]},
    ]

    response = cf.create_stack(
        StackName=STACK_NAME,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=["CAPABILITY_NAMED_IAM"]
    )

    print("Stack creation started:", response["StackId"])


# Update stack
def update_stack():

    vpc_id = get_default_vpc()
    subnets = get_subnets(vpc_id)

    parameters = [
        {"ParameterKey": "VPCId", "ParameterValue": vpc_id},
        {"ParameterKey": "Subnet1", "ParameterValue": subnets[0]},
        {"ParameterKey": "Subnet2", "ParameterValue": subnets[1]},
        {"ParameterKey": "Subnet3", "ParameterValue": subnets[2]},
    ]

    response = cf.update_stack(
        StackName=STACK_NAME,
        TemplateBody=template_body,
        Parameters=parameters,
        Capabilities=["CAPABILITY_NAMED_IAM"]
    )

    print("Stack update started:", response["StackId"])


# Main logic
if stack_exists(STACK_NAME):
    update_stack()
else:
    create_stack()
