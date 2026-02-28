import boto3

STACK_NAME = "django-multiapp-stack"

cf = boto3.client("cloudformation")

with open("../cloudformation/template.yaml", "r") as f:
    template_body = f.read()

try:
    response = cf.create_stack(
        StackName=STACK_NAME,
        TemplateBody=template_body,
        Capabilities=["CAPABILITY_NAMED_IAM"]
    )
    print("Stack creation started")

except cf.exceptions.AlreadyExistsException:

    response = cf.update_stack(
        StackName=STACK_NAME,
        TemplateBody=template_body,
        Capabilities=["CAPABILITY_NAMED_IAM"]
    )

    print("Stack update started", response["StackId"])
