from sentence_transformers import SentenceTransformer, util
import json

Permission_Descriptions = {
    "s3:ListBucket": "Allows listing or viewing all files, folders, or objects inside an Amazon S3 bucket.",
    "s3:GetObject": "Allows reading, downloading, or retrieving objects stored in an Amazon S3 bucket.",
    "s3:PutObject": "Allows uploading, sending, or adding new files or objects into an Amazon S3 bucket.",

    "ec2:DescribeInstances": "Allows viewing or describing details of running or stopped Amazon EC2 virtual machines.",
    "ec2:StartInstances": "Allows starting, launching, or powering on stopped Amazon EC2 instances.",
    "ec2:StopInstances": "Allows stopping or shutting down running Amazon EC2 instances.",

    "lambda:InvokeFunction": "Allows executing, running, or invoking AWS Lambda functions to process events or requests.",

    "dynamodb:Query": "Allows querying, reading, or retrieving items from a DynamoDB table based on a key or condition.",
    "dynamodb:PutItem": "Allows writing, inserting, or adding a new item or record into a DynamoDB table.",

    "logs:CreateLogStream": "Allows creating new log streams in AWS CloudWatch to store application logs.",
    "logs:PutLogEvents": "Allows writing, pushing, or sending log events to AWS CloudWatch Logs.",

    "cloudwatch:GetMetricData": "Allows retrieving or viewing metric data, charts, and statistics from AWS CloudWatch.",

    "iam:ChangePassword": "Allows a user to change, update, or reset their own IAM account password.",
    "iam:GetUser": "Allows viewing details and settings of the currently logged-in IAM user account.",

    "sns:Publish": "Allows publishing, sending, or pushing messages to an SNS topic for notifications and alerts.",
    "sqs:SendMessage": "Allows sending, queuing, or pushing messages into an Amazon SQS queue for background processing."
}

KeyWords={
    "read": [
        "s3:ListBucket",
        "s3:GetObject",
        "ec2:DescribeInstances",
        "dynamodb:Query",
        "cloudwatch:GetMetricData",
        "iam:GetUser"
    ],
    "write": [
        "dynamodb:PutItem",
        "logs:PutLogEvents",
        "logs:CreateLogStream",
        "sns:Publish",
        "sqs:SendMessage",
        "iam:ChangePassword" 
    ],
    "upload": [
        "s3:PutObject"
    ],
    "execute": [
        "lambda:InvokeFunction"
    ],
    "start": [
        "ec2:StartInstances"
    ],
    "stop": [
        "ec2:StopInstances"
    ],
    "notify": [
        "sns:Publish",
        "sqs:SendMessage"
    ]
}

## permission category Finding part
permission_category_descriptions = {
    "read": "Read, view, list, or retrieve data from AWS services such as S3, EC2, or DynamoDB without making any changes.",
    
    "write": "Write, create, modify, or update data or resources in AWS services like DynamoDB, CloudWatch Logs, or SQS.",
    
    "upload": "Upload, send, or put files, documents, or objects into AWS storage services such as S3 buckets.",
    
    "execute": "Run, invoke, or trigger compute functions or processes like AWS Lambda functions or Step Functions.",
    
    "start": "Start, boot up, or launch cloud compute resources such as Amazon EC2 instances or RDS databases.",
    
    "stop": "Stop, shut down, or terminate running AWS services such as EC2 instances or containers to halt activity.",

    "notify": "Send, publish, or push messages to AWS services like SNS topics or SQS queues for notifications and alerts."
}

permission_category_list=list(permission_category_descriptions.keys())

def get_permission_category(user_description):
    model=SentenceTransformer('paraphrase-MiniLM-L6-v2')
    user_embedding = model.encode(user_description, convert_to_tensor=True)
    permission_category_embeddings = model.encode(list(permission_category_descriptions.values()), convert_to_tensor=True)

    # Compute similarity
    cosine_scores = util.pytorch_cos_sim(user_embedding, permission_category_embeddings)[0]
    print(cosine_scores)
    permission_category=[]

    for ind,scores in enumerate(cosine_scores):
        if (scores*100)>=50:

            permission_category.append(permission_category_list[ind])
    #retriving_permissions(permission_category,user_description)
    return permission_category


## comparing the permission with the description

def retriving_permissions(permission_category,description):
    print(permission_category)
    model=SentenceTransformer('paraphrase-MiniLM-L6-v2')
    user_embedding = model.encode(description, convert_to_tensor=True)
    valid_permissions=["iam:ChangePassword"]
    
    for keywords in permission_category:
        for permisssion_items in KeyWords[keywords]:
            permission_embedding=model.encode(Permission_Descriptions[permisssion_items],convert_to_tensor=True)
            cosine_scores = util.pytorch_cos_sim(user_embedding, permission_embedding)[0]
            #print(permisssion_items,cosine_scores)
            if(cosine_scores*100)>=50:
                valid_permissions.append(permisssion_items)
    return valid_permissions



def retrive_actions(user_description):
    
    retriving_permissions_category=get_permission_category(user_description)
    actions=retriving_permissions(retriving_permissions_category,user_description)

    print(actions)
    return actions


#retrive_actions("Allow users to upload files to S3 and read data from DynamoDB")