# ECS Django Multi App Deployment

## Prerequisites

Create ECR repositories:

app1
app2
app3

Example:

aws ecr create-repository --repository-name app1
aws ecr create-repository --repository-name app2
aws ecr create-repository --repository-name app3

## Push images

docker build -t app1 ./apps/app1
docker tag app1:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/app1:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/app1:latest

docker build -t app2 ./apps/app2
docker tag app2:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/app2:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/app2:latest

docker build -t app3 ./apps/app3
docker tag app3:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/app3:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/app3:latest

## Deploy stack

python scripts/create_stack.py

## Access apps

http://<ALB-DNS>
http://<ALB-DNS>/app1/
http://<ALB-DNS>/app2/
